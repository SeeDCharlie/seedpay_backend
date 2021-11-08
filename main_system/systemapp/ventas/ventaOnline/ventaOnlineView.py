from ...models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.mixins import *
from ...serializers import *
from .ventaOnlineSerializer import *




class VentasOnlineViews(viewsets.GenericViewSet, CreateModelMixin):
    pass