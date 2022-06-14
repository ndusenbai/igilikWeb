from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    postType = models.ForeignKey('PostType', on_delete=models.PROTECT, null=True)
    singleType = models.ForeignKey('singleType', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null = True, on_delete=models.CASCADE)

class singleType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class postType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Comments(models.Model):
    comment = models.TextField(blank=True)
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, null=True)
    time_sent = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete=models.CASCADE)