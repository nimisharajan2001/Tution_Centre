from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.

def Admin_index(request):
    return render(request,'Admin_index.html')

def Admin_Academic(request):
    return render(request,'Admin_Academic.html')

def Admin_Academic_Class(request):
    return render(request,'Admin_Academic_Class.html')

def Admin_AddClass(request):
    return render(request,'Admin_AddClass.html')

def Admin_Academic_Subject(request):
    return render(request,'Admin_Academic_Subject.html')

def Admin_AddSubject(request):
    return render(request,'Admin_AddSubject.html')

def Admin_Attendance_Card(request):
    return render(request,'Admin_Attendance_Card.html')

def Admin_Attendance(request):
    return render(request,'Admin_Attendance.html')

def Admin_Attendance_Show(request):
    return render(request,'Admin_AttendanceShow.html')

def Admin_Reportedissues_Card(request):
    return render(request,'Admin_Reportedissues_Card.html')

def Admin_Reportedissues(request):
    return render(request,'Admin_Reportedissues.html')

def Admin_Reportedissues_Show(request):
    return render(request,'Admin_Reportedissues_Show.html')

def Admin_LeaveRequest(request):
    return render(request,'Admin_LeaveRequest.html')

def Admin_Leave(request):
    return render(request,'Admin_l.html')
