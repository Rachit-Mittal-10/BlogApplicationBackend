from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Roles
from .serializers import RoleSerializers 

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializers

    def create(self, request, *args, **kwargs):
        response = super().create(request, args, kwargs)
        return Response({"message": "Role Successfully created"}, status=status.HTTP_201_CREATED)