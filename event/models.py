from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.title)
    