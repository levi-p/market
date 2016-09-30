from django.shortcuts import render
from main.models import Product,Category,Comment,SubCategory

from main.context_p import conte

def call(request):
    categories=Category.objects.all()
    subcategories=SubCategory.objects.all()
    
    return render(request,'uploadRedirect.html',locals())

def home(request):
    idi=request.user.id
    caet=Category.objects.all()
    reco=Product.objects.filter(recommended='yes')
    return render(request,'base.html',locals())

def categoryView(request,name_id):
    
    sub=SubCategory.objects.filter(category_name__id=name_id)
    products=Product.objects.filter(sub_c__category_name__id=name_id)
    
    return render(request,'product_category.html',locals())
    
def subCategoryView(request,sub_id):
    
   # sub=SubCategory.objects.filter(category_name__id=name_id)
    products=Product.objects.filter(sub_c__id=sub_id)
    
    return render(request,'sub_category.html',locals())



