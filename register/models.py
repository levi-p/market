from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


# Create your models here.

class Sign_up(models.Model):
    First_name=models.CharField(max_length=30, default='',blank=True)
    Email=models.EmailField(blank=True,default='')
    password=models.CharField(max_length=30,default='')
    enter_password=models.CharField(max_length=30,default='',blank=True)

    def __str__(self):
        return self.Name

class userprofile(models.Model):
    first_name = models.ForeignKey(User,related_name='name1',blank=True ,null=True)
    Last_name = models.CharField(max_length=30,null=True,blank=True)
    Year_of_birth = models.CharField(max_length=30,null=True,blank=True)
    user_id = models.IntegerField(blank=True)
    email = models.EmailField(blank=True,null=True,default="youremail@email.com")
    location = models.CharField(max_length=30, default='',blank=True)
    profile_pic = models.ImageField(blank=True)
    picToShow= models.ImageField(null=True,blank=True)#,editable=False)
    Phone_number = models.CharField(max_length=13, default='000 000 000',blank=True)
    choices = [('1','true'),('2','false'),]
    active = models.CharField(max_length=5,choices = choices,default='yes', null=True)

    

    def save(self):
      try: 
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (165, 165)

        # Open original photo which we want to thumbnail using PIL's Image
        # object
        image = Image.open(os.path.join('./media/',self.profile_pic.name))

        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0)

        # Save to the thumbnail field
        suf = SimpleUploadedFile(os.path.split(self.profile_pic.name)[-1],
                temp_handle.read(), content_type='image/png')
        self.picToShow.save(suf.name+'.png', suf, save=False)

        # Save this photo instance
        super(userprofile, self).save()
      except:super(userprofile, self).save()
    class Admin:
        pass


    def __str__(self):
        return str(self.first_name)












    

    
