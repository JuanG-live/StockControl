from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_index, name='inicio'),
    path('home/', home, name='home'),
    path('crearProducto/', crear_producto, name='crear_producto'),
    path('crearProveedor/', crear_proveedor, name='crear_proveedor'),
    path('listaProducto/', mostrar_listaProducto, name='lista_producto'),
    path('listaProveedor/', mostrar_listaProveedor, name='lista_proveedor'),
    path('editarProducto/', update_producto, name='editar_producto'),
    path('editarProveedor/<int:proveedor_id>/', update_proveedor, name='editar_proveedor'),
    path('eliminarProducto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('eliminarProveedor/<int:proveedor_id>/', eliminar_proveedor, name='eliminar_proveedor')
]
