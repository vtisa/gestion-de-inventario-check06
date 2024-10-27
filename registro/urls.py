from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/registro/', views.registro_proveedor, name='registro_proveedor'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/registro/', views.registro_cliente, name='registro_cliente'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/registro/', views.registro_producto, name='registro_producto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/registro/', views.registro_categoria, name='registro_categoria'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/registro/', views.registro_venta, name='registro_venta'),
    path('', views.mostrar_menu, name='principal'),
    
]