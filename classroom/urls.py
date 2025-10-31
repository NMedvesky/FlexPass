from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms", views.room_list, name="room_list"),
    path("request", views.request, name="request"),
]
