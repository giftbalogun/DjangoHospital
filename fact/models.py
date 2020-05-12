from django.db import models
from datetime import datetime

# Create your models here.


class Fact(models.Model):
    name = models.CharField(max_length=200)
    testimony = models.TextField(max_length=3000)

    def __str__(self):
        return self.name
