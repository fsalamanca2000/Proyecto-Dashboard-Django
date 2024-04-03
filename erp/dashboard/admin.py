from django.contrib import admin
from dashboard.models import Cliente

# Register your models here.
class DashboardAdmin(admin.ModelAdmin):
    list_display = ["Nombre", "Barrio", "Localidad", "Fecha_de_compra", "Nombre_Producto", "Valor_compra"]
    list_search = ["Nombre_Producto"]

admin.site.register(Cliente, DashboardAdmin)