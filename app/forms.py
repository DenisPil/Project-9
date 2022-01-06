from django import forms
from django.db.models import fields
from . import models


"""Formulaire pour la création de nouveau ticket"""
class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['book_name','author_book', 'content', 'image']


"""Formulaire pour la création d'une review"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['book_name', 'author_book','content', 'advised']
