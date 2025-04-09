from django.shortcuts import render,redirect,get_object_or_404
from ..models import *


def HomeSliderList(request, category_slug=None):
    homesliders = HomeSliderModel.objects.all()
    ourservices = OurServiceModel.objects.all()
    ourservicelists = OurServiceListModel.objects.all()
    ourpartners = OurPartnerModel.objects.all()
    
    categories = None
    projects = None
    
    if category_slug !=None:
        categories = get_object_or_404(ProjectCategoryModel, slug=category_slug)
        projects = ProjectModel.objects.filter(category=categories)
        project_count = projects.count()
    else:
        projects = ProjectModel.objects.all()
        project_count = projects.count()
    
    context = {
        "homeslider":homesliders,
        "ourservice":ourservices,
        "ourservicelist":ourservicelists,
        "ourpartner":ourpartners,
        "projects":projects,
        "project_count":project_count,
    }
    return render(request, 'index.html', context)





