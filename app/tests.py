from django.test import TestCase

# Create your tests here.
@login_required
def follow_users(request):
    follow_form = forms.FollowUsersForm(instance=request.user)
    user = request.user
    follower = request.user.follows.all()
    p = len(follower)
    if request.method == 'POST':
        follow_form = forms.FollowUsersForm(request.POST, instance=request.user)
        if follow_form.is_valid():

            followers = follow_form.save(commit=False)
            followers.save()
            followers.follows.add(request.user)
            return redirect('home')
    return render(request, 'app/follow_users_form.html', context={'follow_form': follow_form, "follower":follower, 'p':p,} )

def unfollow_users(request, user_id):
    unfollow_form = get_object_or_404(User, id=user_id)
    delete_form = forms.DeleteFollowersForm()
    follower = request.user.follows.all()
    p = len(follower)
    if request.method == 'POST':
        if 'delete_follower' in request.POST:
            delete_form = forms.DeleteFollowersForm(request.POST)
            if delete_form.is_valid():
                unfollow_form.delete()
                return redirect('home')
    return render(request, 'app/unfollow_users_form.html', context={"follower":follower, 'p':p, 'delete_form':delete_form})