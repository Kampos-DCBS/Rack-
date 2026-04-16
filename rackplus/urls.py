from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('app/', include('core.urls')),
    path('app/', include('core.urls')),
    path('api/', include('core.api_urls')),
    path('', views.dashboard, name='dashboard'),
    path('salas/', views.lista_salas, name='salas'),
    path('salas/<int:id>/', views.devices_sala, name='devices'),
]