from django.contrib import admin
from django.urls import path, include
from dairy import views as dairy
from users import views as user
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dairy.index, name='home'),
    path('dashboard/', dairy.dashboard, name='dashboard'),
    path('add/', dairy.Add_new, name='add'),
    path('details/<int:id>/', dairy.Details, name='details'),
    path('edit/<int:id>/', dairy.Edit, name='edit'),
    path('delete/<int:id>/', dairy.Delete, name='delete'),
    path('pdf/<int:id>/', dairy.pdfGenerator, name='pdf'),
    path('make/<int:id>/', dairy.pdfView, name='pdfView'),

    path('register/', user.registration, name ='register'),
    path('login/', user.login_page, name='login'),
    path('logout/', user.logout_page, name='logout'),
]
