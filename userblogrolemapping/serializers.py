from roles.models import UserBlogRole
from rest_framework import serializers

class UserBlogRoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserBlogRole
        fields = ["user","blog","role"]