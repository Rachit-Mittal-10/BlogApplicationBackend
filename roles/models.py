from django.db import models
from users.models import CustomUser

# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(to = CustomUser, on_delete = models.CASCADE)
    role = models.ForeignKey(to = Roles, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('user','role')
    
    def __str__(self):
        return f"{self.user.username} - {self.role.name}"