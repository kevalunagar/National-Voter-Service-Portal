from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^addstudentinfo/$', views.addstudentinfo),
    url(r'^getstudentinfo/$', views.getstudentinfo),
    url(r'^addsuccess/$', views.addsuccess),
    url('students/', views.StudentListView, name='students'),
    url('delstudentinfo/',views.delstudentinfo),
]
