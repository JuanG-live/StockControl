from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, Proveedor
from .forms import *
# Create your views here. (CRUD)

#READ INICIO
def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_listaProducto(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def mostrar_listaProveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedor.html', {'proveedores': proveedores})

def mostrar_detalleProducto(request):
    return render(request, 'lista_producto.html')

def mostrar_editarProducto(request):
    return render(request, 'editar_producto.html')

def mostrar_editarProveedor(request):
    return render(request, 'editar_proveedor.html')

def mostrar_eliminarProducto(request):
    return render(request, 'eliminar_producto.html')

def mostrar_eliminarProveedor(request):
    return render(request, 'eliminar_proveedor.html')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_producto')  # Redirect to a URL where you list all products
    else:
        form = ProductForm()
    return render(request, 'crear_producto.html', {'form': form})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedor')  # Redirect to a URL where you list all products
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def update_producto(request, producto_id):
    productoNuevo = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock_actual = request.POST.get('stock_actual')
        proveedor = request.POST.get('proveedor')
        productoNuevo.nombre = nombre
        productoNuevo.precio = precio
        productoNuevo.stock_actual = stock_actual
        productoNuevo.proveedor = proveedor
        productoNuevo.save()
        return redirect('lista_producto')
    return render (request, 'editar_producto.html', {'productoNuevo': productoNuevo})
        

    



