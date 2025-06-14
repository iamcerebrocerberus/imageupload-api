from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['uuid', 'image', 'uploaded_at', 'analyzed_text', 'image_caption']
        read_only_fields = ['uuid', 'uploaded_at', 'analyzed_text', 'image_caption']
