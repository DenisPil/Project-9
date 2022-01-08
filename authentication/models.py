from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

""" Class qui représente les utilisateurs"""
class User(AbstractUser):
    follows = models.ManyToManyField('self', through='UserFollows', related_name='followers', blank=True)


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_by')
    
    class Meta():
        unique_together = ('user','followed_user')

