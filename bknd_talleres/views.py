from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny

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

    def perform_create(self, serializer):
        serializer.save()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")

        if not image:
            return Response({"error": "No se envió ninguna imagen"}, status=400)

        path = default_storage.save(f"talleres/{image.name}", image)
        image_url = request.build_absolute_uri(f"/media/{path}")

        return Response({"url": image_url})
