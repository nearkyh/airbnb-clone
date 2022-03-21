from django.utils import timezone
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import Http404
from . import models


class HomeView(ListView):
    """HomeView"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):
    """RoomDetail"""

    model = models.Room
    pk_url_kwarg = "rename_pk"
