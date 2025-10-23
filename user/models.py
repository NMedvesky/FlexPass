from django.db import models
from django.contrib.auth.models import User
from classroom.models import Classroom


class Student(models.Model):
    # Provided by Student
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_location = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)
    active_request = None
    flex_room = None
    flex_active = models.BooleanField(default=False)
