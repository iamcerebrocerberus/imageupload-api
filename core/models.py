import uuid

from django.db import models
from django.contrib.auth import get_user_model
from cloudinary_storage.storage import MediaCloudinaryStorage

User = get_user_model()

class UploadedImage(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(storage=MediaCloudinaryStorage, upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    analyzed_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.uuid} - {self.user.username}"
