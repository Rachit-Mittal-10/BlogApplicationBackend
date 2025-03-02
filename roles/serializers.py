from .models import Roles
from rest_framework import serializers

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['name']