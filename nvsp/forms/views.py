from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Form

# Create your views here.
def download(request):
    forms = Form.objects.all()
    if request.user.is_authenticated: 
            return render(request, 'form.html', {'forms' : forms})
    messages.info(request,'Please Login first then apply for download from')
    return redirect('/login')