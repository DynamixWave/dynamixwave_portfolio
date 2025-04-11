from django.shortcuts import render,redirect,get_object_or_404
from ..models import *

def Blogdetail(request, pk):
    blogs = BlogModel.objects.all().order_by('-id')[:3]
    posts = BlogModel.objects.filter(category=pk)
    categories = BlogCategoryModel.objects.all()
    blog = get_object_or_404(BlogModel, id=pk) 
    
    context = {
        'blogs':blogs,
        'blog':blog,
        'posts':posts,
        'categories':categories
        
    }
    return render(request, 'blog_detail.html', context)

def BlogCategoryFilterView(request, category_id):
    category = get_object_or_404(BlogCategoryModel, id=category_id)
    blogs = BlogModel.objects.filter(category=category)
    
    context = {
        'blogs': blogs,
        'selected_category': category,
        'categories': BlogCategoryModel.objects.all(),
    }
    return render(request, 'category.html', context)




