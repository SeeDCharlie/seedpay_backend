from rest_framework import serializers
from ...models import *
from ...serializers import *
from loginapp.models import *
from loginapp.serializer import *


class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = producto
        fields = ['id','nombre', 'descripcion', 'precio']

class ProductoInformeVentaGeneralSerializer(serializers.Serializer):

    producto = serializers.CharField(max_length=256)
    unidadesVendidas = serializers.IntegerField()
    valorTotal = serializers.DecimalField(max_digits=23, decimal_places=2)

class NegocioInformeVentaGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'usuario', 'correo', 'direccion' ]

class NegociosInformeVentaGeneralSerializer(serializers.Serializer):
    negocio = NegocioInformeVentaGeneralSerializer()
    productos = ProductoInformeVentaGeneralSerializer(many=True)
    total = serializers.DecimalField(max_digits=23, decimal_places=2)

class InformeVentasGeneralSerializer(serializers.Serializer):

    total = serializers.DecimalField(max_digits=13, decimal_places=2)
    negocios = NegociosInformeVentaGeneralSerializer(many=True)

class peticionInfomeVentasSerializer(serializers.Serializer):

    usuario = serializers.IntegerField()
    mes = serializers.IntegerField()
    año = serializers.IntegerField()

    def validate_usuario(self, value):
        usr = usuario.objects.filter(pk=value)
        if not usr :
            raise serializers.ValidationError("El usuario no existe")
        return usr[0]

