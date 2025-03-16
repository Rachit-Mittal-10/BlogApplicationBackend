from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    - Creates the viewset for managing the user instances and provides the basic CRUD operations.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return Response(
            data = {
                "message":"Method Not Allowed"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )