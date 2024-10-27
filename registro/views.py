# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Cliente, Producto, Categoria, Venta
from .forms import ProveedorForm, ClienteForm, ProductoForm, CategoriaForm, VentaForm,DireccionForm

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/lista_proveedores.html', {'proveedores': proveedores})

def registro_proveedor(request):
    proveedor_form = ProveedorForm()
    if request.method == 'POST':
        direccion_form = DireccionForm(request.POST)
        if direccion_form.is_valid():
            direccion = direccion_form.save()
            proveedor_form = ProveedorForm(request.POST)
            if proveedor_form.is_valid():
                proveedor = proveedor_form.save(commit=False)
                proveedor.direccion_id = direccion.id
                proveedor.save()
                return redirect('/')
    else:
        direccion_form = DireccionForm()
    return render(request, 'ventas/registro_proveedor.html', {'proveedor_form': proveedor_form, 'direccion_form': direccion_form})


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/lista_clientes.html', {'clientes': clientes})

def registro_cliente(request):
    if request.method == 'POST':
        direccion_form = DireccionForm(request.POST)
        if direccion_form.is_valid():
            direccion = direccion_form.save()
            cliente_form = ClienteForm(request.POST)
            if cliente_form.is_valid():
                cliente = cliente_form.save(commit=False)
                cliente.direccion_id = direccion.id
                cliente.save()
                return redirect('/')
    else:
        direccion_form = DireccionForm()
        cliente_form = ClienteForm()
    return render(request, 'ventas/registro_cliente.html', {'cliente_form': cliente_form, 'direccion_form': direccion_form})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def registro_producto(request):
    proveedores = Proveedor.objects.all()
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductoForm()
    return render(request, 'ventas/registro_producto.html', {'form': form, 'proveedores': proveedores, 'categorias': categorias})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/lista_categorias.html', {'categorias': categorias})

def registro_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoriaForm()
    return render(request, 'ventas/registro_categoria.html', {'form': form})


def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})

def registro_venta(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            return redirect('/')
    else:
        form = VentaForm()
        
    return render(request, 'ventas/registro_venta.html', {'form': form, 'clientes': clientes, 'productos': productos})


def mostrar_menu(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()
    
    return render(request, 'ventas/principal.html', {
        'categorias': categorias,
        'productos': productos,
        'ventas': ventas,
        'clientes': clientes,
        'proveedores': proveedores,
    })


