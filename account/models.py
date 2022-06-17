from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    avatarr = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER, default=GENDER[0])
    email = models.EmailField(unique=True, max_length=250)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    alaye = models.CharField(max_length=50, null=True, blank=True)
    account_balance = models.CharField(max_length=50, null=True, blank=True, default="$0")
    percentage = models.CharField(max_length=50, null=True, blank=True, default="+0%")
    total_deposit = models.CharField(max_length=50, null=True, blank=True, default="$0")

    REQUIRED_FIELDS = ['email', 'gender', 'mobile']

    def __str__(self):
        return self.email

    def avatar(self):
        if self.gender == "Male":
            self.avatarr = "male-avatar.png"
        elif self.gender == "Female":
            self.avatarr = "female-avatar.png"
        else:
            self.avatarr = None

    def save(self, *args, **kwargs):
        self.avatar()
        super(User, self).save(*args, **kwargs)

