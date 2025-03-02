from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_picture/",blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_users",  # Change reverse accessor name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users_permissions",  # Change reverse accessor name
        blank=True
    )

    def __str__(self):
        return self.username