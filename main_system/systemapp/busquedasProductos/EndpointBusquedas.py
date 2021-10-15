from ..models import *
from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import  *
from .busquedaGeneralSerializer import BusquedaProductoSerializer

class EndpointFiltroBusquedaGeneral(viewsets.ReadOnlyModelViewSet):
    queryset = negocio.objects.all()
    serializer_class = BusquedaProductoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categorias__nombre']

