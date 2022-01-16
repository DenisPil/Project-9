from django.contrib.auth import get_user_model
from django import forms

from . import models

User = get_user_model()


class TicketForm(forms.ModelForm):
    """Formulaire pour la création de nouveau ticket"""
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['book_name', 'author_book', 'content', 'image']


class ReviewForm(forms.ModelForm):
    """Formulaire pour la création d'une review"""
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'content', 'rating']


class DeleteTicketForm(forms.Form):
    """Formulaire pour delete un Ticket"""
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteReviewForm(forms.Form):
    """Formulaire pour delete un Review"""
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    """Formulaire pour suivre un utilisateur"""
    add_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = User
        fields = ['follows']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['follows'].queryset = User.objects.exclude(
            username="admin").exclude(username=self.instance.username)


class DeleteFollowersForm(forms.Form):
    """Formulaire pour ne plus suivre un utilisateur"""
    delete_follower = forms.BooleanField(widget=forms.HiddenInput,
                                         initial=True)


class Findusers(forms.Form):
    """Formulaire pour trouver un utilisateur"""
    find_follower = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    username = forms.CharField(max_length=128)


class TicketEditForm(forms.ModelForm):
    """Formulaire pour modifier un ticket"""
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['book_name', 'author_book', 'content']
