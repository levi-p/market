from __future__ import unicode_literals

from django.db import models
from register.models import userprofile
import datetime

from django.utils import timezone
from django.contrib.auth.models import User

now = datetime.datetime.now
# Create your models here.

class Message(models.Model):
    From = models.ForeignKey(userprofile,related_name='from1')
    To = models.ForeignKey(userprofile,related_name='to1')
    message = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    readBy = models.CharField(max_length=4,null=True)

    def __str__(self):
        return str(self.From) + " " + " to "  + str(self.To)
    
class Followers(models.Model):
    userToFollow = models.ForeignKey(User)
    followers = models.CharField(max_length=500)
    
    def __str__(self):
        return "%s is followed by" %self.userToFollow

class Following(models.Model):
    me = models.ForeignKey(User)
    following = models.CharField(max_length=5)
