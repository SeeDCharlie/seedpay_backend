from ...models import *
from rest_framework.response import Response
from rest_framework.mixins import *
from ...serializers import *
from .ventaEfectivoSerializer import *
from rest_framework.views import APIView




class VentasEfectivoViews(APIView):
    

    def get(self, request, format=None, *args, **kwargs ):
        dat = {}
        return Response(dat)