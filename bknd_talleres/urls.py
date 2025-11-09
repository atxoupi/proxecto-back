from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TallerServiceViewSet

router = DefaultRouter()
router.register(r'talleres', TallerServiceViewSet, basename='tallerservice')

urlpatterns = [
    path('', include(router.urls)),
]
