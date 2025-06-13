import tempfile
import shutil
import os
from uuid import UUID

from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from core.models import UploadedImage

User = get_user_model()

TEMP_MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class UploadedImageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.fake_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'someimagebytes',
            content_type='image/jpeg'
        )

    def tearDown(self):
        UploadedImage.objects.all().delete()
        if os.path.exists(TEMP_MEDIA_ROOT):
            shutil.rmtree(TEMP_MEDIA_ROOT)

    def test_uploaded_image_creation(self):
        image = UploadedImage.objects.create(
            user=self.user,
            image=self.fake_image
        )

        self.assertIsInstance(image.uuid, UUID)
        self.assertEqual(image.user, self.user)
        self.assertTrue(image.image.name.startswith("uploads/"))
        self.assertTrue(str(image).startswith(str(image.uuid)))
        self.assertIsNone(image.analyzed_text)

    def test_upload_path_format(self):
        image = UploadedImage.objects.create(
            user=self.user,
            image=self.fake_image
        )
        _, ext = os.path.splitext(image.image.name)
        self.assertEqual(ext, ".jpg")
        self.assertIn("uploads/", image.image.name)
        self.assertTrue(image.image.name.endswith(f"{image.uuid}.jpg"))
