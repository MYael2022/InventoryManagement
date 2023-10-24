from django.contrib import admin
from .models import Productos, Ordenes
from django.contrib.auth.models import Group

admin.site.site_header = 'Administracion Tlapaleria'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,'cantidad','categoria' )
    list_filter = ['categoria']
# Register your models here.
admin.site.register(Productos, ProductAdmin)
admin.site.register(Ordenes)
# admin.site.unregister(Group)