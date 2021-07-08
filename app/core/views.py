
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import Tipo_clienteSerializer
from .serializer import ClienteSerializer

from .models import Tipo_cliente
from .models import Cliente

class tipo_clienteView(APIView):

    serializer_class = Tipo_clienteSerializer

    def get(self, request, id=None):
        if id:
            try:
                queryset = Tipo_cliente.objects.get(id_tipo_cliente=id)
            except Tipo_cliente.DoesNotExist:
                return Response({'status': 'No existe ese tipo de cliente'}, status=400)
            serializer = Tipo_clienteSerializer(queryset)
            return Response(serializer.data)
        else:
            queryset = Tipo_cliente.objects.all()
            read_serializer = Tipo_clienteSerializer(queryset, many=True)
            return Response(read_serializer.data)

    def post(self, request, *args, **kwargs):
        tipo_cliente_datos= request.data

        nuevo_tipo_cliente = Tipo_cliente(
            tipo_cliente=tipo_cliente_datos["tipo_cliente"]
        )

        nuevo_tipo_cliente.save()
        serializer = Tipo_clienteSerializer(nuevo_tipo_cliente)
        return Response(serializer.data)


class clienteView(APIView):
    serializer_class = ClienteSerializer

    def get(self, request, id=None):
        if id:
            try:
                queryset = Cliente.objects.get(id_cliente=id)
            except Cliente.DoesNotExist:
                return Response({'status': 'No existe ese cliente'}, status=400)
            serializer = ClienteSerializer(queryset)
            return Response(serializer.data)
        else:
            queryset = Cliente.objects.all()
            read_serializer = ClienteSerializer(queryset, many=True)
            return Response(read_serializer.data)

    def post(self, request, *args, **kwargs):
        cliente_datos = request.data

        tipo_cliente = Tipo_cliente.objects.get(id_tipo_cliente=cliente_datos["fk_tipo_cliente"])

        nuevo_cliente = Cliente(

        nombre = cliente_datos["nombre"],
        codigo = cliente_datos["codigo"],
        fotografia = cliente_datos["fotografia"],
        direccion = cliente_datos["direccion"],
        fk_tipo_cliente=tipo_cliente,

        )

        nuevo_cliente.save()
        serializer = ClienteSerializer(nuevo_cliente)
        return Response(serializer.data)
