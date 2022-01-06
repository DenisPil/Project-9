from django.db import models
from django.conf import settings

from PIL import Image


"""Modele de Ticket """
class Ticket(models.Model):
    book_name = models.CharField(max_length=256, verbose_name='Nom du livre')
    author_book = models.CharField(max_length=256, verbose_name='Auteur', blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.CharField(max_length=2048, blank=True, verbose_name='Information demandé (facultatif)')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


"""Modele de Review """
class Review(models.Model):
    book_name = models.CharField(max_length=256, verbose_name='nom du livre')
    author_book = models.CharField(max_length=256, verbose_name='Auteur', blank=True)
    content = models.CharField(max_length=8192, verbose_name='Votre avis')
    review_from_ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL,)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advised = models.BooleanField(default=False, verbose_name='Recommandé')
    date_created = models.DateTimeField(auto_now_add=True)
