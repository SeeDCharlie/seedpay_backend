from ..models import *
from rest_framework import viewsets, filters, generics
from loginapp.models import usuario 
from rest_framework.decorators import action, api_view

class UsuarioController(viewsets.ViewSet):
    #authentication_class = (TokenAuthentication,)
    #serializer_class = UsuarioSerializer


    @action(detail=False, methods=['get'], url_path=r'/>')
    def negociosProductos(self, request,  args):
        queryset = negocio.objects.all().filter(usuario)