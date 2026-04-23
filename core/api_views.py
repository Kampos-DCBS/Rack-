from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Device, Rack, Sala
from .serializers import DeviceSerializer, RackSerializer, SalaSerializer


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all().order_by('nome')
    serializer_class = SalaSerializer
    permission_classes = [IsAuthenticated]


class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.select_related('sala').all().order_by('nome')
    serializer_class = RackSerializer
    permission_classes = [IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.select_related('rack', 'rack__sala').all().order_by('nome')
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]
