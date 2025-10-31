import uuid
from urllib.parse import urlencode

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import RequestForm
from .models import Classroom, Request


def index(request):
    return HttpResponse("Welcome to the classroom view.")


def send_request(
    student,
    current_room: Classroom,
    destination: Classroom,
    reason: str,
    round_trip: bool,
) -> str:
    if len(destination.current_students) >= destination.max_students:
        return "Room full! Unable to send request."

    if student.id in destination.current_students:
        return "Student already in room! Unable to send request."

    request = Request.objects.create(
        requesting_student=student.id,
        destination=destination.id,
        reason=reason,
        round_trip=round_trip,
    )

    current_room.active_requests.add(request)
    destination.current_students.append(student.id)
    destination.save()
    student.active_request = request
    student.save()

    return "Request Sent!"


def approve_request():
    pass


@login_required()
def request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            reason = form.get_reason()
            round_trip = form.clean()["round_trip"]

            # current_room_id = request.GET.get("current_room_id")
            current_room_id = request.user.student.current_location
            destination_room_id = request.GET.get("destination")

            current_room = Classroom.objects.get(pk=current_room_id)
            destination = Classroom.objects.get(pk=destination_room_id)

            status = send_request(
                request.user.student, current_room, destination, reason, round_trip
            )

            encoded_params = urlencode({"status": status})
            return redirect(f"/classroom/rooms?{encoded_params}")
    else:
        form = RequestForm()
    return render(request, "request.html", {"form": form})


@login_required()
def room_list(request):
    rooms = Classroom.objects.all()
    context = {"rooms": rooms}

    if request.method == "POST":
        destination_room_id = uuid.UUID(request.POST.get("room_id"))
        # destination = Classroom.objects.get(pk=room_id)

        # current_room_id = request.user.student.current_location
        # current_room = Classroom.objects.get(pk=current_room_id)

        encoded_params = urlencode({
            # "current_room_id": current_room_id,
            "destination": destination_room_id,
        })
        return redirect(f"/classroom/request?{encoded_params}")
    elif request.method == "GET":
        status = request.GET.get("status")
        context["status"] = status

    return render(request, "room_list.html", context)
