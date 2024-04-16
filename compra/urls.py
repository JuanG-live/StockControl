from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_index, name='inicio'),
    path('crearProducto/', views.mostrar_crearProducto, name='crear_producto'),
    path('crearProveedor/', views.mostrar_crearProveedor, name='crear_proveedor'),
    path('editarProducto/', views.mostrar_editarProducto, name='editar_producto'),
    path('editarProveedor/', views.mostrar_editarProveedor, name='editar_proveedor'),
    path('eliminarProducto/', views.mostrar_eliminarProducto, name='eliminar_producto'),
    path('eliminarProveedor/', views.mostrar_eliminarProveedor, name='eliminar_proveedor'),
   
]
