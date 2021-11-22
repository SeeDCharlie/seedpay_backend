from django.urls import path, include, re_path
from rest_framework import routers
from .views import *
from .ventas.ventasViews import *
from .endpoints.EndpointCategoriasProductos import EndpointCategoriaProductos
from .busquedasProductos.EndpointBusquedas import *
from .qr.qrView import *
from .informes.informeVentasUsuario.informeVentaGeneralView import InformeVentasGeneralView
from  .ventas.pedidos.pedidosView import PedidosView
from  .ventas.responseEpayco.responseEpaycoView import ResponseEpaycoViews
from  .ventas.confirmationEpayco.confirmationEpaycoView import ConfirmationEpaycoView

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
router.register(r'factura', FacturaController)
router.register(r'metodoPago', MetodoPagoController)
router.register(r'ventas', VentasViews)
router.register(r'productoPaginado', ProductoPaginadoController)
router.register(r'pedidos', PedidosView)
router.register(r'tipoTransporte', TipoTransporteController)
router.register(r'responseCompraEpayco', ResponseEpaycoViews)
# router.register(r'confirmationCompraEpayco', ConfirmationEpaycoView)


urlpatterns = [
    path('', include(router.urls) ),
    path('qr/<int:id>/', QrView.as_view()),
    path('buscar/<str:palabra>/', endpointFiltroBusquedaGeneral, name='busqudageneral'),
    path('informeVentas/', InformeVentasGeneralView.as_view(), name='informeVentaGeneral'),
]