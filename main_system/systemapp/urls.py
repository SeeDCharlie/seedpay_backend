from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioController)
router.register(r'negocio', NegocioController)
router.register(r'producto', ProductoController)
router.register(r'servicio', ServicioController)
router.register(r'tipoUsuario', TipoUsuarioController)
router.register(r'tipoEmpleado', TipoEmpleadoController)
router.register(r'tipoIdentificacion', TipoIdentificacionController)
router.register(r'categoriaServicio', CategoriaServicioController)
router.register(r'categoriaProducto', CategoriaProductoController)

urlpatterns = [
    path('', include(router.urls) ),
]