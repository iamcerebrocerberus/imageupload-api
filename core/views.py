from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadedImageSerializer

class Home(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "All good"})


class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        image = request.FILES.get("image")
        if not image:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        uploaded = UploadedImage.objects.create(user=request.user, image=image)
        serializer = UploadedImageSerializer(uploaded)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
