from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

""" Class qui représente les utilisateurs"""
class User(AbstractUser):
    follows = models.ManyToManyField('self', related_name='followers', blank=True)


