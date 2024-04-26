from django import forms
from .models import Producto, Proveedor

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']