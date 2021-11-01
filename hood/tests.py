from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import *


class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.new_profile = Profile(user_id=2,hood_id = 3, bio ='test bio',email='halima@gmail.com', name ='halima', profile_pic = 'default.jpeg')
        
    def test_instance(self):
        self.assetTrue(isinstance(self.new_profile,Profile))
            
    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects()
        self.assertTrue(len(profile)>0)
        
        
    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objecta.all()
        self.assertTrue(len(profile)==0)
    
    def tearDown(self):
        profile.objecta.all().delete()
            
            
            
            
            
            
            
            
            
            
                