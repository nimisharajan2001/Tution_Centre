from . import views
from django.urls import re_path

urlpatterns=[  
     
      re_path(r'^Admin_index/$', views.Admin_index,
            name='Admin_index'),
      re_path(r'^Admin_Academic/$', views.Admin_Academic,
            name='Admin_Academic'),
      re_path(r'^Admin_Academic_Class/$', views.Admin_Academic_Class,
                  name='Admin_Academic_Class'),
      re_path(r'^Admin_AddClass/$', views.Admin_AddClass,
                  name='Admin_AddClass'),
      re_path(r'^Admin_Academic_Subject/$', views.Admin_Academic_Subject,
                  name='Admin_Academic_Subject'),
      re_path(r'^Admin_AddSubject/$', views.Admin_AddSubject,
                  name='Admin_AddSubject'),
      re_path(r'^Admin_Attendance_Card/$', views.Admin_Attendance_Card,
                  name='Admin_Attendance_Card'),
      re_path(r'^Admin_Attendance/$', views.Admin_Attendance,
                  name='Admin_Attendance'),
      re_path(r'^Admin_Attendance_Show/$', views.Admin_Attendance_Show,
                  name='Admin_Attendance_Show'),
      re_path(r'^Admin_Reportedissues_Card/$', views.Admin_Reportedissues_Card,
                  name='Admin_Reportedissues_Card'),
      re_path(r'^Admin_Reportedissues/$', views.Admin_Reportedissues,
                  name='Admin_Reportedissues'),
      re_path(r'^Admin_Reportedissues_Show/$', views.Admin_Reportedissues_Show,
                  name='Admin_Reportedissues_Show'),
      re_path(r'^Admin_LeaveRequest/$', views.Admin_LeaveRequest,
                  name='Admin_LeaveRequest'),
      re_path(r'^Admin_Leave/$', views.Admin_Leave,
                  name='Admin_Leave'),
]