from django.shortcuts import render
from .forms import Add_Dairy
from .models import Dairy
# Create your views here.
def index(request):

    return render(request, 'dairy/index.html')

def dashboard(request):
    dairy = Dairy.objects.all()
    return render(request, 'dairy/dashboard.html', {'dairy':dairy})
def add(requst):
    if requst.method == 'POST':
        ad = Add_Dairy(requst.POST)
        if ad.is_valid():
            title=ad.cleaned_data['title']
            description=ad.cleaned_data['description']
            ad.save()
            return render(requst, 'dairy/add.html', {'form':ad})
    ad=Add_Dairy()
    return render(requst, 'dairy/add.html', {'form': ad})
