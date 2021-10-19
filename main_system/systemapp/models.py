from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

# Create your models here.

class metodo_pago(models.Model):
    cod = models.CharField(max_length=6)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.cod + ' * ' + self.nombre

    class Meta:
        db_table = 'metodo_pago'
        verbose_name = "metodo de pago"
        verbose_name_plural = "metodos de pago"

class CIIU(models.Model):
    ciiu = models.CharField(max_length=7, unique=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.ciiu + ' * ' + self.descripcion

    class Meta:
        db_table = 'CIIU'
        verbose_name = "categoria de producto"
        verbose_name_plural = "categorias de producto"

class categoria_negocio(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_negocio'
        verbose_name = "categoria de negocio"
        verbose_name_plural = "categorias de servicio"

class categoria_servicios(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    cat_negocio = models.ForeignKey(categoria_negocio, models.DO_NOTHING)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_servicios'
        verbose_name = "categoria de servicio"
        verbose_name_plural = "categorias de servicio"


class categoria_productos(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    cat_negocio = models.ForeignKey(categoria_negocio, models.DO_NOTHING)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_productos'
        verbose_name = "categoria de producto"
        verbose_name_plural = "categorias de producto"


class tipo_usuario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_usuario'
        verbose_name = "tipo de usuario"
        verbose_name_plural = "tipos de usuarios"

class tipo_identificacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_identificacion'
        verbose_name = "tipo de identificacion"
        verbose_name_plural = "tipos de identificacion"

class tipo_empleado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_empleado'
        verbose_name = "tipo de empleado"
        verbose_name_plural = "tipos de empleados"

class cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tipo_cuenta = models.ForeignKey('tipo_cuenta', models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cuenta'
        verbose_name = "cuenta"
        verbose_name_plural = "cuentas"

class tipo_cuenta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_cuenta'
        verbose_name = "tipo de cuenta"
        verbose_name_plural = "tipos de cuentas"

class negocio(ExportModelOperationsMixin('negocio'), models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200)
    usuario = models.ForeignKey('loginapp.usuario', models.DO_NOTHING, null=True)
    telefono = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    telefono1 = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null=True)
    telefono2 = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null = True)
    correo = models.EmailField(max_length=250)
    direccion = models.CharField(max_length=100, null=True)
    ciudad = models.ForeignKey('ciudad', models.DO_NOTHING, null=True)
    imagen_64 = models.TextField(null = True)
    negocio_ciiu= models.ManyToManyField(CIIU,blank=True )
    categorias = models.ManyToManyField(categoria_negocio, blank=True)
    calificacion =  models.DecimalField(max_digits=2, decimal_places= 1, blank=True, null=True, default=5)

    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'negocio'
        verbose_name = "negocio"
        verbose_name_plural = "negocios"

class producto(ExportModelOperationsMixin('producto'), models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    disponible = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    negocio = models.ForeignKey('negocio', models.DO_NOTHING, related_name='productos', blank=True)
    categorias = models.ManyToManyField(categoria_productos, blank=True)
    calificacion =  models.DecimalField(max_digits=2, decimal_places= 1, blank=True, null=True, default=5)
    imagen_64 = models.TextField(null = True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = "producto"
        verbose_name_plural = "productos"

class servicio(ExportModelOperationsMixin('servicio'), models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    disponible = models.BooleanField(default=False, blank=True)
    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    negocio = models.ForeignKey('negocio', models.DO_NOTHING, blank=True)
    categorias = models.ManyToManyField(categoria_servicios, blank=True)
    imagen_64 = models.TextField(null = True, blank=True)
    calificacion =  models.DecimalField(max_digits=2, decimal_places= 1, blank=True, null=True, default=5)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = "servicio"
        verbose_name_plural = "servicios"



class ciudad(models.Model):
    nombre = models.CharField(max_length=150)
    departamento = models.ForeignKey('departamento', models.DO_NOTHING, db_column='departamento_id', null = True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ciudad'
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"

class departamento(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'departamento'
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"

class factura(models.Model):

    cliente = models.ForeignKey('loginapp.usuario', on_delete=models.RESTRICT, blank=True, null = True, related_name='cliente')
    domiciliario = models.ForeignKey('loginapp.usuario', on_delete=models.RESTRICT, blank=True, null = True, related_name='domiciliario')
    vendedor = models.ForeignKey('loginapp.usuario', on_delete=models.RESTRICT,blank=True, null = True, related_name='vendedor')
    negocio = models.ForeignKey('negocio', models.DO_NOTHING)
    #carrito = models.ForeignKey('carrito_compra', on_delete=models.RESTRICT, blank=True, null = True)
    productos = models.ManyToManyField(producto, through='factura_producto')
    servicios = models.ManyToManyField(servicio, through='factura_servicio', blank=True)

    valor_recibido = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null = True)
    valor_devuelto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null = True)
    valor_total = models.DecimalField(max_digits=15, decimal_places = 2, blank=True,null = True)
    metodo_pago = models.ForeignKey('metodo_pago', models.DO_NOTHING)

    fecha_creacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now=True, null = True)

    def __str__(self):
        return str(self.cliente.identificacion) + ' | ' + str(self.id)

    class Meta:
        db_table = 'factura'
        verbose_name = "factura"
        verbose_name_plural = "facturas"



class factura_producto(models.Model):
    producto = models.ForeignKey('producto', on_delete=models.DO_NOTHING)
    factura = models.ForeignKey('factura', on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(null = True)

    class Meta:
        db_table = 'factura_producto'

class factura_servicio(models.Model):
    servicio = models.ForeignKey('servicio', on_delete=models.DO_NOTHING)
    factura = models.ForeignKey('factura', on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(null = True)

    class Meta:
        db_table = 'factura_servicio'