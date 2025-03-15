from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import CustomUser

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username","email","password","first_name","last_name","phone_number","bio", "profile_picture"]
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            # email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            bio=validated_data["bio"],
            # profile_picture=validated_data["profile_picture"]
        )
        return user
    
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        return data