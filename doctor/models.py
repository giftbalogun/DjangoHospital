from django.db import models
from datetime import datetime

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='doctor/')

    def __str__(self):
        return self.name
