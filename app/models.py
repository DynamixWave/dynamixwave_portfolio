from django.db import models
import uuid

# Create your models here.

class HomeSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='HomeSlider')
    title = models.CharField(max_length=1000, null=True, blank=True)
    discover_more = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class OurServiceModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True,  blank=True)
    
    def __str__(self):
        return self.title
    
    
class OurServiceListModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='OurService')
    
    def __str__(self):
        return self.name
    
  
    