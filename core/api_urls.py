from rest_framework.routers import DefaultRouter
from .api_views import DeviceViewSet, RackViewSet, SalaViewSet

router = DefaultRouter()
router.register('salas', SalaViewSet)
router.register('racks', RackViewSet)
router.register('devices', DeviceViewSet)

urlpatterns = router.urls
