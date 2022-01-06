from django import forms
from django.db.models import fields
from . import models


"""Formulaire pour la création de nouveau ticket"""
class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['book_name','author_book', 'content', 'image']


"""Formulaire pour la création d'une review"""
class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        fields = ['book_name', 'author_book','content', 'advised']


"""Formulaire pour delete un Ticket"""
class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


"""Formulaire pour delete un Review"""
class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
