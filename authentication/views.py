from django.shortcuts import render
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class RegisterView(CreateAPIView):
    """
        : configuring the response for POST for api path api/auth/register
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, ** kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message":"User Created successfully."},status=status.HTTP_201_CREATED)
        return Response({"message":"User not created","error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)