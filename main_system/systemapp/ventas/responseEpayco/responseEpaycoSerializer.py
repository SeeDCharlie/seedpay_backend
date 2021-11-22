from rest_framework import serializers
from ...models import *
from loginapp.models import *
from loginapp.serializer import *
from ...serializers import *

class usuarioPedido(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=300)
    apellido =  serializers.CharField(max_length=300)
    direccion = serializers.CharField(max_length=300)
    email = serializers.CharField(max_length=300)
    celular = serializers.CharField(max_length=300)    

class productPedido(serializers.Serializer):
    producto = serializers.IntegerField()
    cantidad = serializers.IntegerField()

class facturaConfirmada(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=3000)
    invoice = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=3000)
    currency = serializers.CharField(max_length=300)
    amount = serializers.CharField(max_length=3000)
    tax_base = serializers.CharField(max_length=300)
    tax = serializers.CharField(max_length=3000)
    tax_ico = serializers.CharField(max_length=300)
    country = serializers.CharField(max_length=3000)
    lang = serializers.CharField(max_length=300)
    external = serializers.CharField(max_length=3000)
    confirmation = serializers.CharField(max_length=300)
    response = serializers.CharField(max_length=3000)
    name_billing = serializers.CharField(max_length=300)
    address_billing = serializers.CharField(max_length=3000)
    type_doc_billing = serializers.CharField(max_length=300)
    mobilephone_billing = serializers.CharField(max_length=3000)
    number_doc_billing = serializers.CharField(max_length=300)
    methodsDisable = serializers.ChoiceField(choices=['CASH'])

class pedidoSerializer(serializers.Serializer):
    usuario = usuarioPedido()
    transporte = serializers.IntegerField()
    metodo_pago = serializers.IntegerField()
    productos = productPedido(many=True)
    negocio = serializers.IntegerField()
    total = serializers.IntegerField()

    def create(self, validate_data):
        print("cliente de la feca ", validate_data)
        negocioAux = negocio.objects.all().get(pk=validate_data.get('negocio'))
        clienteAux = usuario.objects.all().get(pk=validate_data.get('usuario')['id'])
        facturaAux = factura.objects.create(cliente = clienteAux, negocio= negocioAux, 
                                            valor_total=validate_data.get('total') )
        pedidoAux = pedido.objects.create(factura=facturaAux, 
                                        direccion=clienteAux.direccion,
                                        tel_contacto=clienteAux.celular)
        descripcion = "Productos: "

        for productAux in validate_data.get('productos'):
            product = producto.objects.get(pk=productAux['producto'])
            prodcFact = factura_producto.objects.create(producto=product, factura=facturaAux, cantidad=productAux['cantidad'])
            descripcion = descripcion + "%s, "%(product.nombre)

        return facturaConfirmada({
            'name':"Compra %s"%negocioAux.nombre,
            'description': descripcion,
            'invoice': str(facturaAux.id),
            'currency':'cop',
            'amount': facturaAux.valor_total,
            'tax_base': "0",
            'tax': "0",
            'tax_ico': "0",
            'country': "co",
            'lang': "en",
            'external': "false",
            'confirmation': 'https://seedpaymain.seedcharlie.co/api/confirmationCompraEpayco',
            'response':'https://seedpay.seedcharlie.co/success',
            'name_billing': facturaAux.cliente.nombre,
            'address_billing': facturaAux.cliente.direccion,
            'type_doc_billing': "cc",
            'mobilephone_billing': facturaAux.cliente.celular,
            'number_doc_billing': facturaAux.cliente.identificacion,
            'methodsDisable':['CASH']
        })