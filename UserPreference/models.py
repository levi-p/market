from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from register.models import userprofile

# Create your models here.

class Preference(models.Model):
    Choices=[('Clothing,Electronics','hgh'),('Clothing,Electronics','hgh')]
    use_r=models.ForeignKey(userprofile,null=True)
    I_like=models.CharField(max_length=70,null=True,blank=True)#,choices=Choices)



