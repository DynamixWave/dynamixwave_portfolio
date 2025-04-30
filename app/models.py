from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class HomeSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='HomeSlider')
    title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    discover_more = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class OurServiceModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextField(null=True,  blank=True)
    
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
    content = RichTextField(null=True, blank=True)
    points = models.JSONField(null=True, blank=True)
    service_detail_icon_1 = models.ImageField(upload_to='OurService', null=True, blank=True)
    service_detail_icon_title_1 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_1_content = RichTextField(null=True, blank=True)
    service_detail_icon_2 = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    service_detail_icon_title_2 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_2_content = RichTextField(null=True, blank=True)
    service_detail_icon_3 = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    service_detail_icon_title_3 = models.CharField(max_length=1000, null=True,blank=True) 
    service_detail_icon_3_content = RichTextField(null=True, blank=True)
    benefits_title = models.CharField(max_length=200, null=True, blank=True)
    benefits_image = models.ImageField(upload_to='Ourservice', null=True, blank=True)
    benefits_content = RichTextField(null=True, blank=True)

    
    
    def __str__(self):
        return self.name
    
class AccrodionModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    accrodion = models.ForeignKey(OurServiceListModel, on_delete=models.CASCADE, null=True ,blank=True, related_name='accrodion_value')
    accrodion_title = models.CharField(max_length=1000, null=True, blank=True)
    accrodion_content = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.accrodion_title
    
    
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
    pj_url = models.URLField(null=True, blank=True)
    
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
    content = RichTextField()
    image_1 = models.ImageField(upload_to='WhyChooseUs')
    image_2 = models.ImageField(upload_to='WhyChooseUs')
    points = models.JSONField(null=True, blank=True)
    
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
    content = RichTextField(null=True, blank=True)
    certificate_title = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class CertificateGalleryModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    ourteam = models.ForeignKey(OurTeamMemberModel, on_delete=models.CASCADE, null=True, blank=True, related_name='certificates')
    certificate_image = models.ImageField(upload_to='certificate', null=True, blank=True)
    
    def __str__(self):
        return f"{self.ourteam.name} - certificate_image"
    
class OurTeamProgressModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    ourteam_progress = models.ForeignKey(OurTeamMemberModel, on_delete=models.CASCADE, null=True ,blank=True, related_name='progress_value')
    title = models.CharField(max_length=1000, null=True, blank=True)
    progress_value = models.CharField(max_length=200, null=True ,blank=True)
    
    def __str__(self):
        return self.title

    
    
class CustomerFeedbackModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    content = RichTextField()
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
    content = RichTextField()
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
    subject = RichTextField(null=True, blank=True)
    message = RichTextField()
    
    def __str__(self):
        return self.name
        
class AboutModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000, null=True, blank=True)
    sec_title = models.CharField(max_length=1000, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='About')
    points = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    
    
class NewsletterMode(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.email  