from django.contrib import admin
from django.urls import path
from users import views as us
from dairy import views as dairy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', us.registration, name ='register'),
    path('login/', us.login_page, name ='login'),
    path('logout/', us.logout_page, name ='logout'),

    path('', dairy.index, name ='home'),
    path('dashboard/', dairy.dashboard, name ='dashboard'),
    path('add/', dairy.Add_new, name ='add'),
    path('details/<int:id>/', dairy.Details, name ='details'),
    path('edit/<int:id>/', dairy.Edit, name ='edit'),
    path('delete/<int:id>/', dairy.Delete, name ='delete'),
]
