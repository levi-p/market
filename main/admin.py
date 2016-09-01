from django.contrib import admin
from .models import Product,Category

# Register your models here.
class Pd(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        if not change:
            obj.seller=request.user
        obj.save()


admin.site.register(Product,Pd)
admin.site.register(Category)
