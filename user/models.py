from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gapps_key = models.CharField(max_length=16, default='')

    def __str__(self):
        return f'{self.user.username} Profile'
