from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('homepage/', views.lista_salas, name='homepage'),
    path('sala/<int:sala_id>/', views.lista_racks, name='racks'),
    path('rack/<int:rack_id>/', views.lista_devices, name='devices'),
    path('device/<int:device_id>/', views.detalhe_device, name='detalhe_device'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
    path('sala/criar/', views.criar_sala, name='criar_sala'),
    path('criar-rack/<int:sala_id>/', views.criar_rack, name='criar_rack'),
    path('device/criar/<int:rack_id>/', views.criar_device, name='criar_device'),
]
