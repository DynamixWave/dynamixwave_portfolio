from django.shortcuts import render,redirect
from ..models import *
from django.db.models import Q

# def search_by(request):
#     search = request.GET.get('search-box')
#     blogs = []
#     if search:
#         blogs= BlogModel.objects.filter(
#             Q(title__icontains=search) | Q(content__icontains=search)
#         )
#     categories = BlogCategoryModel.objects.all()
    
#     context = {
#         "blogs":blogs,
#         "categories":categories,
#     }
#     return render(request, 'blog_detail.html', context)