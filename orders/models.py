from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class order(models.Model):
    Name=models.CharField(max_length=30,null=True)
    phoneNumber=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    time=models.DateField(default=timezone.now,blank=True)

    def __str__(self):
        return self.Name

