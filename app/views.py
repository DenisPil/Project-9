
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

from itertools import chain
from . import forms, models
from authentication.models import User

"""Vue de la page d'acceuil"""
@login_required
def home(request):
    tickets = models.Ticket.objects.filter(uploader__in=request.user.follows.all())
    reviews = models.Review.objects.filter(
        Q(uploader__in=request.user.follows.all())|Q(uploader__in=request.user.followeds_by.all()))
    follower = request.user.follows.all()
    tickets_and_reviews = sorted(
                                chain(tickets,reviews), 
                                key=lambda instance: instance.date_created, 
                                reverse=True
                                )

    paginator = Paginator(tickets_and_reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, "follower":follower}
    return render(request, 'app/home.html', context=context)

@login_required
def post(request):
    tickets = models.Ticket.objects.filter(Q(uploader_id= request.user.id))
    reviews = models.Review.objects.filter(Q(uploader_id= request.user.id))
    tickets_and_reviews = sorted(
                                chain(tickets,reviews), 
                                key=lambda instance: instance.date_created, 
                                reverse=True
                                )

    paginator = Paginator(tickets_and_reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'app/post.html', context=context)

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
            request.user.ticket_uploaded = ticket
            return redirect('home')
    return render(request, 'app/ticket_creator.html', context={'form': form})


"""Vue de la création d'une review'"""
@login_required
def review_creator_form(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.uploader = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.uploader = request.user
            review.ticket = ticket
            review.save()
        return redirect('home')
    return render(request, 'app/review_creator.html', context=
                  {'ticket_form': ticket_form,'review_form': review_form})





"""Vue qui modofie ou supprime un ticket"""
@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketEditForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if ticket.uploader == request.user:
        if request.method == 'POST':
            if 'edit_ticket' in request.POST:
                edit_form = forms.TicketEditForm(request.POST, instance=ticket)
                if edit_form.is_valid():
                    edit_form.save()
                    return redirect('home')
            if 'delete_ticket' in request.POST:
                delete_form = forms.DeleteTicketForm(request.POST)
                if delete_form.is_valid():
                    ticket.delete()
                    return redirect('home')
        context = {
                    'edit_form': edit_form,
                    'delete_form': delete_form,
                    'ticket': ticket
                }
    else:
        raise Http404
    return render(request, 'app/edit_ticket.html', context=context)


"""Vue qui modofie ou supprime un review"""
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if review.uploader == request.user:
        if request.method == 'POST':
            if 'edit_review' in request.POST:
                edit_form = forms.ReviewForm(request.POST, instance=review)
                if edit_form.is_valid():
                    edit_form.save()
                    return redirect('home')
            if 'delete_review' in request.POST:
                delete_form = forms.DeleteReviewForm(request.POST)
                if delete_form.is_valid():
                    review.delete()
                    return redirect('home')
        context = {
                    'edit_form': edit_form,
                    'delete_form': delete_form,
                    'review':review
                }
    else:
        raise Http404
    return render(request, 'app/edit_review.html', context=context)


"""Vue qui représente la réponse a un ticket"""
@login_required
def ticket_reponse(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id= ticket_id)
    review_form = forms.ReviewForm()
    
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.uploader = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
                'ticket': ticket,
                'review_form': review_form
              }
    return render(request, 'app/ticket_reponse.html', context=context)


""" Vue qui permet de suivre un utilisateur ou de le trouver"""
@login_required
def follow_users(request):
    find_user = forms.Findusers()
    form = forms.FollowUsersForm(instance=request.user)
    follower = request.user.follows.all()
    all_users = User.objects.all()
    if request.method == 'POST':
        if 'add_follower' in request.POST:
            form = forms.FollowUsersForm(request.POST, instance=request.user)
            if form.is_valid():
                followers = form.save(commit=False)
                followers.save()
                request.user.follows.add(request.POST['follows'])
                return redirect('home')
        if 'find_follower' in request.POST:
            find_user = forms.Findusers(request.POST)
            for i in all_users:
                if request.POST['username'] == i.username:
                    request.user.follows.add(i)
            return redirect('home')
    return render(request, 'app/follow_users_form.html', context={'form': form,'follower':follower, "find_user":find_user})


""" Vue qui permet de ne plus suivre un utilisateur"""
@login_required
def unfollow_users(request, user_id):
    form = forms.DeleteFollowersForm()
    follower = request.user.follows.all()
    ff = request.user.followeds_by.all()
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = forms.DeleteFollowersForm(request.POST)
        if form.is_valid():
            request.user.follows.remove(user)
            return redirect('home')
    return render(request, 'app/unfollow_users_form.html', context={'form': form, 'user':user})
