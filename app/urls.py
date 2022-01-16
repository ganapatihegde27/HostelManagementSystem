from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('hostels/', views.hostels, name='hostels'),
    path('hostel/<int:hostel_id>/', views.hostel_id),

    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:room_id>/', views.room_id),

    path('students/', views.students, name='students'),
    path('student/<int:student_id>/', views.student_id),

    path('about/', views.about_us, name='home_page'),

]