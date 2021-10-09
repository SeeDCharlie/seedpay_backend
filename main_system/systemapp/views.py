from django.shortcuts import render
from loginapp.models import usuario
from .models import *
from rest_framework import serializers
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from loginapp.serializer import UsuarioSerializer
from loginapp.models import usuario
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .serializers import *
from .serializables.serializersUsuarios import *

# Create your views here.

class UsuarioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['get'])
    def negociosProductos(self, request, pk=None):
        queryset = negocio.objects.filter(usuario=pk)
        print(queryset)
        serializer = negociosProductosPorUsuario(queryset, many=True)
        return Response(serializer.data, status=200 )

class NegocioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = negocio.objects.all().order_by('id')
    serializer_class = NegocioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'nombre', 'categorias__nombre',  ]


class ProductoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)

    queryset = producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['negocio', 'nombre', 'negocio__usuario']

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

    queryset = categoria_productos.objects.all()
    serializer_class = CategoriaProductoSerializer

    @action(methods=['get'], detail=False, url_path='categoriaNegocio/(?P<catNegocio>[0-9]+)' )
    def getByCatNegocio(self, request,catNegocio):
        queryset = categoria_productos.objects.filter(cat_negocio=catNegocio)
        serializer = CategoriaProductoSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

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

class CarritoComprasController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = carrito_compra.objects.all().order_by('id')
    serializer_class = CarritoComprasSerializer

class FacturaController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = factura.objects.all().order_by('id')
    serializer_class = FacturaSerializer


class MetodoPagoController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = metodo_pago.objects.all().order_by('id')
    serializer_class = MetodoPagoSerializer

class CategoriaNegocioController(viewsets.ModelViewSet):
    #authentication_class = (TokenAuthentication,)
    queryset = categoria_negocio.objects.all().order_by('id')
    serializer_class = CategoriaNegocioSerializer