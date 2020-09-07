from django.contrib import admin
from django.urls import path
from dairy import views
from users import views as us
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',us.register, name='register' ),
    path('login/',us.Login_page, name='login' ),
    path('logout/',us.logout_page, name='logout' ),

    path('dairy/',views.index, name='home'),
    path('dairy/add/',views.add, name='add_new'),
    path('dairy/dashboard/',views.dashboard, name='dashboard'),
    path('dairy/delete/',views.delete, name='delete'),
    path('dairy/edit/',views.edit, name='edit'),
]
