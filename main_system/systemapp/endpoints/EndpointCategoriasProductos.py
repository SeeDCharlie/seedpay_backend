from ..models import *
from rest_framework import viewsets, filters, generics
from ..serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response


class EndpointCategoriaProductos(viewsets.ViewSet):

    queryset = categoria_productos.objects.all()

    @action(methods=['get'], detail=False, url_path='categoriaNegocio/(?P<catNegocio>[0-9]+)' )
    def getByCatNegocio(self, request,catNegocio):
        queryset = categoria_productos.objects.filter(cat_negocio=catNegocio)
        serializer = CategoriaProductoSerializer(queryset, many=True)
        return Response(serializer.data, status=200)