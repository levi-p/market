from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.





class Category(models.Model):
    Name=models.CharField(max_length=30,blank=True)
    Discription=models.TextField(default='')
    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
       return reverse('category_all',kwargs={'name_id':self.id,})

class SubCategory(models.Model):
    category_name=models.ForeignKey(Category)
    name=models.CharField(max_length=30)
    category_name=models.ForeignKey(Category,blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return reverse('subCategory_all',kwargs={'sub_id':self.id,})


class Product(models.Model):

    sub_c=models.ForeignKey(SubCategory,null=True)
    views=models.IntegerField(default=0)
    participants=models.TextField(default=0)
    seller=models.ForeignKey(User,related_name='seller',blank=True ,null=True)
    Product_name=models.CharField(max_length=30, default='')
    Discription=models.TextField()
    Price=models.IntegerField()
    #category_name=models.ForeignKey(Category,blank=True,null=True)
    pic1=models.ImageField()
    pic2=models.ImageField(blank=True)
    pic3=models.ImageField(blank=True)
    recommended=models.CharField(max_length=30, default='',blank=True)
    time=models.DateField(default=timezone.now,blank=True)
    is_sold=models.CharField(max_length=5,default='no')
    


    def get_absolute_url(self):
        return reverse('main:product_details',kwargs={'Pk':self.pk,})

    def __str__(self):
         return self.Product_name
    

class Comment(models.Model):
    read=models.TextField(blank=True)
    products=models.ForeignKey(Product)
    Name=models.CharField(max_length=30,blank=True)
    comment=models.TextField()
    time=models.DateField(default=timezone.now,blank=True)

    def __str__(self):
         return self.Name
 
    def get_absolute_url(self):
        return reverse('main:product_details',kwargs={'Pk':self.products.id,})



