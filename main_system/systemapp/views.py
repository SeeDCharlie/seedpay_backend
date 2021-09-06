from django.shortcuts import render
from loginapp.models import usuario
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from loginapp.serializer import UsuarioSerializer

# Create your views here.


class UsuarioController(viewsets.ModelViewSet):
    
    authentication_class = (TokenAuthentication,)

    queryset = usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer