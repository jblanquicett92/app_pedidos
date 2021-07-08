from rest_framework import serializers
from .models import Tipo_cliente
from .models import Cliente


class Tipo_clienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_cliente
        fields = ("__all__")

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ("__all__")



