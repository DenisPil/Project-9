from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from itertools import chain
from .. import models


"""Vue de la page d'acceuil"""
@login_required
def home(request):
    tickets = models.Ticket.objects.filter(uploader__in=request.user.follows.all())
    reviews = models.Review.objects.filter(
        Q(uploader__in=request.user.follows.all()) | Q(uploader__in=request.user.followeds_by.all()))
    follower = request.user.follows.all()
    tickets_and_reviews = sorted(chain(tickets, reviews),
                                 key=lambda instance: instance.date_created,
                                 reverse=True)
    paginator = Paginator(tickets_and_reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, "follower": follower}
    return render(request, 'app/home.html', context=context)


""" Vue de la page post qui représente les ticket et review de l'utilisateur"""
@login_required
def post(request):
    tickets = models.Ticket.objects.filter(Q(uploader_id=request.user.id))
    reviews = models.Review.objects.filter(Q(uploader_id=request.user.id))
    tickets_and_reviews = sorted(chain(tickets, reviews),
                                 key=lambda instance: instance.date_created,
                                 reverse=True)
    paginator = Paginator(tickets_and_reviews, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'app/post.html', context=context)
