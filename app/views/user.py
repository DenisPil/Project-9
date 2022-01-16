from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .. import forms, models
from authentication.models import User


@login_required
def follow_users(request):
    """ Vue qui permet de suivre un utilisateur ou de le trouver"""
    find_user = forms.Findusers()
    form = forms.FollowUsersForm(instance=request.user)
    follower = request.user.follows.all()
    folowed_by = request.user.followeds_by.all()
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
    context = {'form': form,
               'follower': follower,
               "find_user": find_user,
               'folowed_by': folowed_by}
    return render(request, 'app/follow_users_form.html', context=context)


@login_required
def unfollow_users(request, user_id):
    """ Vue qui permet de ne plus suivre un utilisateur"""
    form = forms.DeleteFollowersForm()
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = forms.DeleteFollowersForm(request.POST)
        if form.is_valid():
            request.user.follows.remove(user)
            return redirect('home')
    context = {'form': form, 'user': user}
    return render(request, 'app/unfollow_users_form.html', context=context)
