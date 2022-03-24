# from curses import def_shell_mode
from pydoc import describe
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
    ba = batch.objects.all()
    return render(request,'Admin_Academic_Class.html',{'ba':ba})

def Admin_AddClass(request):
    ba = batch.objects.all()
    return render(request,'Admin_AddClass.html',{'ba':ba})

def Admin_Academic_Subject(request):
    return render(request,'Admin_Academic_Subject.html')

def Admin_AddSubject(request):
    ba = batch.objects.all()
    return render(request,'Admin_AddSubject.html',{'ba':ba})

def Admin_AddSubject_save(request):
    if request.method == 'POST':
        sub = request.POST['subject']
        type = request.POST['haful']
        rate = request.POST['rate']
        ba = request.POST['batch']
        a=add_subject(subject_name=sub,subject_status=type,batch_name_id=ba,Rate=rate)
        a.save()
        m="Subject added Successfully"
    return render(request,'Admin_AddSubject.html',{'m':m})


def Admin_UpdateSubject(request,id):
    ba = batch.objects.all()
    return render(request,'Admin_UpdateSubject.html',{'ba':ba})

def Admin_UpdateSubject_save(request,id):
    if request.method == 'POST':
        abc = add_subject.objects.get(id=id)
        abc.subject_name= request.POST.get('subject')
        abc.subject_status = request.POST.get('haful')
        abc.Rate = request.POST.get('rate')
        abc.batch_name_id = request.POST.get('batch')
        abc.save()
        m="Subject updated Successfully"
    return render(request,'Admin_UpdateSubject.html',{'m':m})

def Admin_ViewSubject(request):
    var =add_subject.objects.all()
    batch_name_id = request.GET.get('batch_name_id ')
    ba=batch.objects.filter(batch_name=batch_name_id)
    return render(request,'Admin_ViewSubject.html',{'var':var,'ba':ba})

def Admin_deletesubject(request,id):
    m = add_subject.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewSubject')

def Admin_Attendance_Card(request):
    return render(request,'Admin_Attendance_Card.html')

def Admin_Attendance(request):
    b1=batch.objects.all()
    u1=user_registration.objects.all()
    return render(request,'Admin_Attendance.html',{'b1':b1,'u1':u1})

def Admin_Attendance_Show(request):
    if request.method == "POST":
        empname1=request.POST.get('name')
        # usr =user_registration.objects.filter(fullname=empname1)
        atten=attendance.objects.filter(user_id=empname1)
    return render(request,'Admin_AttendanceShow.html',{'atten':atten,'empname1':empname1})

def Admin_Reportedissues_Card(request):
    Desig = designation.objects.all()
    return render(request,'Admin_Reportedissues_Card.html',{'designation':Desig})

def Admin_Reportedissues(request,id):
    reported_issues=reported_issue.objects.get(id=id)
    user=user_registration.objects.all()
    return render(request,'Admin_Reportedissues.html',{'reported_issue':reported_issues,'user':user})
   
    # return render(request,'Admin_Reportedissues.html')

def Admin_Reportedissues_Show(request,id):
    reported_issues=reported_issue.objects.all()
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations).order_by("-id")
    return render(request,'Admin_Reportedissues_Show.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def Admin_LeaveRequest(request):
    return render(request,'Admin_LeaveRequest.html')

def Admin_Leave(request):
    return render(request,'Admin_l.html')

def Admin_ViewClass(request):
    var =class_registration.objects.all()
    batch_name_id = request.GET.get('batch_name_id ')
    ba=batch.objects.filter(batch_name=batch_name_id)
    return render(request,'Admin_ViewClass.html',{'var':var,'ba':ba})

def Admin_add_classsave(request):
    if request.method == 'POST':
        newclass = request.POST['class']
        desc = request.POST['discrip']
        ba = request.POST['batch']
        a=class_registration(class_name=newclass,description=desc,batch_name_id=ba)
        a.save()
        m="Class added Successfully"
    return render(request,'Admin_AddClass.html',{'m':m})

def Admin_deleteclass(request,id):
    m = class_registration.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewClass')


def Admin_UpdateClass(request,id):
    ba = batch.objects.all()
    return render(request,'Admin_UpdateClass.html',{'ba':ba})


def Admin_Update_Classsave(request,id):
    if request.method == 'POST':
        abc = class_registration.objects.get(id=id)
        abc.class_name= request.POST.get('class')
        abc.description = request.POST.get('discrip')
        abc.batch_name_id = request.POST.get('batch')
        abc.save()
        m="Class updated Successfully"
    return render(request,'Admin_UpdateClass.html',{'m':m})

def Admin_At_Designation(request): 
    dept_id = request.GET.get('dept_id') 
    Desig = designation.objects.filter(batch_name_id=dept_id)
    # Desig = designation.objects.all()
    print(Desig)
    return render(request, 'Admin_At_Designation.html', {'Desig': Desig})
    

def Admin_At_Name(request):    
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(batch_id=dept_id)
    print(emp)
    return render(request, 'Admin_At_Name.html', {'emp': emp})


