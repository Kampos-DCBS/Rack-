from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('homepage/', views.lista_salas, name='homepage'),
    path('homepage/<int:id>/', views.devices_sala, name='devices'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
]