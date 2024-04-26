from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', mostrar_index, name='inicio'),
    path('crearProducto/', crear_producto, name='crear_producto'),
    path('crearProveedor/', crear_proveedor, name='crear_proveedor'),
    path('listaProducto/', mostrar_listaProducto, name='lista_producto'),
    path('listaProveedor/', mostrar_listaProveedor, name='lista_proveedor'),
    path('editarProducto/<int:producto_id>/', update_producto, name='update_producto'),
    path('editarProveedor/', mostrar_editarProveedor, name='editar_proveedor'),
    path('eliminarProducto/', mostrar_eliminarProducto, name='eliminar_producto'),
    path('eliminarProveedor/', mostrar_eliminarProveedor, name='eliminar_proveedor')
]
