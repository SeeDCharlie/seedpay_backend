from ..models import *
from rest_framework import viewsets, filters, generics
from ..serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class EndpointFiltroBusquedaGeneral(viewsets.ViewSet):

    equeryset = negocio.objects.all().order_by('id')
    serializer_class = NegocioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'nombre', 'categorias__nombre',  ]
