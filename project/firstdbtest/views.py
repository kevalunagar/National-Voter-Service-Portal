from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from firstdbtest.models import Student
# Create your views here.


def getstudentinfo(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'addstudentinfo.html', c)


def addstudentinfo(request):
    sname = request.POST.get('studentname', '')
    sdate = request.POST.get('birthdate', '')
    s = Student(student_name=sname, student_dob=sdate)
    s.save()
    return HttpResponseRedirect('/firstdb/addsuccess/')


def addsuccess(request):
    return render(request, 'addrecord.html')


def delstudentinfo(request):
    sname = request.POST.get('studentname', '')
    student = Student.objects.filter(student_name=sname)
    for s in student:
        s.delete()
    return render(request, 'delrecord.html')


def StudentListView(request):
    student_list = Student.objects.all()
    return render(request, "student_list.html", {'student_list': student_list})
