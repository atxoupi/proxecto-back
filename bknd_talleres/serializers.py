from rest_framework import serializers

from .models import TallerService

# Serializers define the API representation.
class TallerServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TallerService
        fields = ['id','name', 'description', 'text', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at'] 