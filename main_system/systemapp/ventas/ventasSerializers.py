from rest_framework import serializers
from ..models import *
from loginapp.models import *
from loginapp.serializer import *
from ..serializers import *


class VentaSerializer(serializers.Serializer):
    
    cliente = serializers.IntegerField(allow_null=True, required=False)
    vendedor = serializers.IntegerField(allow_null=True, required=False)
    domiciliario = serializers.IntegerField(allow_null=True, required=False)
    valor_total = serializers.DecimalField(max_digits=13, decimal_places=2)
    metodo_pago = serializers.IntegerField()
    valor_recibido = serializers.DecimalField(max_digits=13, decimal_places=2, allow_null=True)
    productos = FacturaProductoSerializer(many=True)

    def create(self, validate_data):
        cliente_id =  validate_data.get('cliente')
        metodo_pago_id = validate_data.get('metodo_pago')

        productos = validate_data.get('productos') 
        devuelta = validate_data.get('valor_recibido') - validate_data.get('valor_total')
        facturaAux = factura(cliente=cliente_id, metodo_pago= metodo_pago_id,
                            valor_total = float(validate_data.get('valor_total')),
                            valor_recibido = float(validate_data.get('valor_recibido')),
                            valor_devuelto =  devuelta)
        facturaAux.save()

        self.guardarFacturaPorNegocio(productos, cliente= cliente_id, metodo_pago=metodo_pago_id)

        for productoAux in productos:
            producto = factura_producto(producto=productoAux['producto'], cantidad=productoAux['cantidad'], factura=facturaAux)
            producto.save()

        return facturaAux

    def validate_cliente(self, value):
        if value == None :
            return None
        else:
            usr = usuario.objects.get(pk=value)
            if not usr :
                raise serializers.ValidationError("El usuario no existe")
            return usr

    def validate_metodo_pago(self, value):
        metodo = metodo_pago.objects.get(pk=value)
        if not metodo :
            raise serializers.ValidationError("El metodo de pago no existe")
        return metodo

    
    def validate(self, data):
        if data['valor_recibido'] < data['valor_total']:
            raise serializers.ValidationError("el valor recibido debe ser mayor que el total a pagar")
        return data
        

    def guardarFacturaPorNegocio(self, productos, cliente= None, vendedor = None, domiciliario = None, metodo_pago = None):

        negocios = list(dict.fromkeys([product['producto'].negocio for product in productos ]))
        print("negocios : " , negocios)
        for negocioAux in negocios:
            facturaAux = factura(negocio=negocioAux, cliente=cliente, vendedor=vendedor, domiciliario=domiciliario, metodo_pago=metodo_pago )
            facturaAux.save()
            productosPorNegocio = [ factura_producto.objects.create(
                                    factura=facturaAux,
                                    producto=product['producto'], 
                                    cantidad=product['cantidad'])
                                    for product in productos if product['producto'].negocio == negocioAux]
            total_pagar = sum([ (prod.producto.precio * prod.cantidad)  for prod in productosPorNegocio ])
            facturaAux.valor_total = total_pagar
            facturaAux.valor_recibido = total_pagar
            facturaAux.valor_devuelto = 0
            facturaAux.save(update_fields=['valor_total', 'valor_recibido', 'valor_devuelto'])
            pedido.objects.create(factura=facturaAux)

