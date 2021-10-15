from rest_framework import serializers
from ..models import *
from ..serializers import *

class BusquedaProductoSerializer(serializers.ModelSerializer):


    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'imagen_64' ]