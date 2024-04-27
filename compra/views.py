from django.shortcuts import get_object_or_404, redirect, render
from .models import Producto, Proveedor
from .forms import ProductForm, ProveedorForm
from django.urls import reverse
# Create your views here. (CRUD)

#CREAR
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
def mostrar_index(request):
    return render(request, 'index.html')

#MOSTRAR
def mostrar_listaProducto(request):
    productos = Producto.objects.all()
    return render(request, 'lista_producto.html', {'productos': productos})

def mostrar_listaProveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedor.html', {'proveedores': proveedores})

def mostrar_detalleProducto(request):
    return render(request, 'lista_producto.html')

#MODIFICAR
def update_producto(request, producto_id):
    productoNuevo = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=productoNuevo)
        if form.is_valid():
            form.save()
            return redirect('lista_producto')
    else:
        form = ProductForm(instance=productoNuevo)
    return render (request, 'editar_producto.html', {'form': form, 'producto': productoNuevo, 'activo': 'editar_producto'})

def update_proveedor(request, proveedor_id):
    proveedorNuevo = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedorNuevo)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedor')
    else:
        form = ProveedorForm(instance=proveedorNuevo)
    return render (request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedorNuevo, 'activo': 'editar_proveedor'})
        
#ELIMINAR
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('listado_producto'))
    return render(request, 'eliminar_producto.html', {'producto': producto, 'activo': 'eliminar_producto'})
    
def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('listado_proveedor'))
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor, 'activo': 'eliminar_proveedor'})


