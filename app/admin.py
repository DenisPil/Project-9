from django.contrib import admin

# Register your models here.
from .models import Ticket
from .models import Review
from authentication.models import User
from authentication.models import UserFollower

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(UserFollower)
