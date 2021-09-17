from django.db import models


# Create your models here.

class categoria_servicios(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria_servicios'
        verbose_name = "categoria de servicio"
        verbose_name_plural = "categorias de servicio"


class categoria_productos(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)

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

class negocio(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200)
    usuario = models.ForeignKey('loginapp.usuario', models.DO_NOTHING, null=True)
    telefono = models.IntegerField(default=0)
    telefono1 = models.IntegerField(blank=True,null=True)
    telefono2 = models.IntegerField(blank=True,null = True)
    correo = models.EmailField(max_length=250)
    direccion = models.CharField(max_length=100, default="")

    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'negocio'
        verbose_name = "negocio"
        verbose_name_plural = "negocios"

class producto(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    disponible = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    negocio = models.ForeignKey('negocio', models.DO_NOTHING)
    categorias = models.ManyToManyField(categoria_productos)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'producto'
        verbose_name = "producto"
        verbose_name_plural = "productos"

class servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    disponible = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    negocio = models.ForeignKey('negocio', models.DO_NOTHING)
    categorias = models.ManyToManyField(categoria_servicios)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = "servicio"
        verbose_name_plural = "servicios"



class ciudad(models.Model):
    nombre = models.CharField(max_length=150)
    departamento = models.ForeignKey('departamento', models.DO_NOTHING)

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
