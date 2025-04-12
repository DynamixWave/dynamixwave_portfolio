from django.shortcuts import redirect,render,get_object_or_404
from ..models import *

def ServiceList(request):
    ourservicelists = OurServiceListModel.objects.all()
    
    context = {
        'ourservicelists':ourservicelists,
    }
    return render(request, 'service.html', context)

def ServiceDetil(request, pk):
    service_category = OurServiceListCategory.objects.all()
    service = get_object_or_404(OurServiceListModel, id=pk)
    services = OurServiceListModel.objects.all()
    context = {
        'service_category':service_category,
        'service':service,
        'services':services,
        'selected_category': service.category
    }
    
    return render(request, 'service_detail.html',context)

def ServiceByCategory(request, category_id):
    service_category = OurServiceListCategory.objects.all()
    selected_category = get_object_or_404(OurServiceListCategory, id=category_id)
    services = OurServiceListModel.objects.filter(category=selected_category)


    context = {
        'service_category': service_category,
        'selected_category': selected_category,
        'services': services,
    }
    return render(request, 'service_by_category.html', context)
