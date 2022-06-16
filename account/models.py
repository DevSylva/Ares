from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=250)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    alaye = models.CharField(max_length=50, null=True, blank=True)
    account_balance = models.CharField(max_length=50, null=True, blank=True, default="0")
    percentage = models.CharField(max_length=50, null=True, blank=True, default="+0%")
    total_deposit = models.CharField(max_length=50, null=True, blank=True, default="0")

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email


