from rest_framework import serializers
from .models import *

class NegocioSerializer(serializers.ModelSerializer):


    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'nit', 'usuario' ]

class ProductoSerializer(serializers.ModelSerializer):


    class Meta:
        model = producto
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible']

class ServicioSerializer(serializers.ModelSerializer):


    class Meta:
        model = servicio
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible']