from ..models import *
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import  *
from .busquedaGeneralSerializer import BusquedaProductoSerializer
from ..serializers import *
from django.db.models import Q



@api_view(['GET'])
def endpointFiltroBusquedaGeneral(request, palabra="Sour Puss - Tangerine"):
    print("palabra : " + palabra)
    filtroNegocios = negocio.objects.filter(Q(nombre__icontains = palabra) |
                Q(categorias__nombre__icontains = palabra) | Q(productos__nombre__icontains = palabra) | 
                Q(productos__categorias__nombre__icontains = palabra) | Q(productos__descripcion__icontains = palabra) ).distinct()
    negociosSerialzr = BusquedaProductoSerializer(filtroNegocios , many=True)
    return Response(negociosSerialzr.data, status=200)

