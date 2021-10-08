from rest_framework import serializers
from ..models import *
from ..serializers import *
from loginapp.models import usuario 


#todos los negocios de un usuario con sus productos de



class negociosProductosPorUsuario(serializers.ModelSerializer):
        
        productos = ProductoSerializer(
        many=True,
        read_only=True
        )

        class Meta:
            model = negocio 
            fields = ['id', 'nombre', 'productos']

