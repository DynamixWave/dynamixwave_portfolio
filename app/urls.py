from django.urls import path
from .views import homeslider_views

urlpatterns = [
    
    path('', homeslider_views.HomeSliderList, name='HomeSliderList')
    
]
