from ..models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import *
from ..serializers import *
from .ventasSerializers import *




class VentasViews(viewsets.GenericViewSet, CreateModelMixin):
    #authentication_class = (TokenAuthentication,)
    queryset = factura.objects.all().order_by('id')
    serializer_class = VentaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = FacturaSerializer(self.perform_create(serializer))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 

    def perform_create(self, serializer):
        return serializer.save()
