from django.contrib import admin
from .models import Sign_up,userprofile

# Register your models here.



class dop(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        if not change:
            obj.first_name=request.user
            obj.email=request.user.email
            obj.user_id=request.user.id
         
        obj.save()
        

admin.site.register(Sign_up)
admin.site.register(userprofile,dop)
