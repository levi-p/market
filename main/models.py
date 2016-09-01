from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    Name=models.CharField(max_length=30,blank=True)
    Discription=models.TextField(default='')
    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
       return reverse('category_all',kwargs={'name_id':self.id,})

class Product(models.Model):
    seller=models.ForeignKey(User,related_name='seller',blank=True ,null=True)
    Product_name=models.CharField(max_length=30, default='')
    Discription=models.TextField()
    Price=models.IntegerField()
    category_name=models.ForeignKey(Category,blank=True,null=True)
    pic1=models.ImageField(blank=True)
    pic2=models.ImageField(blank=True)
    pic3=models.ImageField(blank=True)
    recommended=models.CharField(max_length=30, default='',blank=True)
    


    def get_absolute_url(self):
        return reverse('main:product_details',kwargs={'Pk':self.pk,})

    def __str__(self):
         return self.Product_name
    
