from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    """ Class qui représente les utilisateurs"""
    followeds_by = models.ManyToManyField(
        'User', verbose_name='Users following', through='UserFollower',
        related_name='+', through_fields=('follow', 'followed_by'))
    follows = models.ManyToManyField(
        'User', verbose_name='Users being followed', through='UserFollower',
        related_name='+', through_fields=('followed_by', 'follow'))


class UserFollower(models.Model):
    follow = models.ForeignKey('User',
                               on_delete=models.CASCADE,
                               related_name='followed_by_UserFollowers')
    followed_by = models.ForeignKey('User',
                                    on_delete=models.CASCADE,
                                    related_name='follow_UserFollowers')

    class Meta:
        unique_together = ('follow', 'followed_by')
