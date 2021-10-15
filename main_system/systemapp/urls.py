from django.urls import path, include, re_path
from rest_framework import routers
from .views import *
from .ventas.ventasViews import *
from .endpoints.EndpointCategoriasProductos import EndpointCategoriaProductos
from .busquedasProductos.EndpointBusquedas import EndpointFiltroBusquedaGeneral
from .qr.qrView import *

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
router.register(r'categoriaProducto', EndpointCategoriaProductos)
router.register(r'categoriaNegocio', CategoriaNegocioController)
router.register(r'ciiu', CiiuController)
router.register(r'ciudad', CiudadController)
router.register(r'departamento', DepartamentoController)
router.register(r'carritoCompra', CarritoComprasController)
router.register(r'factura', FacturaController)
router.register(r'metodoPago', MetodoPagoController)
router.register(r'busqueda', EndpointFiltroBusquedaGeneral, basename='busquedas')
router.register(r'ventas', VentasViews)

urlpatterns = [
    path('', include(router.urls) ),
    path('qr/<int:id>', QrView.as_view())
]