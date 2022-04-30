import email
from unicodedata import name
from django.db import models

# Create your models here.


class Teacher(models.Model):
    TITLE = (
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
    )

    FUNCTION = (
        ("Administrative", "Administrative"),
        ("Academic", "Academic"),
        ("Physique", "Physique"),
    )

    title = models.CharField(choices=TITLE, default=TITLE[0], max_length=4)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    function = models.CharField(choices=FUNCTION, max_length=150)
    date_created = models.DateField(auto_now=True)
    avatar = models.ImageField()

    def imageUrl(self):
        if self.avatar:
            return self.avatar.url
        else:
            return self.avatar

    def __str__(self):
        return "{} {} {}".format(self.title, self.first_name, self.last_name)


class Student(models.Model):
    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    sex = models.CharField(max_length=2, choices=SEX, default=SEX[0])
    age = models.PositiveIntegerField
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(null=True, blank=True)
    avatar = models.ImageField()
    address = models.TextField()

    def imageUrl(self):
        if self.avatar:
            return self.avatar.url
        else:
            return self.avatar

    def __str__(self):
        return self.name


class Project(models.Model):

    STATUS = (
        ("Not started", "Not started"),
        ("Working", "Working"),
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

    logo = models.ImageField(null=True)
    name = models.CharField(max_length=40)
    budget = models.FloatField()
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0])
    completion = models.CharField(max_length=30, choices=COMPLETION, default=COMPLETION[0])
    date_created =  models.DateField(auto_now=True)

    def __str__(self):
        return self.name