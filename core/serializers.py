from rest_framework import serializers
from .models import Device, Rack, Sala


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class RackSerializer(serializers.ModelSerializer):
    sala_nome = serializers.CharField(source='sala.nome', read_only=True)

    class Meta:
        model = Rack
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    rack_nome = serializers.CharField(source='rack.nome', read_only=True)
    sala_id = serializers.IntegerField(source='rack.sala.id', read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
