from django.contrib import admin

from .models import Paciente, Tessiu


# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Paciente,PacienteAdmin)

class TessiuAdmin(admin.ModelAdmin):
    list_display=('color','temperatura','inflammation','name')
    list_filter=('color','name') #FILTRAR
    ordering=('color',) #ORDENAR
    search_fields=('color',)

admin.site.register(Tessiu,TessiuAdmin)