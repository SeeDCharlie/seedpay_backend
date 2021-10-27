from rest_framework import serializers
from ...models import factura

class PedidosSerializer(serializers.ModelSerializer):

    estado = serializers.CharField(source="estado.nombre")
    metodo_pago =serializers.CharField(source="metodo_pago.nombre")

    class Meta:
        model = factura
        fields = ['id', 'estado','metodo_pago','fecha_creacion','valor_total']
