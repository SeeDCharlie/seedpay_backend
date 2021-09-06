from django.urls import path, include
from rest_framework import routers
from .views import UsuarioController

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioController)



urlpatterns = [
    path('', include(router.urls) ),
]