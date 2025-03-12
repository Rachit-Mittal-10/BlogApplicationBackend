from django.shortcuts import render
from .serializers import LoginSerializer

# Create your views here.
class LoginView:
    serializer_class = LoginSerializer