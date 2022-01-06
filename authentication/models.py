from django.db import models
from django.contrib.auth.models import AbstractUser


""" Class qui représente les utilisateurs"""
class User(AbstractUser):
    CREATOR = 'CREATOR'
    FOLLOWERS = 'FOLLOWERS'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (FOLLOWERS, 'Abonné'),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

