from django.db import models
from cloudinary.models import CloudinaryField  

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = CloudinaryField('image', blank=True, null=True)
    
    github_link = models.URLField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.title
    




    
    