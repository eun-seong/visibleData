from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class FileUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to="")
    time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

class DataImage(models.Model):
    title = models.CharField(max_length=100)
    path = models.ImageField(blank=True, upload_to="img/")
    time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title


