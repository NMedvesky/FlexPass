from django.contrib import admin

# Register your models here.
from .models import Classroom, Moderator

admin.site.register(Classroom)
admin.site.register(Moderator)
