from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms_page = paginator.get_page(page)
    print(dir(rooms_page))
    print(vars(rooms_page))
    return render(request, "rooms/home.html", {"rooms_page": rooms_page})
