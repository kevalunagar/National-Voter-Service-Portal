from django.shortcuts import render

# Create your views here.
def download(request):
    return render(request,'form.html')
