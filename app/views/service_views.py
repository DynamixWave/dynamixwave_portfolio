from django.shortcuts import redirect,render,get_object_or_404
from ..models import *

def ServiceList(request):
    ourservicelists = OurServiceListModel.objects.all()
    
    context = {
        'ourservicelists':ourservicelists,
    }
    return render(request, 'service.html', context)

def ServiceDetil(request):
    return render(request, 'service_detail.html')