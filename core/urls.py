from django.urls import path
from .views import Home, UploadImageView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('image/upload/', UploadImageView.as_view(), name='upload-image'),
]
