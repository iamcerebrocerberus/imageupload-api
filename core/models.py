import uuid
import os

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def upload_to_uuid(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.uuid}.{ext}"
    return os.path.join("uploads/", filename)


class UploadedImage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images')
    image = models.ImageField(upload_to=upload_to_uuid)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analyzed_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.uuid)
