from django.db import models

# Create your models here.
class Hostel(models.Model):
    hostel_id = models.IntegerField(primary_key=True)
    hostel_name = models.CharField(max_length=100)
    vacancy = models.IntegerField(default=0)
    no_of_rooms = models.IntegerField(default=0)
    no_of_students = models.IntegerField(default=0)
    def __str__(self):
        return self.hostel_name

class Hostel_admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=100)
    vacancy = models.IntegerField(default=0)
    ROOM_OCCUPANCY = ((1,"Single"), (2,"Double"), (3,"Triple"))
    room_occupancy = models.IntegerField(choices=ROOM_OCCUPANCY)
    ROOM_STATUS = (('OCCUPIED', 1), ('VACANT', 0))
    room_status = models.CharField(max_length=100, choices=ROOM_STATUS)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)
    def __str__(self):
        return self.room_name

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    dept = models.CharField(max_length=100)
    years_of_study = models.IntegerField(default=1)
    def __str__(self):
        return self.student_name

class Room_allotment(models.Model):
    id = models.IntegerField(primary_key=True)
    joining_date = models.DateField()
    vacating_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
