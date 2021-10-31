from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length= 60)
    location = models.CharField(max_length=50)
    admin = models.ForeignKey("Profile", on_delete= models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to ='images/')
    description = models.TextField()
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IPAddressField(null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.name} hood'
    
    def create_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()  
        
    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        return cls.object.filter(id=neighbourhood_id)       
