from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:rename_pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.search, name="search"),
]
