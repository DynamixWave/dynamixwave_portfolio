from django.contrib import admin
from django.db import models
from .models import *

# Register your models here.


class HomeSliderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'discover_more']
    search_fields = ['id', 'title']
    list_filter = ['id', 'title']
    
class OurServiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['id', 'title']
    list_filter = ['id', 'title']
    
class OurServiceListModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    
admin.site.register(HomeSliderModel, HomeSliderModelAdmin)
admin.site.register(OurServiceModel, OurServiceModelAdmin)
admin.site.register(OurServiceListModel, OurServiceListModelAdmin)
    