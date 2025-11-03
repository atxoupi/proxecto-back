from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TallerServiceViewSet

router = DefaultRouter()
router.register(r'talleres', TallerServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
