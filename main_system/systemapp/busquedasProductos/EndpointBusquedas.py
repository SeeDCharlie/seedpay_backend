from ..models import *
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import  *
from .busquedaGeneralSerializer import BusquedaProductoSerializer
from ..serializers import *
from django.db.models import Q

class EndpointFiltroBusquedaGeneral(APIView):

    def get(self, request, palabra=None, *args, **kwargs):
        print("palabra : " + palabra)
        negocios = producto.objects.filter(Q(negocio__nombre__icontains = palabra) | Q(nombre__icontains = palabra) | Q(negocio__categorias__nombre__icontains = palabra) ).values('negocio').distinct('negocio')

        print(negocios)
        negociosSerialzr = BusquedaProductoSerializer(data=negocios , many=True)
                                            
        print("resultado : " + str(negocios))
        return Response(negociosSerialzr.data, status=200)

