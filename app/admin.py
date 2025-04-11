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
    list_display = ['id', 'name', 'icon_image', 'content', 'image_inner']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    
class OurPartnerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'url']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    
class ProjectCategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['id', 'name','slug']
    search_fields = ['id', 'name', 'slug']
    list_filter = ['id', 'name', 'slug']
    
class ProjectModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['id', 'category', 'name', 'image', 'slug']
    search_fields = ['id', 'name', 'category']
    list_filter = ['id', 'name']
    
class CounterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'count_number']
    search_fields = ['id', 'name', 'count_number']
    list_filter = ['id', 'name']
    
class WhyChooseUsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image_1', 'image_2']
    search_fields = ['id', 'title','content']
    list_filter = ['id', 'title']
    
class CertificateGalleryModelInline(admin.TabularInline):
    model = CertificateGalleryModel
    
class OurTeamMemberModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'name', 'position', 'facebook', 'telegram', 'viber', 'whatsapp', 'title', 'content', 'certificate_title']
    search_fields = ['id', 'name', 'position', 'title']
    inlines = [CertificateGalleryModelInline]
    list_filter = ['id', 'name', 'position']
    
class CustomerFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'image', 'position']
    search_fields = ['id', 'name', 'content', 'position']
    list_filter = ['id', 'name', 'position']
    
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'image', 'get_categories', 'date']
    search_fields = ['id', 'title', 'content', 'category__name', 'date']
    list_filter = ['id', 'title', 'content', 'category', 'date']
    
    
     
    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    get_categories.short_description = 'Categories'
 
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'mobile', 'mobile', 'subject', 'message']

    
    

    
    
    

    
    
    
    
    
    
admin.site.register(HomeSliderModel, HomeSliderModelAdmin)
admin.site.register(OurServiceModel, OurServiceModelAdmin)
admin.site.register(OurServiceListModel, OurServiceListModelAdmin)
admin.site.register(OurPartnerModel, OurPartnerModelAdmin)
admin.site.register(ProjectCategoryModel, ProjectCategoryModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)
admin.site.register(CounterModel, CounterModelAdmin)
admin.site.register(WhyChooseUsModel, WhyChooseUsModelAdmin)
admin.site.register(OurTeamMemberModel, OurTeamMemberModelAdmin)
admin.site.register(CustomerFeedbackModel, CustomerFeedbackModelAdmin)
admin.site.register(BlogCategoryModel, BlogCategoryModelAdmin)
admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)

    