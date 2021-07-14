from django.urls import path
from . import views

urlpatterns = [
    path('tipo_cliente/', views.tipo_clienteView.as_view()),
    path('tipo_cliente/<int:id>', views.tipo_clienteView.as_view()),
    path('cliente/', views.clienteView.as_view()),
    path('cliente/<int:id>', views.clienteView.as_view()),
    path('articulo/', views.ArticuloView.as_view()),
    path('articulo/<int:id>', views.ArticuloView.as_view()),
    path('proveedor/', views.ProveedorView.as_view()),
    path('proveedor/<int:id>', views.ProveedorView.as_view()),
    path('empresa_asociada/', views.Empresa_asociadaView.as_view()),
    path('empresa_asociada/<int:id>', views.Empresa_asociadaView.as_view()),
    path('sucursal/', views.SucursalView.as_view()),
    path('sucursal/<int:id>', views.SucursalView.as_view()),
    path('centro_distribucion/', views.Centro_distribucionView.as_view()),
    path('centro_distribucion/<int:id>', views.Centro_distribucionView.as_view()),
    path('pedido/', views.PedidoView.as_view()),
    path('pedido/<int:id>', views.PedidoView.as_view()),
    path('detalle_pedido/', views.Detalle_PedidoView.as_view()),
    path('detalle_pedido/<int:id>', views.Detalle_PedidoView.as_view()),
    path('proveedor_tiene_articulo/<int:id>', views.Proveedor_tiene_articuloView.as_view()),
    path('proveedor_tiene_articulo/', views.Proveedor_tiene_articuloView.as_view()),
    path('articulo_en_proveedor/', views.Articulo_en_proveedorView.as_view()),
    path('articulo_en_proveedor/<int:id>', views.Articulo_en_proveedorView.as_view()),
    path('admin_pedidos/crear_pedido/', views.Crear_Nuevo_PedidoViewSet.as_view({'post':'create'})),
    path('admin_pedidos/listar_urgente/', views.Listar_Pedido_UrgenteViewSet.as_view()),
]
