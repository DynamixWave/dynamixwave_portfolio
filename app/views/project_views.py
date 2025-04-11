from django.shortcuts import redirect,render,get_object_or_404
from ..models import *

def ProjectList(request, category_slug):
    projectcategories = ProjectCategoryModel.objects.all()
    
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

        "projects":projects,
        "project_count":project_count,
        "projectcategories":projectcategories
    }
    return render(request, 'project.html', context)