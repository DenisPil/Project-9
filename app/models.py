from django.db import models
from django.conf import settings


"""Modele de Ticket """
class Ticket(models.Model):
    book_name = models.CharField(max_length=256, verbose_name='Nom du livre')
    author_book = models.CharField(max_length=256, verbose_name='Auteur', blank=True)
    content = models.CharField(max_length=2048, blank=True, verbose_name='Information demandé (facultatif)')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


"""Modele de Review """
class Review(models.Model):
    book_name = models.CharField(max_length=256, verbose_name='nom du livre')
    author_book = models.CharField(max_length=256, verbose_name='Auteur', blank=True)
    content = models.CharField(max_length=8192, verbose_name='Votre avis')
    review_from_ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advised = models.BooleanField(default=False, verbose_name='Recommandé')
    date_created = models.DateTimeField(auto_now_add=True)
