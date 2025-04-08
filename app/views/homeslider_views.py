from django.shortcuts import render,redirect
from ..models import *

def HomeSliderList(request):
    homesliders = HomeSliderModel.objects.all()
    ourservices = OurServiceModel.objects.all()
    ourservicelists = OurServiceListModel.objects.all()
    
    context = {
        "homeslider":homesliders,
        "ourservice":ourservices,
        "ourservicelist":ourservicelists,
        }
    
    return render(request, 'index.html', context)

