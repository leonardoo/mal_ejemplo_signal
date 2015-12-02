from django.contrib.auth import forms, models
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic

from rest_framework.authtoken.models import Token

from .models import User


class CreateUserView(generic.CreateView):

    form_class = forms.UserCreationForm
    success_url = reverse_lazy("created_user")
    template_name = "user/create.html"


class CreateUserView(generic.CreateView):

    model = User
    fields = ("name", "plan")
    success_url = reverse_lazy("test_created_user")
    template_name = "user/create.html"


def user_create(request):
    user = models.User.objects.last()
    token = user.auth_token
    return render(request, "user/created.html", {"usuario": user.username,
                                                 "token": token.key})
