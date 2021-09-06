from django.shortcuts import render
from loginapp.models import usuario
from .models import *
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from loginapp.serializer import UsuarioSerializer
from loginapp.models import usuario
from .serializers import *


# Create your views here.




class UsuarioController(viewsets.ModelViewSet):
    
    authentication_class = (TokenAuthentication,)

    queryset = usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer


class NegocioController(viewsets.ModelViewSet):
    
    #authentication_class = (TokenAuthentication,)

    queryset = negocio.objects.all().order_by('id')
    serializer_class = NegocioSerializer

class ProductoController(viewsets.ModelViewSet):
    
    #authentication_class = (TokenAuthentication,)

    queryset = producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer

class ServicioController(viewsets.ModelViewSet):
    
    #authentication_class = (TokenAuthentication,)

    queryset = servicio.objects.all().order_by('id')
    serializer_class = ServicioSerializer