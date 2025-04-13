from django.db import models

from blogs.models import CustomBlog
from roles.models import Roles
from users.models import CustomUser

# Create your models here.
class UserBlogRole(models.Model):
    """
    : creates the user role table for many to many mapping between customuser table and roles table
    """
    user = models.ForeignKey(to = CustomUser, on_delete = models.CASCADE,null=True)
    blog = models.ForeignKey(to = CustomBlog, on_delete = models.CASCADE,null=True)
    role = models.ForeignKey(to = Roles, on_delete = models.CASCADE,null=True)

    class Meta:
        unique_together = ('user','blog')
    
    def __str__(self):
        return f"{self.user.username} - {self.role.name}"