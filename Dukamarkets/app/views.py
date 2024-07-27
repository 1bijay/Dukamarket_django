from django.shortcuts import render
#This code is written for importing models 
from . models import *  
# Create your views here.
def Base(request):
    return render(request,'base.html')

def Home(request):
    slider=Slider.objects.all()
    banner=Banner_area.objects.all()
    context={
        'slider': slider,
        'banner': banner,
    }
    return render(request,'Main/home.html',context)