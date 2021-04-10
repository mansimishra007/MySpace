from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_warden = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    student_first_name = models.CharField(max_length=200, null=True)
    student_last_name = models.CharField(max_length=200, null=True)
    father_name = models.CharField(max_length=200, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    smart_card_id = models.CharField(max_length=10, unique=True, primary_key=True)
    email = models.EmailField(max_length=70, unique=True)
    phone_no = PhoneNumberField(null=True, blank=False, unique=True)
    #address = models.CharField(max_length = 100,null =True)
    #city = models.CharField(max_length = 100,null =True)
    #state = models.CharField(max_length = 100,null =True)
    #pincode = models.IntegerField(default=382009)
    course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room_allotted = models.BooleanField(default=False)
    no_dues = models.BooleanField(default=True)

    def __str__(self):
        return self.smart_card_id

class Hostel(models.Model):
    hostel_id = models.CharField(max_length=20, primary_key=True, unique=True)
    hostel_name = models.CharField(max_length=20)
    course = models.ManyToManyField('Course', default=None, blank=True)
    warden_assigned = models.CharField(max_length=100, blank=True)
    total_no_floors = models.IntegerField()
    total_no_rooms = models.IntegerField()
    vacant_beds = models.IntegerField()

    def __str__(self):
        return self.hostel_id

class Room(models.Model):
    room_choice = [('SGL', 'Single Occupancy'), ('DLB', 'Double Occupancy'), ('TLB', 'Triple Occupancy')]
    room_no = models.CharField(max_length=5)
    room_name = models.CharField(max_length=10)
    room_type = models.CharField(choices=room_choice, max_length=3, default='TLB')
    vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

    def __str__(self):
        return self.room_no

#?????????????????????????????????
class Course(models.Model):
    # if a student has smart card id BTBTC18267, then BTBTC is the course code
    code = models.CharField(max_length=100, default=None)
    year = models.CharField(max_length=10)
    room_choice = [('SGL', 'Single Occupancy'), ('DLB', 'Double Occupancy'), ('TLB', 'Triple Occupancy')]
    room_type = models.CharField(choices=room_choice, max_length=3, default='TLB')

    def __str__(self):
        return self.code