from django.shortcuts import render
from rest_framework import viewsets
from .models import Roles
from .serializers import RoleSerializers

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializers