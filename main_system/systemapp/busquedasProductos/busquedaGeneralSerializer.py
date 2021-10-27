from rest_framework import serializers
from ..models import *
from ..serializers import *

class BusquedaProductoSerializer(serializers.ModelSerializer):

    productos = ProductoSerializer( read_only=True, many=True)

    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'imagen_64', 'productos' ]

    
    def validate_productos(self, producto):
        if not producto:
            raise serializers.ValidationError("no hay productos")
        return producto