from email.policy import default
from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    avatarr = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER, default=GENDER[0])
    email = models.EmailField(unique=True, max_length=250)
    mobile = PhoneNumberField(default="")
    location = models.CharField(max_length=50, null=True, blank=True)
    alaye = models.CharField(max_length=50, null=True, blank=True)
    account_balance = models.FloatField(default=0)
    percentage = models.CharField(max_length=50, null=True, blank=True)
    total_deposit = models.FloatField(default=0)
    referral = models.CharField(max_length=50, null=True, blank=True)

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

    def percent(self):
        try:
            percent_ = ((int(self.account_balance) - int(self.total_deposit))/int(self.total_deposit)) * 100
            _percent = round(percent_, 2)
            if _percent >= 0:
                self.percentage = f"+{_percent}%"
            else:
                self.percentage = f"-{_percent}%"
        except Exception:
            self.percentage = "+0%"
        
    def save(self, *args, **kwargs):
        self.avatar()
        self.percent()
        super(User, self).save(*args, **kwargs)

