import uuid

from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()

class UploadedImage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images')
    image = CloudinaryField('image')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analyzed_text = models.TextField(blank=True, null=True)
    image_caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.uuid)
