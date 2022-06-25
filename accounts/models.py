from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(blank=False, null=False, upload_to='accounts/', default='accounts/default.jpg')
    def __str__(self):
        return self.username

