from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_verified = models.BooleanField(default=False)
    auto_token = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username