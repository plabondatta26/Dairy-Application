from django.shortcuts import render,HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .forms import Add_Dairy
from .models import Dairy
# Create your views here.


def index(request):

    return render(request, 'dairy/index.html')
@login_required(login_url='login')
def dashboard(request):
    dairy = Dairy.objects.all()

    return render(request, 'dairy/dashboard.html', {'dairy':dairy})
@login_required(login_url='login')
def add(requst):
    if requst.method == 'POST':
        ad = Add_Dairy(requst.POST)
        if ad.is_valid():
            title=ad.cleaned_data['title']
            description=ad.cleaned_data['description']
            ad.save()
            return HttpResponseRedirect('/dairy/dashboard/')
    ad=Add_Dairy()
    return render(requst, 'dairy/add.html', {'form': ad})

@login_required(login_url='login')
def delete(request,id):
        dairy = Dairy.objects.get(pk=id)
        dairy.delete()
        return HttpResponseRedirect('/dairy/dashboard/')

@login_required(login_url='login')
def edit(request,id):
    if request.method== 'POST':
        dairy = Dairy.objects.get(pk=id)
        form= Add_Dairy(request.POST, instance=dairy)

        form.save()
        return HttpResponseRedirect('/dairy/dashboard/')
    else:
        dairy = Dairy.objects.get(pk=id)
        form=Add_Dairy(instance=dairy)
    return render(request, 'dairy/Update.html', {'form':form})