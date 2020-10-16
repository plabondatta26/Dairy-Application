from django.contrib import admin
from django.urls import path, include
import dairy, users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dairy.urls')),
    path('user/',include('users.urls')),
]
