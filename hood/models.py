from django.db import models
from django.contrib.auth.models import User
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
    police_contact = models.IntegerField(null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.name} hood'
    
    def create_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()  
        
    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        return cls.object.filter(id=neighbourhood_id)  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name ='profile')
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to='images/',default ='default.png')
    location = models.CharField(max_length=50,blank=True, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    
    def __str__(self):
        return f'{self.user.username}profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save 

 
    
class Business(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    description = models.TextField(blank=True)   
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete = models.CASCADE,related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    
    def __str__(self):
        return f'{self.name}Business'
    
    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    @classmethod
    def search_business(cls,name):
        return cls.objects.filter(name_icontains = name).all()             

class Post(models.Model):
    title = models.CharField(max_length=120,null=True)
    post = models.TextField()
    date = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')
    
       