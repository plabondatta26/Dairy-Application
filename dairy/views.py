from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Dairy
from .forms import CreateNew
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'dairy/home.html')


@login_required(login_url='login')
def dashboard(request):
   if request.user.is_authenticated:
       dairy=Dairy.objects.filter(user= request.user).order_by('-created_on')
       if dairy is not None:
           return render(request, 'dairy/dashboard.html', {'dairy': dairy})
       else:
           return render(request, 'dairy/dashboard.html')

@login_required(login_url='login')
def Add_new(request):
    user_id= User.objects.get(id= request.user.id)
    if request.method=='POST':
        fm = CreateNew(request.POST)
        if fm.is_valid():
            fm_obj = fm.save(commit=False)
            fm_obj.user=user_id
            fm_obj.save()
            return redirect('dashboard')
        else:
            redirect('add')
    fm = CreateNew()
    return render(request, 'dairy/add.html', {'fm':fm})

"""
user_id = request.user.id
        user = get_object_or_404(User, pk=user_id)
        fm = CreateNew(request.POST, instance=user)
        if fm.is_valid():
            print('before save')
            fm.save()
            print('after save')
            return redirect('dashboard')
        else:
            return redirect('add')
    fm = CreateNew()
    return render(request, 'dairy/add.html', {'fm': fm})

"""
"""
def Add_new(request):

    if request.method =='POST':
        user = User(request.user.id)
        print(user,'user id')
        fm = CreateNew(request.POST, instance=request.user)
        print(request.user.id)
        if fm.is_valid():
            print('before save')
            fm.save(commit=True)
            print('after save')
            return redirect('dashboard')
        else:
            return redirect('add')
    fm= CreateNew()
    return render(request, 'dairy/add.html', {'fm':fm})

"""

@login_required(login_url='login')
def Details(request,id):
    if request.user.is_authenticated:
        dairy= Dairy.objects.get(pk=id)
        return render(request, 'dairy/details.html', {'dairy': dairy})
    else:
        return redirect('login')

@login_required(login_url='login')
def Edit(request, id):
    dairy = Dairy.objects.get(pk=id)
    if request.method=='POST':
        fm= CreateNew(request.POST, instance=dairy)
        if fm.is_valid():
            fm.save()
            return redirect('dashboard')
    fm = CreateNew()
    return render(request, 'dairy/edit.html', {'fm':fm, 'dairy':dairy})
@login_required(login_url='login')
def Delete(request,id):
    print(id, 'id')
    dairy = Dairy.objects.get(pk=id)
    print(dairy)
    dairy.delete()
    return HttpResponseRedirect('/dashboard/')