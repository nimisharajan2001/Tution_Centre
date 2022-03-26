from . import views
from django.urls import re_path


urlpatterns=[  
     
      # re_path(r'^$', views.login, name='login'),

      re_path(r'^Admin_index/$', views.Admin_index,
            name='Admin_index'),
      #-------Academic------
      re_path(r'^Admin_Academic/$', views.Admin_Academic,
            name='Admin_Academic'),
      re_path(r'^Admin_Academic_Class/$', views.Admin_Academic_Class,
                  name='Admin_Academic_Class'),
      re_path(r'^Admin_AddClass/$', views.Admin_AddClass,
                  name='Admin_AddClass'),
      re_path(r'^Admin_ViewClass/$', views.Admin_ViewClass,
                  name='Admin_ViewClass'),
      re_path(r'^Admin_add_classsave/$', views.Admin_add_classsave,
                  name='Admin_add_classsave'),
      re_path(r'^Admin_deleteclass/(?P<id>\d+)/$', views.Admin_deleteclass,
                  name='Admin_deleteclass'),
      re_path(r'^Admin_UpdateClass/(?P<id>\d+)/$', views.Admin_UpdateClass,
                  name='Admin_UpdateClass'),
      re_path(r'^Admin_Update_Classsave/(?P<id>\d+)/$', views.Admin_Update_Classsave,
                  name='Admin_Update_Classsave'),
      re_path(r'^Admin_Academic_Subject/$', views.Admin_Academic_Subject,
                  name='Admin_Academic_Subject'),
      re_path(r'^Admin_AddSubject/$', views.Admin_AddSubject,
                  name='Admin_AddSubject'),
      re_path(r'^Admin_AddSubject_save/$', views.Admin_AddSubject_save,
                  name='Admin_AddSubject_save'),
      re_path(r'^Admin_ViewSubject/$', views.Admin_ViewSubject,
                  name='Admin_ViewSubject'),
      re_path(r'^Admin_UpdateSubject/(?P<id>\d+)/$', views.Admin_UpdateSubject,
                  name='Admin_UpdateSubject'),
      re_path(r'^Admin_UpdateSubject_save/(?P<id>\d+)/$', views.Admin_UpdateSubject_save,
                  name='Admin_UpdateSubject_save'),
      re_path(r'^Admin_deletesubject/(?P<id>\d+)/$', views.Admin_deletesubject,
                  name='Admin_deletesubject'),
      
      #-----Attendance-------

      re_path(r'^Admin_Attendance/$', views.Admin_Attendance,
                  name='Admin_Attendance'),
      re_path(r'^Admin_Attendance_Show/$', views.Admin_Attendance_Show,
                  name='Admin_Attendance_Show'),
      re_path(r'^Admin_At_Designation/$', views.Admin_At_Designation,
                  name='Admin_At_Designation'),
      re_path(r'^Admin_At_Name/$', views.Admin_At_Name,
                  name='Admin_At_Name'),

      #---------Reported issues-------
      re_path(r'^Admin_Reportedissues_Card/$', views.Admin_Reportedissues_Card,
                  name='Admin_Reportedissues_Card'),
      re_path(r'^Admin_Reportedissues/(?P<id>\d+)/$', views.Admin_Reportedissues,
                  name='Admin_Reportedissues'),
      re_path(r'^Admin_Reportedissues_Show/(?P<id>\d+)/$', views.Admin_Reportedissues_Show,
                  name='Admin_Reportedissues_Show'),

      #--------Leave--------

      re_path(r'^Admin_LeaveRequest/$', views.Admin_LeaveRequest,
                  name='Admin_LeaveRequest'),
        
      #-----------MANAGER------------

      re_path(r'^MAN_index/$', views.MAN_index,
            name='MAN_index'),
      re_path(r'^MAN_Academic/$', views.MAN_Academic,
            name='MAN_Academic'),
      re_path(r'^MAN_ViewClass/$', views.MAN_ViewClass,
            name='MAN_ViewClass'),
      re_path(r'^MAN_UpdateClass/(?P<id>\d+)/$', views.MAN_UpdateClass,
            name='MAN_UpdateClass'),
      re_path(r'^MAN_Update_Classsave/(?P<id>\d+)/$', views.MAN_Update_Classsave,
            name='MAN_Update_Classsave'),
      re_path(r'^MAN_deleteclass/(?P<id>\d+)/$', views.MAN_deleteclass,
            name='MAN_deleteclass'),
]