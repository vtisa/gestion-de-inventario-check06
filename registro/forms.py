from django import forms
from .models import Proveedor, Cliente, Producto, Categoria, Venta, Direccion

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        exclude = ['direccion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'

