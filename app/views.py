from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import forms, models


"""Vue de la page d'acceuil"""
@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'app/home.html', context={'tickets': tickets})


"""Vue de la création de ticket"""
@login_required
def ticket_creator_form(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'app/ticket_creator.html', context={'form': form})


"""Vue de la création d'une review'"""
@login_required
def review_creator_form(request):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.uploader = request.user
            review.save()
            return redirect('home')
    return render(request, 'app/review_creator.html', context={'form': form})