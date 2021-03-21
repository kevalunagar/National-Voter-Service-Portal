import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from .models import ApplicationData
from datetime import date 
  # Create your views here.

# def calculateAge(birthDate): 
#     today = date.today()
#     birthDate=d 
#     age = today.year - birthDate - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
#     return age 

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
        messages.info(request,'Please Login first then apply for new application')
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