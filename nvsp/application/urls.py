from django.urls import path, include
from . import views
from accounts.views import login

urlpatterns = [
    #path('login',login,name='login'),
    path('',views.application,name='application'),
    path('upload',views.upload,name='upload'),
    path('preview', views.preview, name='preview'),
    path('modification', views.modification, name='modification'),
    path('status', views.status, name='status'),
    path('eEpic', views.eEpic, name='eEpic'),
    #path('saveApplication',views.saveApplication,name='saveApplication'),
]