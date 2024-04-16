from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here. (CRUD)

#READ INICIO
def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_crearProducto(request):
    return render(request, 'crear_producto.html', {
            'form': UserCreationForm()
    })

def mostrar_crearProveedor(request):
    return render(request, 'crear_proveedor.html')

def mostrar_editarProducto(request):
    return render(request, 'editar_producto.html')

def mostrar_editarProveedor(request):
    return render(request, 'editar_proveedor.html')

def mostrar_eliminarProducto(request):
    return render(request, 'eliminar_producto.html')

def mostrar_eliminarProveedor(request):
    return render(request, 'eliminar_proveedor.html')

#CREATE

