from rest_framework import serializers
from ...models import pedido, factura, factura_producto
from ...serializers import FacturaSerializer, MetodoPagoSerializer, EstadoPedidoSerializer, EstadoFacturaSerializer, ProductoSerializer, UsuarioSerializer

class ProductoFacturaSerializer(serializers.ModelSerializer):

    producto = serializers.CharField(source="producto.nombre")

    class Meta:
        model = factura_producto
        fields = ['producto', 'cantidad']

class FacturaPedidoSerializer(serializers.ModelSerializer):

    productos = ProductoFacturaSerializer(many=True, read_only=True, source='factura_producto_set')
    metodo_pago = MetodoPagoSerializer()
    cliente = UsuarioSerializer()
    cliente = UsuarioSerializer()
    estado = EstadoFacturaSerializer()
    class Meta:
        model = factura
        fields = ['id', 'productos', 'metodo_pago', 'estado','cliente', 'domiciliario', 'valor_total']

class PedidosSerializer(serializers.ModelSerializer):
    
    factura = FacturaPedidoSerializer()
    estado = EstadoPedidoSerializer()

    class Meta:
        model = pedido
        fields = '__all__'
