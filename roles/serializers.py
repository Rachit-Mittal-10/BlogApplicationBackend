from .models import Roles, UserRole
from rest_framework import serializers

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['name']

class UserRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ["user","blog","role"]