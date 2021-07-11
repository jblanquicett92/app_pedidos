from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import Tipo_clienteSerializer, ClienteSerializer, ArticuloSerializer, ProveedorSerializer
from .serializer import Empresa_asociadaSerializer, SucursalSerializer, Centro_distribucionSerializer
from .serializer import PedidoSerializer, DetallePedidoSerializer, Articulo_en_proveedorSerializer
from .serializer import Proveedor_tiene_articuloSerializer

from .models import Tipo_cliente, Cliente, Articulo, Proveedor, Empresa_asociada
from .models import Sucursal, Centro_distribucion, Pedido, Detalle_pedido

from django.db import connection


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

    @swagger_auto_schema(responses={200: Tipo_clienteSerializer(many=True)})
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

        tipo_cliente = Tipo_cliente.objects.get(id_tipo_cliente=cliente_datos["fk_tipo_cliente"])

        nuevo_cliente = Cliente(

            nombre=cliente_datos["nombre"],
            codigo=cliente_datos["codigo"],
            fotografia=cliente_datos["fotografia"],
            direccion=cliente_datos["direccion"],
            fk_tipo_cliente=tipo_cliente

        )

        nuevo_cliente.save()
        serializer = ClienteSerializer(nuevo_cliente)
        return Response(serializer.data)



class ArticuloView(APIView):
    serializer_class = ArticuloSerializer

    user_response = openapi.Response(
        'Si la consulta es / entrega una lista [] de lo contrario si es: /{id} un objeto { }', serializer_class)

    @swagger_auto_schema(responses={200: user_response})
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

    test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
    user_response = openapi.Response('response description', ArticuloSerializer)

    codigo = openapi.Parameter('codigo',
                               in_=openapi.IN_QUERY,
                               description='Indica clave alfanumerica con la que relacionaran la descripcion del equipo',
                               type=openapi.TYPE_STRING,
                               required=False
                               )
    descripcion = openapi.Parameter('descripcion',
                                    in_=openapi.IN_QUERY,
                                    description='Indica que articulo es, por ejemplo: Teclado, Laptop',
                                    type=openapi.TYPE_STRING,
                                    required=False
                                    )
    precio = openapi.Parameter('precio',
                               in_=openapi.IN_QUERY,
                               description='Valor numerico que represanta el costo del articulo',
                               type=openapi.TYPE_INTEGER,
                               required=False
                               )
    user_response = openapi.Response(
        'Si la consulta es / entrega una lista [] de lo contrario si es: /{id} un objeto { }', serializer_class)

    @swagger_auto_schema(manual_parameters=[codigo, descripcion, precio], responses={200: user_response})
    def post(self, request, *args, **kwargs):
        '''Servicio para crear un nuevo articulo'''
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


class PedidoView(APIView):
    class_serializer = PedidoSerializer
    #class_serializer_2 = DetallePedidoSerializer

    def get(self, request, id=None):
        if id:
            try:
                pedido = Pedido.objects.get(id_pedido=id)
            except Pedido.DoesNotExist:
                return Response({'status': 'no existe ese pedido'}, status=400)
            serializer = PedidoSerializer(pedido)
            return Response(serializer.data)
        else:
            pedido = Pedido.objects.all()
            serializer = PedidoSerializer(pedido, many=True)
            return Response(serializer.data)

    def put(self, request, id=None, *args, **kwargs):
        try:
            pedido = Pedido.objects.get(id_pedido=id)
        except Pedido.DoesNotExist:
            return Response({'status': 'no existe ese pedido'}, status=400)

        pedido_datos = request.data

        pedido.fecha_surte_pedido=pedido_datos['fecha_surte_pedido']
        pedido.hora_surte_pedido=pedido_datos['hora_surte_pedido']

        pedido.save()
        serializer = PedidoSerializer(pedido)
        return Response(serializer)

    def post(self, request, *args, **kwargs):
        datos_pedido = request.data

        print(datos_pedido)

        try:
            cliente = Cliente.objects.get(id_cliente=datos_pedido['fk_cliente'])
        except Cliente.DoesNotExist:
            cliente=None

        try:
            centro_distribucion = Centro_distribucion.objects.get(
                id_centro_distribucion=datos_pedido['fk_centro_distribucion'])
        except Centro_distribucion.DoesNotExist:
            centro_distribucion=None

        try:
            sucursal = Sucursal.objects.get(id_sucursal=datos_pedido['fk_sucursal'])
        except Sucursal.DoesNotExist:
            sucursal = None

        try:
            empresa_asociada = Empresa_asociada.objects.get(id_empresa_asociada=datos_pedido['fk_empresa_asociada'])
        except Empresa_asociada.DoesNotExist:
            empresa_asociada=None



        nuevo_pedido = Pedido(
            fk_cliente=cliente,
            fecha_gen_pedido=datos_pedido['fecha_gen_pedido'],
            hora_gen_pedido=datos_pedido['hora_gen_pedido'],
            fecha_surte_pedido=None,
            hora_surte_pedido=None,
            es_urgente=datos_pedido['es_urgente'],
            fk_sucursal=sucursal,
            fk_centro_distribucion=centro_distribucion,
        )

        nuevo_pedido.save()

        nuevo_detalle = Detalle_pedido(
            fk_pedido=nuevo_pedido,
            fk_cliente=nuevo_pedido.fk_cliente

        )
        nuevo_detalle.save()

        #nuevo_detalle.fk_pedido.add(nuevo_pedido)

        proveedor = Proveedor.objects.get(id_proveedor=datos_pedido['fk_proveedor'])
        nuevo_detalle.fk_proveedor.add(proveedor)

        for art in datos_pedido['fk_articulo']:
            articulo = Articulo.objects.get(id_articulo=art['fk_articulo'])
            print(articulo)
            nuevo_detalle.fk_articulo.add(articulo)

        serializer = DetallePedidoSerializer(nuevo_detalle)
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


class Articulo_en_proveedorView(APIView):
    class_serializer = Articulo_en_proveedorSerializer

    def get(self, request, id=None):
        '''Mediante a una consulta en la URL {id}, podemos averiguar que que proveedor surte el articulo consultado'''
        if id:
            try:
                articulo = Articulo.objects.get(id_articulo=id)
            except Articulo.DoesNotExist:
                return Response({'status': 'No existe el articulo'}, status=400)
            sql = f'''SELECT
			    DISTINCT prov.id_proveedor, prov.nombre, prov.direccion
                FROM  core_detalle_pedido as dp
                    INNER JOIN core_detalle_pedido_fk_articulo as dp_art_fk
                    ON dp.id_detalle_pedido=dp_art_fk.detalle_pedido_id
                    INNER JOIN core_detalle_pedido_fk_proveedor as dp_prov_fk
                    ON dp_prov_fk.detalle_pedido_id = dp.id_detalle_pedido
                    INNER JOIN core_proveedor as prov
                    ON prov.id_proveedor = dp_prov_fk.proveedor_id
		        WHERE dp_art_fk.articulo_id ={id}'''

            cursor = connection.cursor()
            cursor.execute(sql)
            if cursor.rowcount != 0:
                articulos_en_proveedor = []
                for p in cursor.fetchall():
                    proveedor = {
                        "id_proveedor": p[0],
                        "nombre": p[1],
                        "direccion": p[2]
                    }
                    articulos_en_proveedor.append(proveedor)

                return Response({'proveedor': articulos_en_proveedor})
            return Response({'status': 'el articulo no es surtido por ningun proveedor'})
        else:
            return Response({'status': 'HTTP_400_BAD_REQUEST'}, status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):

        detalle_datos = request.data

        nuevo_detalle = Detalle_pedido()
        nuevo_detalle.save()

        proveedor = Proveedor.objects.get(id_proveedor=detalle_datos['fk_proveedor'])
        print(proveedor)
        nuevo_detalle.fk_proveedor.add(proveedor)

        for art in detalle_datos['fk_articulo']:
            articulo = Articulo.objects.get(id_articulo=art['fk_articulo'])
            print(articulo)
            nuevo_detalle.fk_articulo.add(articulo)

        serializer = Articulo_en_proveedorSerializer(nuevo_detalle)

        return Response(serializer.data)


class Proveedor_tiene_articuloView(APIView):
    class_serializer = Proveedor_tiene_articuloSerializer

    def get(self, request, id=None):

        if id:
            try:
                proveedor = Proveedor.objects.get(id_proveedor=id)
            except Proveedor.DoesNotExist:
                return Response({'status': 'No existe el proveedor'}, status=400)
            sql = f'''SELECT 
                        DISTINCT art.id_articulo, art.codigo, art.descripcion, art.precio
                        FROM  core_detalle_pedido as dp
                        INNER JOIN core_detalle_pedido_fk_articulo as dp_art_fk
                        ON dp.id_detalle_pedido=dp_art_fk.detalle_pedido_id
                        INNER JOIN core_detalle_pedido_fk_proveedor as dp_prov_fk 
                        ON dp_prov_fk.detalle_pedido_id = dp.id_detalle_pedido 
                        INNER JOIN core_articulo as art
                        ON art.id_articulo = dp_art_fk.articulo_id
            		WHERE dp_prov_fk.proveedor_id={id};'''

            cursor = connection.cursor()
            cursor.execute(sql)
            if cursor.rowcount != 0:
                proveedor_tiene_articulos = []
                for a in cursor.fetchall():
                    articulos = {
                        "id_articulo": a[0],
                        "codigo": a[1],
                        "descripcion": a[2],
                        "precio": a[3]
                    }
                    proveedor_tiene_articulos.append(articulos)

                return Response({'articulos': proveedor_tiene_articulos})
            return Response({'status': 'proveedor no surte ningun articulo'})
        else:
            return Response({'status': 'HTTP_400_BAD_REQUEST'}, status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):

        detalle_datos = request.data

        nuevo_detalle = Detalle_pedido()
        nuevo_detalle.save()

        articulo = Articulo.objects.get(id_articulo=detalle_datos['fk_articulo'])
        print(articulo)
        nuevo_detalle.fk_articulo.add(articulo)

        for prv in detalle_datos['fk_proveedor']:
            proveedor = Proveedor.objects.get(id_proveedor=prv['fk_proveedor'])
            print(proveedor)
            nuevo_detalle.fk_proveedor.add(proveedor)

        serializer = Proveedor_tiene_articuloSerializer(nuevo_detalle)

        return Response(serializer.data)
