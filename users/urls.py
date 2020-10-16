from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name ='register'),
    path('login/', views.login_page, name ='login'),
    path('logout/', views.logout_page, name ='logout'),
]
