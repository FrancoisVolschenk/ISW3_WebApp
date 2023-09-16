from django.db import models
from django.utils import timezone

class Uploads(models.Model):
    file_name = models.TextField()
    path = models.TextField()

class Log(models.Model):
    Event = models.TextField()
    Status = models.CharField(max_length = 10)
    When = models.DateTimeField(default= timezone.now)