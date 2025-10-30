import uuid

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Classroom, Request


def index(request):
    return HttpResponse("Welcome to the classroom view.")


def send_request(
    student,
    current_room: Classroom,
    destination: Classroom,
    reason: str,
    round_trip: bool,
) -> bool:
    if len(destination.current_students) >= destination.max_students:
        return False

    request = Request.objects.create(
        requesting_student=student.id,
        destination=destination.id,
        reason=reason,
        round_trip=round_trip,
    )
    
    # print(current_room.current_students)
    # print(current_room.current_students.remove(student.id))
    # print(current_room.current_students)


def approve_request():
    pass


@login_required()
@staff_member_required()
def room_list(request):
    if request.method == "POST":
        room_id = uuid.UUID(request.POST.get("room_id"))
        destination = Classroom.objects.get(pk=room_id)

        current_room_id = request.user.student.current_location
        current_room = Classroom.objects.get(pk=current_room_id)

        print("Request")
        print(current_room)
        print(destination)

        send_request(
            request.user.student, current_room, destination, "testing reason", False
        )

    rooms = Classroom.objects.all()
    context = {"rooms": rooms}
    return render(request, "room_list.html", context)
