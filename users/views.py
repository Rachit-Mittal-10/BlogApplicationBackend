from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, args, kwargs)
        return Response(
            data = {
                "message":"User Added Successfully"
            },
            status=status.HTTP_201_CREATED
        )