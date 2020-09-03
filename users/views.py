from django.shortcuts import render,redirect
from .forms import create_user
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method=='POST':
        reg = create_user(request.POST)
        if reg.is_valid():
            username= reg.cleaned_data['username']
            reg.save()
            return redirect('login')
        else:
            messages.error(request, "Fill the form correctly")
            return redirect('register')
    else:
        reg=create_user()
        return render(request, 'users/register.html',{'reg':reg} )

def Login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Log in success")
                    return redirect('dashboard')
            else:
                messages.error(request, "Username or Password is wrong")
                return redirect('login')
        return render(request, 'users/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')