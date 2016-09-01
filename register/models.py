from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sign_up(models.Model):
    Name=models.CharField(max_length=30, default='')
    Email=models.EmailField(blank=True,default='')
    password=models.CharField(max_length=30,default='')
    enter_password=models.CharField(max_length=30,default='')

class userprofile(models.Model):
    first_name = models.ForeignKey(User,related_name='name1',blank=True ,null=True)
    email=models.EmailField(blank=True,null=True)
    location=models.CharField(max_length=30, default='')
    profile_pic=models.ImageField(blank=True)
    Phone_number=models.IntegerField( default=0)

    

    
