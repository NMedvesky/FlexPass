from django.contrib.auth import get_user_model

# from django.contrib.postgres.fields import ArrayField
from django.db import models


class Moderator(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Classroom(models.Model):
    moderator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=200, help_text="Description of room for flex time."
    )
    max_students = models.IntegerField(default=20)
    student_count = models.IntegerField(default=0)
    open_room = models.BooleanField(
        default=False, help_text="Is the room availible to all students?"
    )
    allowed_students = models.ManyToManyField(Moderator)
