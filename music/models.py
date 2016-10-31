from __future__ import unicode_literals

from django.db import models

# Create your models here.

class music(models.Model):
    Artist=models.CharField(max_length = 30)
    Title=models.CharField(max_length = 40)
    Song = models.FileField()

    class Meta:
        verbose_name_plural='music'
    def __str__(self):
        return self.Title
    
