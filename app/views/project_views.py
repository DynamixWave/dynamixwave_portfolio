from django.shortcuts import redirect,render,get_object_or_404
from ..models import *

def ProjectList(request):
    projectcategories = ProjectCategoryModel.objects.all()
    projects = ProjectModel.objects.all()
    
    # if category_slug !=None:
    #     categories = get_object_or_404(ProjectCategoryModel, slug=category_slug)
    #     projects = ProjectModel.objects.filter(category=categories)
    #     project_count = projects.count()
    # else:
    #     projects = ProjectModel.objects.all()
    #     project_count = projects.count()
    
    context = {
        "projects":projects,
        "projectcategories":projectcategories
    }
    return render(request, 'project.html', context)

# def Project_detail(request, pk):
#     projectcategories = ProjectCategoryModel.objects.all()
#     project = get_object_or_404(ProjectModel, id=pk)
#     related_project = ProjectModel.objects.filter(category=project.category).exclude(pk=project.id)
    
#     context = {
#         'projectcategories':projectcategories,
#         'project':project,
#         'related_project':related_project
#     }
#     return render(request, 'project_detail.html', context)

