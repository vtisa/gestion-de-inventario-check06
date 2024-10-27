from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()

class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, default='')
    celular = models.CharField(max_length=20, default='')

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Venta(models.Model):
    numero_factura = models.CharField(max_length=20, unique=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    cantidad = models.PositiveIntegerField(default=0)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)
