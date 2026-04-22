from django.contrib import admin
from .models import Rack, Sala, Device

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sala')
    list_filter = ('sala',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_sala', 'rack', 'carregando')

    def get_sala(self, obj):
        return obj.rack.sala.nome

    get_sala.short_description = 'Sala'