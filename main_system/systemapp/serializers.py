from rest_framework import serializers
from .models import *

class NegocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'nit', 'usuario', 'telefono', 'telefono1', 'telefono2', 'correo', 'direccion' ]

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = producto
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible']

class ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible']

class TipoUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = tipo_usuario
        fields = ['id','nombre', 'descripcion']

class TipoIdentificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = tipo_identificacion
        fields = ['id','nombre', 'descripcion']

class TipoEmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = tipo_empleado
        fields = ['id','nombre', 'descripcion']