from django import forms

from app.models import Room_allotment

class HostelForm(forms.Form):
    hostel_id = forms.IntegerField()
    hostel_name = forms.CharField()
    admin_id = forms.IntegerField()
    admin_name = forms.CharField()
    phone_no = forms.IntegerField()
    vacancy = forms.IntegerField()
    no_of_rooms = forms.IntegerField()
    no_of_students = forms.IntegerField()


class RoomForm(forms.Form):
    room_id = forms.IntegerField()
    room_name = forms.CharField()
    vacancy = forms.IntegerField()
    room_occupancy = forms.IntegerField()
    room_status = forms.IntegerField()
    hostel_id = forms.IntegerField()

class StudentForm(forms.Form):
    student_id = forms.IntegerField()
    student_name = forms.CharField()
    phone_no = forms.IntegerField()
    dept = forms.CharField()
    years_of_study = forms.IntegerField()
    room_allotment_id = forms.IntegerField()
    joining_date = forms.DateField()
    vacating_date = forms.DateField()
    room_id = forms.IntegerField()
