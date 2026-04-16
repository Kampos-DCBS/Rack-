from django.contrib import admin
from .models import Sala, Device

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sala', 'processador', 'armazenamento', 'carregando')
    list_filter = ('sala', 'carregando')