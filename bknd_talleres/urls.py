from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TallerServiceViewSet, ImageUploadView, ContactFormView

router = DefaultRouter()
router.register(r'talleres', TallerServiceViewSet, basename='tallerservice')

urlpatterns = [
    path('talleres/upload/', ImageUploadView.as_view(), name='image-upload'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('', include(router.urls))
]
