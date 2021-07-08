from django.urls import path

from . import views


urlpatterns = [
     path('tipo_cliente/',  views.tipo_clienteView.as_view()),
     path('tipo_cliente/<int:id>', views.tipo_clienteView.as_view()),
     path('cliente/', views.clienteView.as_view()),
     path('cliente/<int:id>', views.clienteView.as_view()),
]
