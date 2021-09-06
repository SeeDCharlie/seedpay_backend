from .models import usuario
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate, login, logout
# Create your views here.



class GenerateToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        #,{'token': token.key, 'id': user.pk, 'email': user.email, 'nombre': user. }
        user.token = token
        userSerializer = UsuarioSerializer(user)
        return Response(userSerializer.data )

