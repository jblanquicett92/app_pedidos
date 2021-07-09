from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import Tipo_clienteSerializer, ClienteSerializer, ArticuloSerializer, ProveedorSerializer
from .serializer import Empresa_asociadaSerializer, SucursalSerializer, Centro_distribucionSerializer
from .serializer import PedidoSerializer, DetallePedidoSerializer, Articulo_en_proveedorSerializer

from .models import Tipo_cliente, Cliente, Articulo, Proveedor, Empresa_asociada
from .models import Sucursal, Centro_distribucion, Pedido, Detalle_pedido


class Centro_distribucionView(APIView):
    serializer_class = Centro_distribucionSerializer

    def get(self, request, id=None):
        if id:
            try:
                centro_distribucion = Centro_distribucion.objects.get(id_centro_distribucion=id)
            except Centro_distribucion.DoesNotExist:
                return Response({'status': 'El centro de distribucion no existe'})
            serializer = Centro_distribucionSerializer(centro_distribucion)
            return Response(serializer.data)
        else:
            sucursal = Centro_distribucion.objects.all()
            serializer = Centro_distribucionSerializer(sucursal, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        centro_distribucion_datos = request.data

        nueva_centro_distribucion = Centro_distribucion(

            almacen=centro_distribucion_datos['almacen'],
        )

        nueva_centro_distribucion.save()
        serialize = Centro_distribucionSerializer(nueva_centro_distribucion)
        return Response(serialize.data)


class SucursalView(APIView):
    serializer_class = SucursalSerializer

    def get(self, request, id=None):
        if id:
            try:
                sucursal = Sucursal.objects.get(id_sucursal=id)
            except Sucursal.DoesNotExist:
                return Response({'status': 'La sucursal asociada no existe'})
            serializer = SucursalSerializer(sucursal)
            return Response(serializer.data)
        else:
            sucursal = Sucursal.objects.all()
            serializer = SucursalSerializer(sucursal, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        sucursal_datos = request.data

        nueva_sucursal = Sucursal(
            referencia=sucursal_datos['referencia'],
            codigo_sucursal=sucursal_datos['codigo_sucursal'],
        )

        nueva_sucursal.save()
        serialize = SucursalSerializer(nueva_sucursal)
        return Response(serialize.data)


class Empresa_asociadaView(APIView):
    serializer_class = Empresa_asociadaSerializer

    def get(self, request, id=None):
        if id:
            try:
                empresa_asociada = Empresa_asociada.objects.get(id_empresa_asociada=id)
            except Empresa_asociada.DoesNotExist:
                return Response({'status': 'La empresa asociada no existe'})
            serializer = Empresa_asociadaSerializer(empresa_asociada)
            return Response(serializer.data)
        else:
            empresa_asociada = Empresa_asociada.objects.all()
            serializer = Empresa_asociadaSerializer(empresa_asociada, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        empresa_asociada_datos = request.data

        nueva_empresa_asociada = Empresa_asociada(
            referencia=empresa_asociada_datos['referencia'],
            codigo_socio=empresa_asociada_datos['codigo_socio'],
        )

        nueva_empresa_asociada.save()
        serialize = Empresa_asociadaSerializer(nueva_empresa_asociada)
        return Response(serialize.data)


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
        tipo_cliente_datos = request.data

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

        try:
            tipo_cliente = Tipo_cliente.objects.get(id_tipo_cliente=cliente_datos["fk_tipo_cliente"])
        except Tipo_cliente.DoesNotExist:
            return self.crear_usuario(cliente_datos["nombre"], cliente_datos["codigo"], cliente_datos["fotografia"],
                                      cliente_datos["direccion"], None)
        return self.crear_usuario(cliente_datos["nombre"], cliente_datos["codigo"], cliente_datos["fotografia"],
                                  cliente_datos["direccion"], tipo_cliente)

    def crear_usuario(self, nombre, codigo, fotografia, direccion, tipo_cliente):

        nuevo_cliente = Cliente(
            nombre=nombre,
            codigo=codigo,
            fotografia=fotografia,
            direccion=direccion,
            fk_tipo_cliente=tipo_cliente
        )

        nuevo_cliente.save()
        serializer = ClienteSerializer(nuevo_cliente)
        return Response(serializer.data)


class ArticuloView(APIView):
    serializer_class = ArticuloSerializer

    def get(self, request, id=None):

        if id:
            try:
                articulo = Articulo.objects.get(id_articulo=id)
            except Articulo.DoesNotExist:
                return Response({'status': 'No existe el Articulo'}, status=400)
            serializer = ArticuloSerializer(articulo)
            return Response(serializer.data)
        else:
            articulos = Articulo.objects.all()
            serializer = ArticuloSerializer(articulos, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        articulo_datos = request.data

        nuevo_articulo = Articulo(
            codigo=articulo_datos['codigo'],
            descripcion=articulo_datos['descripcion'],
            precio=articulo_datos['precio']
        )

        nuevo_articulo.save()
        serializer = ArticuloSerializer(nuevo_articulo)
        return Response(serializer.data)


class ProveedorView(APIView):
    serializer_class = ProveedorSerializer

    def get(self, request, id=None):

        if id:
            try:
                proveedor = Proveedor.objects.get(id_proveedor=id)
            except Proveedor.DoesNotExist:
                return Response({'status': 'No existe ese Proveedor'}, status=400)
            serializer = ProveedorSerializer(proveedor)
            return Response(serializer.data)
        else:
            proveedor = Proveedor.objects.all()
            serializer = ProveedorSerializer(proveedor, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        proveedor_datos = request.data

        nuevo_proveedor = Proveedor(
            nombre=proveedor_datos['nombre'],
            direccion=proveedor_datos['direccion']
        )

        nuevo_proveedor.save()
        serializer = ProveedorSerializer(nuevo_proveedor)
        return Response(serializer.data)


class Detalle_PedidoView(APIView):
    class_serializer = DetallePedidoSerializer

    def get(self, request, id=None):
        if id:
            try:
                detalle_pedido = Detalle_pedido.objects.get(id_detalle_pedido=id)
            except Detalle_pedido.DoesNotExist:
                return Response({'status': 'Detalle no existe'}, status=400)
            serializer = DetallePedidoSerializer(detalle_pedido)
            return Response(serializer.data)
        else:
            detalle_pedido = Detalle_pedido.objects.all()
            serializer = DetallePedidoSerializer(detalle_pedido, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass


class Articulo_en_proveedorView(APIView):

    class_serializer = Articulo_en_proveedorSerializer

    def get(self, request, id=None):

        if id:
            detalle_pedido = Detalle_pedido.objects.filter(fk_articulo=id)
            serializer = Articulo_en_proveedorSerializer(detalle_pedido,  many=True)
            return Response(serializer.data)
        else:
            detalle_pedido = Detalle_pedido.objects.all()
            serializer = Articulo_en_proveedorSerializer(detalle_pedido, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        detalle_datos = request.data


#        print(proveedor)
#        print(detalle_datos['fk_articulo'])

        nuevo_detalle = Detalle_pedido()
        nuevo_detalle.save()
        proveedor = Proveedor.objects.get(id_proveedor=detalle_datos['fk_proveedor'])
        nuevo_detalle.fk_proveedor.add(proveedor)


        for art in detalle_datos['fk_articulo']:
            articulo = Articulo.objects.get(id_articulo=art['fk_articulo'])
            print(articulo)
            nuevo_detalle.fk_articulo.add(articulo)


        serializer = ArticuloSerializer(nuevo_detalle)
        print(serializer)
        return Response(serializer.data)


class Proveedor_tiene_articuloView(APIView):
    class_serializer = DetallePedidoSerializer

    def get(self, request, id=None):
        pass

    def post(self, request, *args, **kwargs):
        pass
