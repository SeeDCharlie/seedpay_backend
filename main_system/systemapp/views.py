from django.shortcuts import render
from loginapp.models import usuario
from .models import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from loginapp.serializer import UsuarioSerializer
from loginapp.models import usuario
from rest_framework.decorators import action
from .serializers import *


# Create your views here.

class UsuarioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer

class NegocioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = negocio.objects.all().order_by('id')
    serializer_class = NegocioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'nombre']


class ProductoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['negocio', 'nombre']

class ServicioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = servicio.objects.all().order_by('id')
    serializer_class = ServicioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['negocio', 'nombre']

class TipoUsuarioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = tipo_usuario.objects.all().order_by('id')
    serializer_class = TipoUsuarioSerializer

class TipoEmpleadoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = tipo_empleado.objects.all().order_by('id')
    serializer_class = TipoEmpleadoSerializer

class TipoIdentificacionController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = tipo_identificacion.objects.all().order_by('id')
    serializer_class = TipoIdentificacionSerializer

class CategoriaServicioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = categoria_servicios.objects.all().order_by('id')
    serializer_class = CategoriaServicioSerializer

class CategoriaProductoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = categoria_productos.objects.all().order_by('id')
    serializer_class = CategoriaProductoSerializer

class CiiuController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = CIIU.objects.all().order_by('id')
    serializer_class = CiiuSerializer

class CiudadController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = ciudad.objects.all().order_by('id')
    serializer_class = CiudadSerializer

class DepartamentoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = departamento.objects.all().order_by('id')
    serializer_class = DepartamentoSerializer