from django.urls import path, include
from . import views
from accounts.views import login

urlpatterns = [
    #path('login',login,name='login'),
    path('',views.application,name='application'),
    path('upload',views.upload,name='upload'),
    path('preview', views.preview, name='preview'),
    #path('saveApplication',views.saveApplication,name='saveApplication'),
]