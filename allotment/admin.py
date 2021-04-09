from django.contrib import admin
from .models import Student, Hostel, Room, Course
# Register your models here.

admin.site.register(Student)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Course)
