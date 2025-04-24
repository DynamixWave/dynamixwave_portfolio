from django.shortcuts import render,redirect,get_object_or_404
from ..models import *

def BlogList(request):
    blogs = BlogModel.objects.all()
    
    context = {
        'blogs':blogs
    }
    return render(request, 'blog.html', context)


def Blogdetail(request, pk):
    latestblogs = BlogModel.objects.all().order_by('-id')[:3]
    categories = BlogCategoryModel.objects.all()
    blog = get_object_or_404(BlogModel, id=pk) 
    blogs = BlogModel.objects.all().order_by('-id')
    
    context = {
        'latestblogs':latestblogs,
        'blog':blog,
        'categories':categories,
        'blogs':blogs
    }
    return render(request, 'blog_detail.html', context)


def BlogCategoryFilterView(request, category_id):
    category = get_object_or_404(BlogCategoryModel, id=category_id)
    blogs = BlogModel.objects.filter(category=category).order_by('-id')[:1]
    
    latestblogs = BlogModel.objects.filter(category=category).order_by('-id')[:5]
    
    context = {
        'blogs': blogs,
        'latestblogs': latestblogs,
        'selected_category': category,
        'categories': BlogCategoryModel.objects.all(),
    }
    return render(request, 'blog_by_category.html', context)




