from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser, Permission, Group, PermissionsMixin
from django_prometheus.models import ExportModelOperationsMixin



class usersManager(BaseUserManager):
    def create_superuser(self, email, identificacion, nombre, apellido, celular, direccion, password):
        usuario = self.create_user(email = email, identificacion = identificacion , nombre = nombre, apellido = apellido, celular = celular,  direccion = direccion, password = password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

    def create_user(self, email, identificacion , nombre, apellido, celular, direccion, password ):
        if not email:
            raise ValueError('el usuario debe tener un correo electronico')
        else :
            usuario = self.model(email = self.normalize_email(email),identificacion = identificacion , nombre = nombre, apellido = apellido, celular = celular, direccion = direccion )
            usuario.set_password(password)
            usuario.save()
            return usuario

class usuario(AbstractBaseUser, PermissionsMixin):
    
    identificacion = models.DecimalField(max_digits=13, decimal_places=0, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    celular = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    direccion = models.CharField(max_length=50, null=True)
    imagen_64 = models.CharField(max_length=200,null = True)
    token = models.CharField(max_length=300, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, auto_now_add=True, null = True)
    fecha_modificacion = models.DateTimeField(blank=True, auto_now=True, null = True)
    tipo_identificacion = models.ForeignKey('systemapp.tipo_identificacion', models.DO_NOTHING, null=True)
    tipo_usuario = models.ForeignKey('systemapp.tipo_usuario', models.DO_NOTHING, null=True)
    tipo_empleado = models.ForeignKey('systemapp.tipo_empleado', models.DO_NOTHING, null=True)
    cuenta = models.ForeignKey('systemapp.cuenta', models.DO_NOTHING, null=True)
    ciudad = models.ForeignKey('systemapp.ciudad', models.DO_NOTHING, null=True)
    activo = models.BooleanField(default=True, blank=True)
    
    usuario_administrador = models.BooleanField(default=False)
    objects = usersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'identificacion', 'nombre', 'apellido', 'celular', 'direccion' ]

    def __str__(self):
        return self.email
    
    """def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True
    """
    @property
    def is_staff(self):
        return self.usuario_administrador



    class Meta:
        db_table = 'usuarios'
        app_label = 'loginapp'
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
