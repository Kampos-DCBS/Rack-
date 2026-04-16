from django.contrib import admin
from django.urls import path, include
from core.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # LOGIN (página inicial)
    path('', login_view, name='login'),

    # APP protegida
    path('app/', include('core.urls')),

    # API
    path('api/', include('core.api_urls')),
]