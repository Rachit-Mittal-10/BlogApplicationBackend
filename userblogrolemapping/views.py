from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from roles.models import Roles
from roles.serializers import RoleSerializers

# Create your views here.
class UserBlogRoleViewSet(viewsets.ModelViewSet):
    """
        - creates the viewsets for managing the user role api
        - methods: [POST, GET, PATCH]
    """
    queryset = Roles.objects.all()
    serializer_class = RoleSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        pass  