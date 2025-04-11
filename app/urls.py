from django.urls import path
from .views import home_views
from .views import blog_views
from .views import search_views
from .views import contact_views
from .views import ourteam_views
from .views import service_views
from .views import project_views

urlpatterns = [
    
    path('', home_views.HomeSliderList, name='HomeList'),
    path('detail/<uuid:pk>/', blog_views.Blogdetail, name='detail'),
    path('contact/', contact_views.Contact, name='contact'),
    path('ourteam/', ourteam_views.Ourteam, name='ourteam'),
    path('ourteam/detail/<uuid:pk>/', ourteam_views.Ourteam_detail, name='ourteam_detail' ),
    path('service/', service_views.ServiceList, name='service_list'),
    path('service/detail/<uuid:pk>/', service_views.ServiceDetil, name='service_detail'),
    path('project/', project_views.ProjectList, name='project_list'),


    
    path('<slug:category_slug>/', home_views.HomeSliderList, name='project_by_category'),
    path('blog/category/<uuid:category_id>/', blog_views.BlogCategoryFilterView, name='blog_category_filter'),
    
    
]
