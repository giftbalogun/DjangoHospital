from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
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


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
