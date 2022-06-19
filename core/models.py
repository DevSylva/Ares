import email
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    pricing = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    starter_bonus = models.CharField(max_length=50, null=True, blank=True)
    topup_bonus = models.CharField(max_length=50, null=True, blank=True) 
    daily_interest = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Investment Plan"
        verbose_name_plural = "Investment Plans"

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Done", "Done"),
        ("Canceled", "Canceled"),
    )

    COMPLETION = (
        ("0", "0"),
        ("10", "10"),
        ("20", "20"),
        ("30", "30"),
        ("40", "40"),
        ("50", "50"),
        ("60", "60"),
        ("70", "70"),
        ("80", "80"),
        ("90", "90"),
        ("100", "100"),
    )

    TYPE = (
        ("Deposit", "Deposit"),
        ("Withdrawal", "Withdrawal")
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    plan = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0])
    completion = models.CharField(
        max_length=30, choices=COMPLETION, default=COMPLETION[9])
    type = models.CharField(max_length=30, choices=TYPE, default=TYPE[0])
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def logo(self):
        if self.type == "Deposit":
            self.image = "deposit.png"
        else:
            self.image = "withdrawal.png"

    def save(self, *args, **kwargs):
        self.logo()
        super(Transaction, self).save(*args, **kwargs)


class Payment(models.Model):

    MONTH = (
        ("1", "a month"), ("2", "2 months"),
        ("3", "3 months"),("4", "4 months"),
        ("5", "5 months"),("6", "6 months"),
        ("7", "7 months"),("8", "8 months"),
        ("9", "9 months"),("2", "10 months"),
        ("11", "11 months"),("12", "a year"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    receipt = models.ImageField(upload_to="images", null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50, choices=MONTH, default=MONTH[0])
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    btc_wallet_address = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)