from django.urls import path
from .views import homeslider_views
from .views import our_service_views

urlpatterns = [
    
    path('', homeslider_views.HomeSliderList, name='HomeSliderList'),
    # path('/service', our_service_views.OurServiceList, name='OurServiceList')
    
]
