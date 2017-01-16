from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
#from zinnia.markups import html_format
import datetime
from django.utils import timezone



now = timezone.now

# Create your models here.

class Comments(models.Model):
    Name = models.CharField(max_length=30,default='anonymous')
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.Name


#class author(models.Model):
    

class Article_details(models.Model):
    Title = models.CharField(max_length=120)
    Article = models.TextField(blank=True)
    Pic = models.ImageField(blank=True)
    time=models.DateField(default=now)
    
    A_Name=models.CharField(max_length=50,blank=True)
    A_pic=models.ImageField(blank=True)
    choices=[('1','yes'),('2','no')]
    public = models.CharField(max_length=5,choices = choices,default=1, null=True)
    


    @property
    def html_content(self):
        """
        Returns the "content" field formatted in HTML.
        """
        return html_format(self.Article)

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('art:article',kwargs={'article_id':self.id,})

class article_Comment(models.Model):
    #read=models.TextField(blank=True)
    article=models.ForeignKey(Article_details)
    Name=models.CharField(max_length=30,blank=True)
    comment=models.TextField()
    time=models.DateField(default=timezone.now,blank=True)

    def __str__(self):
         return self.Name
 
    def get_absolute_url(self):
        return reverse('art:article',kwargs={'article_id':self.id,})    
 #return reverse('main:product_details',kwargs={'Pk':self.products.id,})

    


    

    
