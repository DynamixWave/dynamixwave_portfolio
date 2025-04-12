from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class HomeSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='HomeSlider')
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    discover_more = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class OurServiceModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True,  blank=True)
    
    def __str__(self):
        return self.title
    
class OurServiceListCategory(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
       
    
class OurServiceListModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(OurServiceListCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='service_category')
    icon_image = models.ImageField(upload_to='OurService')
    image_inner = models.ImageField(upload_to='OurService', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    service_detail_icon_1 = models.ImageField(upload_to='OurService', null=True, blank=True)
    service_detail_icon_title_1 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_1_content = models.TextField(null=True, blank=True)
    service_detail_icon_2 = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    service_detail_icon_title_2 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_2_content = models.TextField(null=True, blank=True)
    service_detail_icon_3 = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    service_detail_icon_title_3 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_3_content = models.TextField(null=True, blank=True)
    
    benefits_title = models.CharField(max_length=200, null=True, blank=True)
    benefits_image = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    benefits_content = models.TextField(null=True, blank=True)
    accrodion_title_1 = models.CharField(max_length=1000, null=True, blank=True)
    accrodion_content_1 = models.TextField(null=True, blank=True)
    accrodion_title_2 = models.CharField(max_length=1000, null=True ,blank=True)
    accrodion_content_2 = models.TextField(null=True, blank=True)
    accrodion_title_3 = models.CharField(max_length=1000 ,null=True, blank=True)
    accrodion_content_3 = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
class OurPartnerModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='OurPenter', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ProjectCategoryModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True,blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
class ProjectModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    category = models.ForeignKey(ProjectCategoryModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='category')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True,blank=True)
    image = models.ImageField(upload_to='Project')
    
    def __str__(self):
        return self.name
    
class CounterModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Counter')
    count_number = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class WhyChooseUsModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_1 = models.ImageField(upload_to='WhyChooseUs')
    image_2 = models.ImageField(upload_to='WhyChooseUs')
    
    def __str__(self):
        return self.title
    
    
class OurTeamMemberModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='OurTeam')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    facebook = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    viber = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    certificate_title = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class CertificateGalleryModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    ourteam = models.ForeignKey(OurTeamMemberModel, on_delete=models.CASCADE, null=True, blank=True, related_name='certificates')
    certificate_image = models.ImageField(upload_to='certificate', null=True, blank=True)
    
    def __str__(self):
        return f"{self.ourteam.name} - certificate_image"

    
    
class CustomerFeedbackModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='Customer')
    position = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class BlogCategoryModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='Blog')
    category = models.ManyToManyField(BlogCategoryModel, blank=True, related_name='blogcategory')
    date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    
class ContactModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.IntegerField(default=0)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
        
class AboutModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000, null=True, blank=True)
    sec_title = models.CharField(max_length=1000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='About')
    
    def __str__(self):
        return self.title

    
    
   