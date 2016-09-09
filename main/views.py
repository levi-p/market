from django.shortcuts import render,redirect
from .models import Product,Category
from register.models import userprofile
from .forms import ProductUploadForm


# Create your views here.

def ProductView(request,Pk):
    product=Product.objects.get(pk=Pk)
    sellerprofile=userprofile.objects.get(first_name=product.seller)
    
    return render(request,'product_details.html',locals())

def ProductUpload(request):

    
    form=ProductUploadForm(request.POST,request.FILES)
    
    if form.is_valid():
        
        Product_name=form.cleaned_data['Product_name']
        price=form.cleaned_data['Price']
        discription= form.cleaned_data['Discription']
        category=form.cleaned_data['category_name']
        pic1=form.cleaned_data['pic1']
        pic2=form.cleaned_data['pic2']
        
        
        P_d=Product(seller=request.user,Product_name=Product_name,Discription=discription,Price=price,category_name=category,pic1=pic1,pic2=pic2)
        #P_d=Product(Product_name=Product_name,Discription=discription,Price=price,pic1=pic1,pic2=pic2,pic3=pic3)
        P_d.save()
        categ=Category.objects.get(Name=category)
        return redirect(categ.get_absolute_url())
        
    else:
        error='errr'
        

    return render(request,'UploadProduct.html',locals())
