from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from .forms import create_user
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
    if request.method=='POST':
        fm = create_user(request.POST)
        if fm.is_valid():
            fm.save()
            print('success')
            return redirect('login')
        else:
            return redirect('register')
    else:
        fm=create_user()
        return render(request, 'users/register.html',{'fm':fm})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password= request.POST.get('password')
            user= authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('dashboard')
            else:
                return redirect('login')
    return render(request, 'users/login.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')