from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import TallerService
from .serializers import TallerServiceSerializer

class TallerServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Taller Services to be viewed, created  or edited.
    """
    queryset = TallerService.objects.all()
    serializer_class = TallerServiceSerializer
    permission_classes = [permissions.AllowAny] 

    def perform_create(self, serializer):
        serializer.save()
