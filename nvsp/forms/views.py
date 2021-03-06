from django.shortcuts import render
from .models import Form

# Create your views here.
def download(request):
    forms = Form.objects.all()
    return render(request, 'form.html', {'forms' : forms})
