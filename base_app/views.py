# from curses import def_shell_mode
from audioop import reverse
from pydoc import describe
from urllib.parse import urlencode
from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def Admin_index(request):
#     if 'SAdm_id' in request.session:
#         if request.session.has_key('SAdm_id'):
#             SAdm_id = request.session['SAdm_id']
#         else:
#             variable="dummy"
#         mem = user_registration.objects.filter(id=SAdm_id)
#         return render(request,'Admin_index.html',{'mem':mem})
#     else:
#         return redirect('/') 


def login(request):
    manag = designation.objects.get(designation="manager")
    if request.method == 'POST':       
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=manag.id).exists():           
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['m_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.batch_id
            request.session['m_id'] = member.id 
            mem=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            return render(request,'MAN_index.html',{'mem':mem,'num':Num})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')


def Admin_index(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    return render(request,'Admin_index.html')

#-------Academic---------
def Admin_Academic(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    return render(request,'Admin_Academic.html')

def Admin_Academic_Class(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    ba = batch.objects.all()
    return render(request,'Admin_Academic_Class.html',{'ba':ba})

def Admin_AddClass(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    ba = batch.objects.all()
    return render(request,'Admin_AddClass.html',{'ba':ba})


def Admin_ViewClass(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    var =class_registration.objects.all()
    batch_name_id = request.GET.get('batch_name_id ')
    ba=batch.objects.filter(batch_name=batch_name_id)
    return render(request,'Admin_ViewClass.html',{'var':var,'ba':ba})

def Admin_add_classsave(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == 'POST':
        newclass = request.POST['class']
        desc = request.POST['discrip']
        ba = request.POST['batch']
        a=class_registration(class_name=newclass,description=desc,batch_name_id=ba)
        a.save()
        m="Class added Successfully"
    return render(request,'Admin_AddClass.html',{'m':m})

def Admin_deleteclass(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    m = class_registration.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewClass')


def Admin_UpdateClass(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    var= class_registration.objects.filter(id=id)
    vars=class_registration.objects.get(id=id)
    ba = batch.objects.all()
    return render(request,'Admin_UpdateClass.html',{'ba':ba,'var':var,'vars':vars})


def Admin_Update_Classsave(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == 'POST':
        var = class_registration.objects.get(id=id)
        var.class_name= request.POST.get('class')
        var.description = request.POST.get('discrip')
        var.batch_name_id = request.POST.get('batch')
        var.save()
        m="Class updated Successfully"
    return render(request,'Admin_UpdateClass.html',{'m':m})

def Admin_Academic_Subject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    return render(request,'Admin_Academic_Subject.html')

def Admin_AddSubject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    ba = batch.objects.all()
    return render(request,'Admin_AddSubject.html',{'ba':ba})

def Admin_AddSubject_save(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == 'POST':
        sub = request.POST['subject']       
        rate = request.POST['rate']
        ba = request.POST['batch']
        a=add_subject(subject_name=sub,batch_name_id=ba,Rate=rate)
        a.save()
        m="Subject added Successfully"
    return render(request,'Admin_AddSubject.html',{'m':m})


def Admin_UpdateSubject(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    var= add_subject.objects.filter(id=id)
    vars=add_subject.objects.get(id=id)
    ba = batch.objects.all()
    return render(request,'Admin_UpdateSubject.html',{'ba':ba,'vars':vars,'var':var})

def Admin_UpdateSubject_save(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == 'POST':
        abc = add_subject.objects.get(id=id)
        abc.subject_name= request.POST.get('subject')
        abc.Rate = request.POST.get('rate')
        abc.batch_name_id = request.POST.get('batch')
        abc.save()
        m="Subject updated Successfully"
    return render(request,'Admin_UpdateSubject.html',{'m':m})

def Admin_ViewSubject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    var =add_subject.objects.all()
    batch_name_id = request.GET.get('batch_name_id ')
    ba=batch.objects.filter(batch_name=batch_name_id)
    return render(request,'Admin_ViewSubject.html',{'var':var,'ba':ba})

def Admin_deletesubject(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    m = add_subject.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewSubject')

#------Attendance--------

def Admin_Attendance(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    b1=batch.objects.all()
    u1=user_registration.objects.all()
    return render(request,'Admin_Attendance.html',{'b1':b1,'u1':u1})

def Admin_Attendance_Show(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == "POST":
        empname1=request.POST.get('empname')      
        atten=attendance.objects.filter(user_id=empname1).order_by("-id")
    return render(request,'Admin_AttendanceShow.html',{'atten':atten,'empname':empname1})


def Admin_At_Designation(request): 
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    dept_id = request.GET.get('dept_id') 
    Desig = designation.objects.filter(batch_name_id=dept_id)
    # Desig = designation.objects.all()
    print(Desig)
    return render(request, 'Admin_At_Designation.html', {'Desig': Desig})
    
def Admin_At_Name(request):   
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy" 
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(batch_id=dept_id)
    print(emp)
    return render(request, 'Admin_At_Name.html', {'emp': emp})

#----------Reported issue------

def Admin_Reportedissues_Card(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    Desig = designation.objects.all()
    return render(request,'Admin_Reportedissues_Card.html',{'designation':Desig})

def Admin_Reportedissues(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    reported_issues=reported_issue.objects.get(id=id)
    user_reg=user_registration.objects.all()
    return render(request,'Admin_Reportedissues.html',{'reported_issue':reported_issues,'user':user_reg})
   

def Admin_Reportedissues_Show(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    reported_issues=reported_issue.objects.all()
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations).order_by("-id")
    return render(request,'Admin_Reportedissues_Show.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def Admin_ManagerReportedissue(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    reported_issues=reported_issue.objects.all()
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations).order_by("-id")
    return render(request,'Admin_ManagerReportedissue.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

#---------Leave-------



def Admin_ManagerLeaveRequest(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    Man = designation.objects.get(designation='manager')
    var = Leave.objects.filter(designation_id=Man.id).all().order_by("-id")
    return render(request,'Admin_ManagerLeaveRequest.html',{'var':var})

def Admin_rejectedManager_leave(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"
    if request.method == 'POST':
        staff_reason=request.POST.get('reply')
        pro_sts = Leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,leaveapprovedstatus ='Rejected')      
    return redirect('Admin_ManagerLeaveRequest')

def Admin_acceptedManager_leave(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"    
    al = Leave.objects.filter(id=id).update(leaveapprovedstatus ='Approved')     
    return redirect('Admin_ManagerLeaveRequest')

#------------------MANAGER--------------

# def MAN_index(request):
#     if request.session.has_key('m_id'):
#         m_id = request.session['m_id']
#     else:
#         variable="dummy"   
#     return render(request,'MAN_index.html')


def MAN_index(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']        
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_index.html',{'mem':mem})

def MAN_Academic(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        mem = user_registration.objects.filter(id=m_id)
        ba = batch.objects.all()
        var = class_registration.objects.all()
        return render(request,'MAN_Academic.html',{'ba':ba,'var':var,'mem':mem})
    else:
        return redirect('/') 


def MAN_UpdateClass(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        mem = user_registration.objects.filter(id=m_id) 
        var= class_registration.objects.filter(id=id)
        vars=class_registration.objects.get(id=id)
        ba = batch.objects.all()
        return render(request,'MAN_UpdateClass.html',{'ba':ba,'var':var,'vars':vars,'mem':mem})
    else:
        return redirect('/') 


def MAN_Update_Classsave(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        mem = user_registration.objects.filter(id=m_id)  
        if request.method == 'POST':
            var = class_registration.objects.get(id=id)
            var.class_name= request.POST.get('class')
            var.description = request.POST.get('discrip')
            var.batch_name_id = request.POST.get('batch')
            var.save()
            # m="Class updated Successfully"
        return render(request,'MAN_UpdateClass.html',{'mem':mem})
    else:
        return redirect('/') 



def MAN_deleteclass(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        mem = user_registration.objects.filter(id=m_id)  
        m = class_registration.objects.get(id=id)
        m.delete()
        return redirect('MAN_ViewClass',{'mem':mem})
    else:
        return redirect('/') 


def MAN_ViewClass(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        mem = user_registration.objects.filter(id=m_id)  
        var =class_registration.objects.all()
        batch_name_id = request.GET.get('batch_name_id ')
        ba=batch.objects.filter(batch_name=batch_name_id)
        return render(request,'MAN_ViewClass.html',{'var':var,'ba':ba,'mem':mem})
    else:
        return redirect('/') 

