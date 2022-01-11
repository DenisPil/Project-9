from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .. import forms, models


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
        context = {'edit_form': edit_form,
                   'delete_form': delete_form,
                   'ticket': ticket}
    else:
        raise Http404
    return render(request, 'app/edit_ticket.html', context=context)


"""Vue qui représente la réponse a un ticket"""
@login_required
def ticket_reponse(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.uploader = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {'ticket': ticket,
               'review_form': review_form}
    return render(request, 'app/ticket_reponse.html', context=context)
