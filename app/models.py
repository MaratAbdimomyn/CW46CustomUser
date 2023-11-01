from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name