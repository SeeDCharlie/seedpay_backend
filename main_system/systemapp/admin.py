from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(categoria_negocio)
admin.site.register(categoria_productos)
admin.site.register(categoria_servicios)
admin.site.register(departamento)
admin.site.register(tipo_usuario)
admin.site.register(tipo_identificacion)