from .models import usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer
# Create your views here.


class UsuarioController(viewsets.ModelViewSet):
    
    queryset = usuario.objects.all().order_by('id')
    serializer_class = UsuarioSerializer
