import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import ApplicationData
from datetime import date 

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf 


apply = ApplicationData()

def application(request):
    today = date.today()
    if request.method=='POST':
        apply.name = request.POST['name']
        apply.surname = request.POST['surname']
        apply.gender = request.POST['gender']
        apply.state = request.POST['state']
        apply.city = request.POST['city']
        apply.address = request.POST['address']
        apply.pincode = request.POST['pincode']
        apply.dob = request.POST['dob']
        apply.relation = request.POST['relation']
        apply.relativeName = request.POST['relativeName']
        apply.relativeSurname = request.POST['relativeSurname']
        apply.email = request.POST['email']
        apply.mobile = request.POST['phone']
        apply.declarationPlace = request.POST['applyFrom']
        apply.declarationDate = request.POST['applyAt']
        apply.dob = datetime.datetime.strptime(apply.dob, '%Y-%m-%d')

        if  (today.year - apply.dob.year - ((today.month, today.day) < (apply.dob.month, apply.dob.day))) < 18 :
            messages.info(request,'Youe age is less than 18 you can not apply for voter id card')
            return redirect('application')
    
        else:
            #apply = ApplicationData(name=name , surname=surname , gender=gender , state=state , city=city , address=address , pincode=pincode , dob=dob , relation=relation , relativeName=relativeName , relativeSurname=relativeSurname , email=email , mobile=mobile , declarationDate=declarationDate , declarationPlace=declarationPlace)
            apply.save()
            return redirect('upload')
    
    else:
        if request.user.is_authenticated: 
            return render(request,'applicationform.html')
        messages.info(request,'Please Login First Then Apply For New Application')
        return redirect('/login')


def upload(request):
    if request.method == 'POST':
        apply.photo = request.FILES['photo']
        apply.aadharCard = request.FILES['aadharCard']
        apply.declaration = request.FILES['declaration']

        #apply = ApplicationData(photo=photo, aadharCard=aadharCard, declaration=declaration)
        apply.save()
        return redirect('preview')
    else:
        return render(request, 'upload_documents.html')

def preview(request):
    date=str(apply.dob.strftime("%d%m%Y"))
    apply.application_id=(str(apply.name))+date
    apply.save()
    return render(request, 'preview.html', {'apply': apply })

def modification(request):
    
    if request.user.is_authenticated: 
        if request.method == "POST" and (request.POST['submit'] == 'Submit'):
            id = request.POST['id']
            obj = ApplicationData.objects.filter(application_id=id)
            return render(request, 'modificationform.html', {'obj': obj })
        elif request.method == "POST" and (request.POST['submit'] == 'Modify'):
            id = request.POST['id']
            ApplicationData.objects.filter(application_id=id).update(name = request.POST['name'])
            ApplicationData.objects.filter(application_id=id).update(surname = request.POST['surname'])
            ApplicationData.objects.filter(application_id=id).update(gender = request.POST['gender'])
            ApplicationData.objects.filter(application_id=id).update(state = request.POST['state'])
            ApplicationData.objects.filter(application_id=id).update(city = request.POST['city'])
            ApplicationData.objects.filter(application_id=id).update(address = request.POST['address'])
            ApplicationData.objects.filter(application_id=id).update(pincode = request.POST['pincode'])
            ApplicationData.objects.filter(application_id=id).update(relation = request.POST['relation'])
            ApplicationData.objects.filter(application_id=id).update(relativeName = request.POST['relativeName'])
            ApplicationData.objects.filter(application_id=id).update(relativeSurname = request.POST['relativeSurname'])
            ApplicationData.objects.filter(application_id=id).update(email = request.POST['email'])
            ApplicationData.objects.filter(application_id=id).update(mobile = request.POST['phone'])
            ApplicationData.objects.filter(application_id=id).update(declarationPlace = request.POST['applyFrom'])
            ApplicationData.objects.filter(application_id=id).update(dob = datetime.datetime.strptime(request.POST['dob'], '%Y-%m-%d'))
            return redirect('/')
        else:
            send = "modification"
            return render(request,'applicationid.html', {'obj': send})
        
    else:
        messages.info(request,'Please Login For Modification In Your Application')
        return redirect('/login')

def status(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            id = request.POST['id']
            if(ApplicationData.objects.filter(application_id=id).count()):
                obj = ApplicationData.objects.filter(application_id=id)
                return render(request, 'showstatus.html', {'obj': obj })
            else:
                messages.info(request,'Please enter valid Application Number.')
                send = "status"
                return render(request, 'applicationid.html', {'obj': send})
        else:
            send = "status"
            return render(request, 'applicationid.html', {'obj': send})
    else:
        messages.info(request,'Please Login For Track Your Status')
        return redirect('/login')

def eEpic(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            id = request.POST['id']
            if(ApplicationData.objects.filter(application_id=id).count()):
                data = ApplicationData.objects.filter(application_id=id)
                obj={
                    'obj' : data
                }
                pdf = render_to_pdf('eEpic.html', obj)
                return HttpResponse(pdf, content_type='application/pdf')
            else:
                messages.info(request,'Please enter valid Application Number.')
                send = "eEpic"
                return render(request, 'applicationid.html', {'obj': send})         
        else:
            send = "eEpic"
            return render(request, 'applicationid.html', {'obj': send})
    else:
        messages.info(request,'Please Login For Download E-Epic Card')
        return redirect('/login')


