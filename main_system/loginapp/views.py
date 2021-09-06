from .models import usuario
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

from django.contrib.auth import authenticate, login, logout
# Create your views here.





