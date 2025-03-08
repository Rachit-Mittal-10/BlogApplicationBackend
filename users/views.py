from django.shortcuts import render
from rest_framework import viewsets, status
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

    def create(self, request, *args, **kwargs):
        """
        : configuring the response for POST for api path api/users
        """
        response = super().create(request, args, kwargs)
        return Response(
            data = {
                "message":"User Added Successfully"
            },
            status=status.HTTP_201_CREATED
        )