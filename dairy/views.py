from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Dairy
from .forms import CreateNew
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
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


def pdfView(request,id):
    data = Dairy.objects.get(pk=id)
    return render(request,'dairy/pdf.html',{'dairy':data})

def pdfGenerator(request, id):
    data= Dairy.objects.get(pk=id)
    context = {'dairy': data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dairy.pdf"'
    # find the template and render it.
    template = get_template('dairy/pdf.html')
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)#, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

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