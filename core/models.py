from django.db import models
from django.utils import timezone
from datetime import date, timedelta


# Create your models here.
class Pupil(models.Model):

    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )
    # personal info
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    age = models.CharField(max_length=4, null=True, blank=True, default="0")
    sex = models.CharField(choices=SEX, max_length=2)
    passport = models.ImageField(null=True, blank=True)

    # contact info
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=320)

    # parent/guardian info
    parent_or_guardian_name = models.TextField()
    parent_or_guardian_phone_numbers = models.TextField()

    Class = models.ForeignKey("core.Class", null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def getAge(self):
        age = (date.today() - self.date_of_birth) // timedelta(days=365.2425)
        self.age = age

    def save(self, *args, **kwargs):
        self.getAge()
        super(Pupil, self).save(*args, **kwargs)


class Teacher(models.Model):

    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )
    # personal info
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    age = models.CharField(max_length=4, null=True, blank=True, default="0")
    sex = models.CharField(choices=SEX, max_length=2)
    passport = models.ImageField(null=True, blank=True)

    # contact info
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=320)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def getAge(self):
        age = (date.today() - self.date_of_birth) // timedelta(days=365.2425)
        self.age = age

    def save(self, *args, **kwargs):
        self.getAge()
        super(Teacher, self).save(*args, **kwargs)


class Staff(models.Model):
    SEX = (
        ("M", "Male"),
        ("F", "Female"),
    )

    ROLE = (
        ("CLEANING", "CLEANING"),
        ("SECURITY", "SECURITY"),
        ("ADMINISTRATIVE", "ADMINISTRATIVE"),
    )
    # personal info
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    age = models.CharField(max_length=4, null=True, blank=True, default="0")
    sex = models.CharField(choices=SEX, max_length=2)
    passport = models.ImageField(null=True, blank=True)
    role = models.CharField(choices=ROLE, max_length=20, null=True)

    # contact info
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=320)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def getAge(self):
        age = (date.today() - self.date_of_birth) // timedelta(days=365.2425)
        self.age = age

    def save(self, *args, **kwargs):
        self.getAge()
        super(Staff, self).save(*args, **kwargs)


class Class(models.Model):
    Class = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return str(self.Class)
