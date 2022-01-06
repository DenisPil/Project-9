from django.db import models
from django.conf import settings

class Ticket(models.Model):
    book_name = models.CharField(max_length=256)
    content = models.CharField(max_length=2048, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class review(models.Model):
    book_name = models.CharField(max_length=256)
    content = models.CharField(max_length=8192)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advised = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
