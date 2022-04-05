from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from . import forms
from . import models


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    initial = {"email": "nearkyh@gmail.com"}
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "Yonghan",
        "last_name": "Kim",
        "email": "nearkyh@gmail.com",
    }

    def form_valid(self, form):
        form.save()
        # Login
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # TODO: Add success message
    except models.User.DoesNotExist:
        # TODO: Add error message
        pass
    return redirect(reverse("core:home"))
