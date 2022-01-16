from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .. import forms, models


@login_required
def review_creator_form(request):
    """Vue de la création d'une review'"""
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
    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'app/review_creator.html', context=context)


@login_required
def edit_review(request, review_id):
    """Vue qui modofie ou supprime un review"""
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
        context = {'edit_form': edit_form,
                   'delete_form': delete_form,
                   'review': review}
    else:
        raise Http404
    return render(request, 'app/edit_review.html', context=context)
