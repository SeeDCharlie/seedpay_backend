from rest_framework import serializers
from .models import usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuario
        fields = ['nombre', 'apellido', 'direccion', 'email', 'celular', 'telfijo', 'identificacion', 'password' ]