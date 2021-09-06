from rest_framework import serializers
from .models import usuario

class UsuarioSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = usuario
        fields = ['id','nombre', 'apellido', 'direccion', 'email', 'celular', 'telfijo', 'identificacion', 'tipo_identificacion', 'password', 'token' ]