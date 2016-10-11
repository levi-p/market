from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sign_up(models.Model):
    First_name=models.CharField(max_length=30, default='')
    Email=models.EmailField(blank=True,default='')
    password=models.CharField(max_length=30,default='')
    enter_password=models.CharField(max_length=30,default='')

    def __str__(self):
        return self.Name

class userprofile(models.Model):
    first_name = models.ForeignKey(User,related_name='name1',blank=True ,null=True)
    Last_name = models.CharField(max_length=30,null=True,blank=True)
    Year_of_birth = models.CharField(max_length=30,blank=True,null=True)
    user_id = models.IntegerField(blank=True)
    email = models.EmailField(blank=True,null=True,default="youremail@email.com")
    location = models.CharField(max_length=30, default='')
    profile_pic = models.ImageField(blank=True)
    Phone_number = models.CharField(max_length=12, default='000 000 000')

    def __str__(self):
        return str(self.first_name)

    

    
