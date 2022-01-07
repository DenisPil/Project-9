"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', app.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket_creator/', app.views.ticket_creator_form, name='ticket-creator'),
    path('review_creator/', app.views.review_creator_form, name='review-creator'),
    path('review/<int:review_id>', app.views.view_review, name='view-review'),
    path('edit_ticket/<int:ticket_id>/', app.views.edit_ticket, name='edit-ticket'),
    path('edit_review/<int:review_id>/', app.views.edit_review, name='edit-review'),
    path('ticket/<int:ticket_id>/reponse/', app.views.ticket_reponse, name='ticket-reponse'),
    path('follow-users/', app.views.follow_users, name='follow-users'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)