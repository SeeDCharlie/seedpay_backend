from rest_framework import viewsets, status #, filters, generics
from ...models import pedido
from .pedidosSerializer import PedidosSerializer
from rest_framework.mixins import *
from rest_framework.decorators import action
from rest_framework.response import Response

class PedidosView(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):

    queryset = pedido.objects.all().order_by('id')
    serializer_class = PedidosSerializer

    @action(methods=['get'], detail=False, url_path='vendedor/(?P<usuario_id>[0-9]+)' )
    def pedidosByVendedor(self, request, usuario_id):
        queryset = pedido.objects.filter(factura__negocio__usuario=usuario_id).order_by('id')        
        return Response(PedidosSerializer(queryset, many=True).data, status=status.HTTP_200_OK)