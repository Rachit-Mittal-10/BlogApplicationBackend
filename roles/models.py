from django.db import models
from users.models import CustomUser
from blogs.models import CustomBlog

# Create your models here.
class Roles(models.Model):
    """
    : creates the roles table
    """
    name = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.name
