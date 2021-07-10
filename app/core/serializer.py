from rest_framework import serializers
from .models import Tipo_cliente, Cliente, Articulo, Proveedor, Empresa_asociada
from .models import Sucursal, Centro_distribucion, Pedido, Detalle_pedido

class Tipo_clienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_cliente
        fields = ("__all__")

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ("__all__")

        depth = 1

class ArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulo
        fields = ("__all__")

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = ("__all__")

class Empresa_asociadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa_asociada
        fields = ("__all__")

class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursal
        fields = ("__all__")

class Centro_distribucionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Centro_distribucion
        fields = ("__all__")


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ("__all__")

        depth = 1

class DetallePedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_pedido
        fields = ("__all__")

        depth = 1

class Articulo_en_proveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_pedido
        fields = ("fk_proveedor", 'fk_articulo')

        depth = 1
#Proveedor_tiene_articuloSerializer
class Proveedor_tiene_articuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_pedido
        fields = ("fk_proveedor", 'fk_articulo')

        depth = 1






