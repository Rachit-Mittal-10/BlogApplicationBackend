from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ["username","email","password","first_name","last_name","phone_number","bio","profile_picture"]
        extra_kwargs = {
            "profile_picture":{
                "required": False,
                "allow_null": True
            }
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            bio=validated_data["bio"],
            profile_picture=validated_data.get("profile_picture")
        )
        return user
    
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        return data