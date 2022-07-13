from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    singleType = models.ForeignKey('singleType', on_delete=models.PROTECT, null=True, default=2)
    #image = models.ImageField(null=True, blank=True, upload_to='img')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('myBlog')


class singleType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class postType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    content = models.TextField(blank=True)
    ids = models.ForeignKey(Post, id, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)