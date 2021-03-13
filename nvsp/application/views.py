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

def application(request):
    today = date.today()
    if request.method=='POST':
        name = request.POST['name']
        surname = request.POST['surname']
        gender = request.POST['gender']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        pincode = request.POST['pincode']
        dob = request.POST['dob']
        relation = request.POST['relation']
        relativeName = request.POST['relativeName']
        relativeSurname = request.POST['relativeSurname']
        email = request.POST['email']
        mobile = request.POST['phone']
        declarationPlace = request.POST['applyFrom']
        declarationDate = request.POST['applyAt']
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
       

        if  (today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))) < 18 :
            messages.info(request,'Youe age is less than 18 you can not apply for voter id card')
            return redirect('application')
    
        else:
            apply = ApplicationData(name=name , surname=surname , gender=gender , state=state , city=city , address=address , pincode=pincode , dob=dob , relation=relation , relativeName=relativeName , relativeSurname=relativeSurname , email=email , mobile=mobile , declarationDate=declarationDate , declarationPlace=declarationPlace)
            apply.save()
            return redirect('home')
    
    else:
        if request.user.is_authenticated: 
            return render(request,'application_form.html')
        messages.info(request,'Please Login first then apply for new application')
        return redirect('login')



