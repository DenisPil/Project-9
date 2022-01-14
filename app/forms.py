from django.contrib.auth import get_user_model
from django import forms

from . import models

User = get_user_model()

"""Formulaire pour la création de nouveau ticket"""
class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['book_name', 'author_book', 'content', 'image']


"""Formulaire pour la création d'une review"""
class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'content', 'rating']


"""Formulaire pour delete un Ticket"""
class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


"""Formulaire pour delete un Review"""
class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


"""Formulaire pour suivre un utilisateur"""
class FollowUsersForm(forms.ModelForm):
    add_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = User
        fields = ['follows']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['follows'].queryset = User.objects.exclude(username="admin").exclude(username=self.instance.username)



class DeleteFollowersForm(forms.Form):
    delete_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class Findusers(forms.Form):
    find_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    username = forms.CharField(max_length=128)

class TicketEditForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['book_name', 'author_book', 'content']
