from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # LOGIN / LOGOUT
    path('', core_views.login_view, name='login'),
    path('logout/', core_views.logout_view, name='logout'),

    # APP
    path('app/', include('core.urls')),

    # API
    path('api/', include('core.api_urls')),
]

handler404 = 'core.views.erro_404'
handler500 = 'core.views.erro_500'
