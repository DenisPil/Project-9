from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import forms, models


"""Vue de la page d'acceuil"""
@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'app/home.html', context={'tickets': tickets, 'reviews': reviews})


"""Vue de la création de ticket"""
@login_required
def ticket_creator_form(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
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


"""Vue qui représente une seul review"""
@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'app/view_review.html', context={'review': review})