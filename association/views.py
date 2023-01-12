from django.shortcuts import render
from .models import Destination

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    
    return render(request,'index.html', {'dests':dests})