from django.contrib import admin
from django.urls import path
from dairy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dairy/',views.index, name='home'),
    path('dairy/add/',views.add, name='add_new'),
    path('dairy/dashboard/',views.dashboard, name='dashboard'),
]
