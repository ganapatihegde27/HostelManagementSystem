from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('hostels/', views.hostels, name='hostels'),
    path('hostel/<int:hostel_id>/', views.hostel_id),
    path('hostel/booking/', views.hostel_booking),
    path('hostel/<int:hostel_id>/remove', views.remove_hostel),

    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:room_id>/', views.room_id),
    path('room/booking/', views.room_booking),
    path('room/<int:room_id>/remove', views.remove_room),

    path('students/', views.students, name='students'),
    path('student/<int:student_id>/', views.student_id),
    path('student/booking/', views.student_registration),
    path('student/<int:student_id>/remove', views.remove_student),

    path('populate/', views.populate, name='populate'),
    path('about/', views.about_us, name='home_page'),

]