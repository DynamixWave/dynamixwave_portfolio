from django.db import models
import uuid

# Create your models here.

class HomeSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    title = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='HomeSlider')
    discover_more = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
  
    