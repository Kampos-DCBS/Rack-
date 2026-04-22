from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('homepage/', views.lista_salas, name='homepage'),
    path('sala/<int:sala_id>/', views.lista_racks, name='racks'),
    path('rack/<int:rack_id>/', views.lista_devices, name='devices'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
]
