from django.urls import path
from .views import home_views
from .views import blog_views
from .views import search_views
from .views import contact_views
from .views import ourteam_views
from .views import service_views
from .views import project_views
from .views import about_views
from .views import faqs_views
from .views import fzf_views
from .views import newsletter_views

urlpatterns = [
    
    path('', home_views.HomeSliderList, name='HomeList'),
    path('newsletter/', newsletter_views.newsletter, name='newsletter'),
    path('detail/<uuid:pk>/', blog_views.Blogdetail, name='detail'),
    path('contact/', contact_views.Contact, name='contact'),
    path('ourteam/', ourteam_views.Ourteam, name='ourteam'),
    path('ourteam/detail/<uuid:pk>/', ourteam_views.Ourteam_detail, name='ourteam_detail' ),
    path('service/', service_views.ServiceList, name='service_list'),
    path('service/service_detail/<uuid:pk>/', service_views.ServiceDetil, name='service_detail'),
    path('project/', project_views.ProjectList, name='project_list'),
    # path('project/project_detail/<uuid:pk>/', project_views.Project_detail, name='project_detail'),
    path('blog/', blog_views.BlogList, name='blog_list'),
    path('about/', about_views.AboutList, name='about_list'),
    path('faqs/', faqs_views.faqs, name='faqs_list'),
    path('404/', fzf_views.error, name='404'),
    
    path('<slug:category_slug>/', home_views.HomeSliderList, name='project_by_category'),
    path('blog/category/<uuid:category_id>/', blog_views.BlogCategoryFilterView, name='blog_category_filter'),

    path('service/category/<uuid:category_id>/', service_views.ServiceByCategory, name='service_by_category'),

    
]
