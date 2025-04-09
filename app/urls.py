from django.urls import path
from .views import home_views
from .views import our_service_views

urlpatterns = [
    
    path('', home_views.HomeSliderList, name='HomeSliderList'),
    path('<slug:category_slug>/', home_views.HomeSliderList, name='project_by_category'),
    
]
