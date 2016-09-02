from django.shortcuts import render
from main.models import Product,Category

def home(request):
    #ds=request.user.email
    caet=Category.objects.all()
    reco=Product.objects.filter(recommended='yes')
    return render(request,'base.html',locals())

def categoryView(request,name_id):
    cat2=Category.objects.get(id=name_id)
    products=Product.objects.filter(category_name=name_id)
    
    return render(request,'product_category.html',locals())
    


