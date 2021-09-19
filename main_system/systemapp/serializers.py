from rest_framework import serializers
from .models import *

class NegocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = negocio
        fields = ['id','nombre', 'descripcion', 'usuario', 'telefono', 'telefono1',
         'telefono2', 'correo', 'direccion', 'imagen_64', 'negocio_ciiu', 'categorias' ]

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = producto
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible', 'categorias', 'negocio', 'imagen_64']

class ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = ['id','nombre', 'descripcion', 'precio', 'negocio', 'disponible', 'categorias', 'negocio', 'imagen_64']

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

class CategoriaServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = categoria_servicios
        fields = ['id','nombre', 'descripcion', 'cat_negocio']

class CategoriaProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = categoria_productos
        fields = ['id','nombre', 'descripcion', 'cat_negocio']

class CiiuSerializer(serializers.ModelSerializer):

    class Meta:
        model = CIIU
        fields = ['id','ciiu', 'descripcion']

class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ciudad
        fields = ['id','nombre', 'departamento_id']

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = departamento
        fields = ['id','nombre']

class CarritoComprasSerializer(serializers.ModelSerializer):

    class Meta:
        model = carrito_compra
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = factura
        fields = '__all__'

class MetodoPagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = metodo_pago
        fields = '__all__'