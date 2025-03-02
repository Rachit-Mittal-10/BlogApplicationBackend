from .models import CustomUser
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'bio',
            'profile_picture',
            'phone_number',
        ]