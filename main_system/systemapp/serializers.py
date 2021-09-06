from rest_framework import serializers
from .models import *

class NegocioSerializer(serializers.ModelSerializer):


    class Meta:
        model = negocio
        fields = ['nombre', 'descripcion', 'nit', 'usuario' ]

class ProductoSerializer(serializers.ModelSerializer):


    class Meta:
        model = negocio
        fields = ['nombre', 'descripcion', 'precio', 'negocio', 'disponible']

class ServicioSerializer(serializers.ModelSerializer):


    class Meta:
        model = negocio
        fields = ['nombre', 'descripcion', 'precio', 'negocio', 'disponible']