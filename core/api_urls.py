from rest_framework.routers import DefaultRouter
from .api_views import DeviceViewSet

router = DefaultRouter()
router.register('devices', DeviceViewSet)

urlpatterns = router.urls