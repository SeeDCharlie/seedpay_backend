
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioController)

urlpatterns = [
    path('', include(router.urls) ),
    path('token-auth/', views.obtain_auth_token),
]