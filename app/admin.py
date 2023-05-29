from django.contrib import admin
from .models import *

# Register your models here.

class SolicitudAdmin(admin.ModelAdmin):
    list_display=('id_solicitud', 'run_cli','run_emp', 'tipo_solicitud', 'fecha_solicitud')
    
    def get_tipo_sol(self, obj):
        return obj.tipo_sol
    def get_descripcion(self, obj):
        return obj.descripcion

class InspeccionAdmin(admin.ModelAdmin):
    list_display=('estado', 'descripcion', 'valor', 'idsol', 'ideqp')



class SalidaAdmin(admin.ModelAdmin):
    list_display=('salida', 'ideqps')

admin.site.register(Solicitud, SolicitudAdmin)
