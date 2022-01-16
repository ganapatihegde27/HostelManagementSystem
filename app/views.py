import datetime
from django.shortcuts import render
from django.db import connection

from app.models import *

add = 1
def add_entries():
     with connection.cursor() as cursor:
        cursor.execute('INSERT INTO app_hostel VALUES (100, "CMRIT", 4, 5, 10)')
        cursor.execute('INSERT INTO app_hostel VALUES (101, "BMSCE", 3, 4, 10)')
        cursor.execute('INSERT INTO app_hostel VALUES (102, "RVCE", 3, 4, 10)')

        cursor.execute('INSERT INTO app_hostel_admin VALUES (111,"TED",4444,100)')
        cursor.execute('INSERT INTO app_hostel_admin VALUES (121,"ROSE",2542,101)')
        cursor.execute('INSERT INTO app_hostel_admin VALUES (131,"MARSHAL",4564,102)')     

        cursor.execute('INSERT INTO app_room VALUES (10,"FX101",5,2,1,100)')
        cursor.execute('INSERT INTO app_room VALUES (20,"FX102",3,3,0,100)')
        cursor.execute('INSERT INTO app_room VALUES (30,"FX103",4,1,1,100)')
        cursor.execute('INSERT INTO app_room VALUES (40,"FX104",6,2,0,100)')
        cursor.execute('INSERT INTO app_room VALUES (50,"FX105",8,1,0,100)')

        cursor.execute('INSERT INTO app_room VALUES (60,"CD106",7,3,1,101)')
        cursor.execute('INSERT INTO app_room VALUES (70,"CD107",7,3,1,101)')
        cursor.execute('INSERT INTO app_room VALUES (80,"CD108",7,3,1,101)')
        cursor.execute('INSERT INTO app_room VALUES (90,"CD109",7,3,1,101)')

        cursor.execute('INSERT INTO app_room VALUES (100,"AB110",6,2,1,102)')
        cursor.execute('INSERT INTO app_room VALUES (110,"AB111",5,3,1,102)')
        cursor.execute('INSERT INTO app_room VALUES (120,"AB112",4,1,1,102)')
        cursor.execute('INSERT INTO app_room VALUES (130,"AB113",3,2,1,102)')

        cursor.execute('INSERT INTO app_student VALUES (1,"Raj",7888,"CSE",3)')
        cursor.execute('INSERT INTO app_student VALUES (2,"Hegde",1234,"CSE",3)')
        cursor.execute('INSERT INTO app_student VALUES (3,"Tom",2545,"ECE",2)')
        cursor.execute('INSERT INTO app_student VALUES (4,"Harry",3654,"ECE",4)')
        cursor.execute('INSERT INTO app_student VALUES (5,"Jake",4567,"MECH",1)')
        cursor.execute('INSERT INTO app_student VALUES (6,"Liam",7888,"CSE",3)')
        cursor.execute('INSERT INTO app_student VALUES (7,"Oliver",1234,"CSE",3)')
        cursor.execute('INSERT INTO app_student VALUES (8,"James",2545,"ECE",2)')
        cursor.execute('INSERT INTO app_student VALUES (9,"Blaze",3654,"ECE",4)')
        cursor.execute('INSERT INTO app_student VALUES (10,"Roma",4567,"MECH",1)')

        cursor.execute('INSERT INTO app_student VALUES (11,"Kate",7888,"EEE",3)')
        cursor.execute('INSERT INTO app_student VALUES (12,"Ruth",1234,"EEE",3)')
        cursor.execute('INSERT INTO app_student VALUES (13,"Liv",2545,"EEE",2)')
        cursor.execute('INSERT INTO app_student VALUES (14,"Ave",3654,"ISE",4)')
        cursor.execute('INSERT INTO app_student VALUES (15,"Grace",4567,"ISE",1)')
        cursor.execute('INSERT INTO app_student VALUES (16,"Suee",7888,"ISE",3)')
        cursor.execute('INSERT INTO app_student VALUES (17,"Dee",1234,"ISE",3)')
        cursor.execute('INSERT INTO app_student VALUES (18,"Ram",2545,"AI",2)')
        cursor.execute('INSERT INTO app_student VALUES (19,"Bheem",3654,"AI",4)')
        cursor.execute('INSERT INTO app_student VALUES (20,"Roman",4567,"AI",1)')

        cursor.execute('INSERT INTO app_student VALUES (21,"Gold",1888,"TC",4)')
        cursor.execute('INSERT INTO app_student VALUES (22,"Gem",1734,"TC",2)')
        cursor.execute('INSERT INTO app_student VALUES (23,"Gia",2745,"TC",1)')
        cursor.execute('INSERT INTO app_student VALUES (24,"Dve",3754,"ACC",3)')
        cursor.execute('INSERT INTO app_student VALUES (25,"Luna",7567,"ACC",2)')
        cursor.execute('INSERT INTO app_student VALUES (26,"Star",4888,"ACC",2)')
        cursor.execute('INSERT INTO app_student VALUES (27,"Dave",5234,"ACC",1)')
        cursor.execute('INSERT INTO app_student VALUES (28,"Aja",6545,"BUSI",4)')
        cursor.execute('INSERT INTO app_student VALUES (29,"Tima",5654,"BUSI",3)')
        cursor.execute('INSERT INTO app_student VALUES (30,"Reema",6567,"BUSI",4)')

        cursor.execute('INSERT INTO app_room_allotment VALUES (1,DATE "2022-10-21", DATE "2022-10-21",10,1)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (2,DATE "2022-10-21", DATE "2022-10-21",10,2)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (3,DATE "2022-10-21", DATE "2022-10-21",20,3)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (4,DATE "2022-10-21", DATE "2022-10-21",20,4)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (5,DATE "2022-10-21", DATE "2022-10-21",30,5)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (6,DATE "2022-10-21", DATE "2022-10-21",30,6)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (7,DATE "2022-10-21", DATE "2022-10-21",40,7)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (8,DATE "2022-10-21", DATE "2022-10-21",40,8)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (9,DATE "2022-10-21", DATE "2022-10-21",50,9)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (10,DATE "2022-10-21", DATE "2022-10-21",50,10)')

        cursor.execute('INSERT INTO app_room_allotment VALUES (12,DATE "2022-10-21", DATE "2022-10-21",60,11)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (13,DATE "2022-10-21", DATE "2022-10-21",60,12)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (14,DATE "2022-10-21", DATE "2022-10-21",70,13)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (15,DATE "2022-10-21", DATE "2022-10-21",70,14)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (16,DATE "2022-10-21", DATE "2022-10-21",80,15)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (17,DATE "2022-10-21", DATE "2022-10-21",80,16)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (18,DATE "2022-10-21", DATE "2022-10-21",90,17)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (19,DATE "2022-10-21", DATE "2022-10-21",90,18)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (21,DATE "2022-10-21", DATE "2022-10-21",100,19)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (22,DATE "2022-10-21", DATE "2022-10-21",100,20)')

        cursor.execute('INSERT INTO app_room_allotment VALUES (23,DATE "2022-10-21", DATE "2022-10-21",110,21)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (24,DATE "2022-10-21", DATE "2022-10-21",110,22)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (25,DATE "2022-10-21", DATE "2022-10-21",120,23)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (26,DATE "2022-10-21", DATE "2022-10-21",120,24)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (27,DATE "2022-10-21", DATE "2022-10-21",130,25)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (28,DATE "2022-10-21", DATE "2022-10-21",130,26)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (29,DATE "2022-10-21", DATE "2022-10-21",90,27)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (31,DATE "2022-10-21", DATE "2022-10-21",40,28)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (32,DATE "2022-10-21", DATE "2022-10-21",30,29)')
        cursor.execute('INSERT INTO app_room_allotment VALUES (33,DATE "2022-10-21", DATE "2022-10-21",50,30)')
        
def home_page(request):
    return render(request, 'home_page.html')

def hostels(request):
    total_hostels = Hostel.objects.raw('SELECT COUNT(hostel_id) FROM app_hostel')
    hostel_list = Hostel.objects.raw('SELECT * FROM app_hostel')
    total_vacancy = Hostel.objects.raw('SELECT SUM(vacancy) FROM app_hostel')
    admin_list = Hostel_admin.objects.raw('SELECT * FROM app_hostel_admin')
    context = {
        'total_hostels': total_hostels,
        'hostel_list': hostel_list,
        'total_vacancy': total_vacancy,
        'admin_list': admin_list,
    }
    return render(request, 'hostels/hostels.html', context)

def hostel_id(request, hostel_id):
    total_rooms = Room.objects.raw('SELECT room_id, COUNT(room_id) AS count FROM app_room WHERE hostel_id = ' + str(hostel_id))[0]
    hostel = Hostel.objects.raw('SELECT * FROM app_hostel WHERE hostel_id = ' + str(hostel_id))[0]
    room_list = Room.objects.raw('SELECT * FROM app_room WHERE hostel_id = ' + str(hostel_id))
    admin = Hostel_admin.objects.raw('SELECT * FROM app_hostel_admin where hostel_id = ' + str(hostel_id))
    context = {
        'total_rooms': total_rooms,
        'hostel': hostel,
        'room_list': room_list,
        'admin': admin,
    }
    return render(request, 'hostels/hostel.html', context)


def rooms(request):
    total_rooms = Room.objects.raw('SELECT room_id, COUNT(room_id) AS count FROM app_room')[0]
    room_list = Room.objects.raw('SELECT * FROM app_room')
    context = {
        'total_rooms': total_rooms,
        'room_list': room_list,
    }
    return render(request, 'rooms/rooms.html', context)


def room_id(request, room_id):
    total_students = Room_allotment.objects.raw('SELECT id, COUNT(student_id) AS count FROM app_room_allotment WHERE room_id = ' + str(room_id))[0]
    room = Room.objects.raw('SELECT * FROM app_room WHERE room_id = ' + str(room_id))[0]
    student_list = Student.objects.raw('SELECT * FROM app_student WHERE student_id in (SELECT student_id FROM app_room_allotment WHERE room_id = ' + str(room_id) + ')')
    context = {
        'total_students': total_students,
        'room': room,
        'student_list': student_list,
    }
    return render(request, 'rooms/room.html', context)

def students(request):
    total_students = Student.objects.raw('SELECT student_id, COUNT(student_id) AS count FROM app_student')[0]
    student_list = Student.objects.raw('SELECT * FROM app_student')
    context = {
        'total_students': total_students,
        'student_list': student_list,
    }
    return render(request, 'students/students.html', context)

def student_id(request, student_id):
    student = Student.objects.raw('SELECT * FROM app_student WHERE student_id = ' + str(student_id))[0]
    room = Room.objects.raw('SELECT * FROM app_room WHERE room_id in (SELECT room_id FROM app_room_allotment WHERE student_id = ' + str(student_id) + ')')[0]
    hostel = Hostel.objects.raw('SELECT * FROM app_hostel WHERE hostel_id = ' + str(room.hostel_id))[0]
    context = {
        'room': room,
        'student': student,
        'hostel': hostel,
    }
    return render(request, 'students/student.html', context)

def about_us(request):
    global add
    if add == 1:
        add_entries()
        add = 0
    return render(request, 'about_us.html')
