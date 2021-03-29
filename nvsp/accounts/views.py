from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.


def register(request) :
    if request.method == 'POST' :
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confPassword=request.POST['confPassword']
        
        if password != confPassword :
            messages.info(request,'Password and Confirm Password Is not same... :(')
            return redirect('register')
    
        elif User.objects.filter(username=username).exists() :
            messages.info(request,'User name is already teken... :(')
            return redirect('register')
    
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email id is already register... :(')
            return redirect('register')
    
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username Or Password is wrong...  :( ')
                return redirect('login')
    else:
        return render(request,'register.html')



def login(request) :
    if request.method =='POST' :
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is wrong...  :( ')
            return redirect('login')
    else:
        return render(request,'login.html')


def home(request) :
    return render(request,'home.html')

def logout(request) :
    auth.logout(request)
    return redirect('home')


def profile(request) :
    if request.user.is_authenticated: 
        return render(request,'profile.html')
    messages.info(request,'Please Login for check your profile')
    return redirect('login')