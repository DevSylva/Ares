from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


