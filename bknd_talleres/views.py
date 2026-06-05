from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from django.db.models import F
from .models import TallerService
from .serializers import TallerServiceSerializer

class TallerServiceViewSet(viewsets.ModelViewSet):
    queryset = TallerService.objects.order_by(F('date').asc(nulls_last=True))
    serializer_class = TallerServiceSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.mail import EmailMessage
from django.conf import settings
import uuid
from pathlib import Path

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")

        if not image:
            return Response({"error": "No se envió ninguna imagen"}, status=400)

        ext = Path(image.name).suffix.lower()
        filename = f"talleres/{uuid.uuid4().hex}{ext}"
        path = default_storage.save(filename, image)
        image_url = request.build_absolute_uri(f"/media/{path}")

        return Response({"url": image_url})


class ContactFormView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        nombre = request.data.get('nombre', '').strip()
        email = request.data.get('email', '').strip()
        mensaje = request.data.get('mensaje', '').strip()

        if not all([nombre, email, mensaje]):
            return Response({'error': 'Todos los campos son obligatorios.'}, status=400)

        try:
            EmailMessage(
                subject=f'Contacto web — {nombre}',
                body=f'Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            ).send(fail_silently=False)
            return Response({'ok': True})
        except Exception as e:
            return Response({'error': 'No se pudo enviar el mensaje. Inténtalo de nuevo.'}, status=500)
