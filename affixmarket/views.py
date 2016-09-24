from django.shortcuts import render
from main.models import Product,Category,Comment

from main.context_p import conte

def call(request):
    return render(request,'productd_redirect.html',locals())

def home(request):
    #ds=request.user.email
    #notify=comment.objects.filter(is_read=False).filter(
    
    #
    #comment_list=[x for x in d if x.products in c]
    #cd=conte(request)
    #noti_number=cd.noti_number

    idi=request.user.id
        

    caet=Category.objects.all()
    reco=Product.objects.filter(recommended='yes')
    return render(request,'base.html',locals())

def categoryView(request,name_id):
    cat2=Category.objects.get(id=name_id)
    products=Product.objects.filter(category_name=name_id)
    
    return render(request,'product_category.html',locals())
    


