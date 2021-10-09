from ..models import *
from rest_framework import viewsets, filters, generics
from ..serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response


class EndpointFiltroBusquedaGeneral(viewsets.ViewSet):



    @action(detail=False, methods=['get'], url_path='general/')
    def filtroNombreProductoCategoria(self, request, pk=None, *args, **kwargs):

        negociosFiltro = negocio.objects.filter(categorias__nombre=kwargs['nombre'])
        serializar = NegocioSerializer(negociosFiltro, many=True)
        return Response(serializar.data, status=200)