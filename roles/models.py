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

class UserRole(models.Model):
    """
    : creates the user role table for many to many mapping between customuser table and roles table
    """
    user = models.ForeignKey(to = CustomUser, on_delete = models.CASCADE)
    blog = models.ForeignKey(to = CustomBlog, on_delete = models.CASCADE)
    role = models.ForeignKey(to = Roles, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('user','blog')
    
    def __str__(self):
        return f"{self.user.username} - {self.role.name}"