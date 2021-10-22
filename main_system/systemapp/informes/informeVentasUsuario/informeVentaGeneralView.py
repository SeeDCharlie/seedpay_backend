from django.shortcuts import render
from loginapp.models import usuario
from ...models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from loginapp.serializer import UsuarioSerializer
from loginapp.models import usuario
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from ...serializers import *
from ...serializables.serializersUsuarios import *
from rest_framework.mixins import *
from .informVentaGeneralSerializer import *
from .manejadorInformeVentasGeneral import *

class InformeVentasGeneralView(APIView, ManejadorInformeVentasGeneral):

    def post(self, request, format=None):
        peticion = peticionInfomeVentasSerializer(data = request.data)
        peticion.is_valid(raise_exception=True)
        return Response(self.ejecutar(peticion.validated_data), status=status.HTTP_200_OK)