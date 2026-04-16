from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
    path('salas/', views.lista_salas, name='salas'),
    path('salas/<int:id>/', views.devices_sala, name='devices'),
]