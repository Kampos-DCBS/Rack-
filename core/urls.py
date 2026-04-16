from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
    path('', login_view, name='login'),
]
