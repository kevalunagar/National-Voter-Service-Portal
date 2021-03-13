from django.urls import path
from . import views
from accounts.views import login

urlpatterns = [
    path('login',login,name='login'),
    path('',views.application,name='application'),
    #path('saveApplication',views.saveApplication,name='saveApplication'),
]