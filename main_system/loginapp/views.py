from .models import usuario
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
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
        userDos = authenticate(request, username=user.email, password=user.password)
        if user :
            
            token, created = Token.objects.get_or_create(user=user)
            user.token=token
            userSerializer = UsuarioSerializer(user)
            login(request, user)
            return Response(userSerializer.data)
        return Response({'msj':'credenciales incorrectas'}, status=400)

"""
'csrftoken=vEne3E9NJYOVkRpLvAnbpqz5pl8Nc1STeUOFVWNlGoA9nUilZMwThPDuXuoNnw1O; sessionid=fwqw6d5k64d51c0m2oq5azjns843ija3'}
"""
@api_view(('GET',))
def logOut( request):
    if request.user.is_authenticated :
        request.user.auth_token.delete()
    logout(request)
    return Response(status= status.HTTP_200_OK)

