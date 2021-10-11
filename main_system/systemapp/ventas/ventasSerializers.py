from rest_framework import serializers
from ..models import *
from loginapp.models import *
from loginapp.serializer import *
from ..serializers import *



class VentaSerializer(serializers.Serializer):
    usuario = serializers.IntegerField()
    total_pagar = serializers.DecimalField(max_digits=13, decimal_places=2)
    metodo_pago = serializers.IntegerField()
    productos = ProductoCarritoSerializer(many=True)
    negocio = serializers.IntegerField()
    valor_recibido = serializers.DecimalField(max_digits=13, decimal_places=2)

    def create(self, validate_data):
        usuario_id = usuario.objects.get( pk= validate_data.get('usuario'))
        metodo_pago_id = metodo_pago.objects.get( pk= validate_data.get('metodo_pago'))
        negocio_id = negocio.objects.get( pk= validate_data.get('negocio'))

        #creando carrito de compras con sus productos
        productos = validate_data.get('productos') 
        print("productos : " + str(productos))
        carrito = carrito_compra()
        carrito.save()
        
        for productoAux in productos:
            carrito_producto(carrito_compra=carrito, producto=producto.objects.get(pk=productoAux['producto'].id), cantidad=productoAux['cantidad']).save()

        return factura.objects.create(cliente=usuario_id,
                                             metodo_pago= metodo_pago_id,
                                             negocio = negocio_id, 
                                             valor_total = validate_data.get('total_pagar'),
                                             valor_recibido = validate_data.get('valor_recibido'),
                                             valor_devuelto = validate_data.get('valor_recibido') - validate_data.get('total_pagar') )
        
    def validate_usuario(self, value):
        usr = usuario.objects.filter(pk=value).exists()
        if not usr :
            raise serializers.ValidationError("El usuario no existe")
        return value

    def validate_metodo_pago(self, value):
        metodo = metodo_pago.objects.filter(pk=value).exists()
        if not metodo :
            raise serializers.ValidationError("El metodo de pago no existe")
        return value

    def validate_negocio(self, value):
        negocioaux = negocio.objects.filter(pk=value).exists()
        if not negocioaux :
            raise serializers.ValidationError("El metodo de pago no existe")
        return value