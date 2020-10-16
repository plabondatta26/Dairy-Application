from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('add/', views.Add_new, name ='add'),
    path('details/<int:id>/', views.Details, name ='details'),
    path('edit/<int:id>/', views.Edit, name ='edit'),
    path('delete/<int:id>/', views.Delete, name ='delete'),
    path('pdf/<int:id>/', views.pdfGenerator, name ='pdf'),
    path('make/<int:id>/', views.pdfView, name ='pdfView'),
]
