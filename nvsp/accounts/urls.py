from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),    
    path('',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
]
