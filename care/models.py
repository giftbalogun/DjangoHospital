from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Blog(models.Model):
    # Create your models here.
    title = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    categories = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-details', kwargs={
            'id': self.id
        })
