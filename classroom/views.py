from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Classroom


def index(request):
    return HttpResponse("Welcome to the classroom view.")


@login_required()
@staff_member_required()
def room_list(request):
    rooms = Classroom.objects.all()
    context = {"rooms": rooms}
    return render(request, "room_list.html", context)
