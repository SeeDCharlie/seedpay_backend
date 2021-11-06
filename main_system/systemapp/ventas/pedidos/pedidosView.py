from rest_framework import viewsets #, filters, generics
from ...models import pedido
from .pedidosSerializer import PedidosSerializer
from rest_framework.mixins import *

class PedidosView(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):

    queryset = pedido.objects.all().order_by('id')
    serializer_class = PedidosSerializer