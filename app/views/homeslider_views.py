from django.shortcuts import render,redirect
from ..models import *

def HomeSliderList(request):
    homeslider = HomeSliderModel.objects.all()
    context = {"homeslider":homeslider}
    
    return render(request, 'index.html', context)