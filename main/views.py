from django.shortcuts import render,redirect
from .models import Product,Category,Comment
from register.models import userprofile
from .forms import ProductUploadForm,ProductCommentForm,Noti



# Create your views here.

def notify(request):
    
    

    


    


    return render(request,'notifications.html',locals())

def ProductView(request,Pk):
    product=Product.objects.get(pk=Pk)
    sellerprofile=userprofile.objects.get(first_name=product.seller)
    product.views+=1
    product.save()
    
    #add user ro have read list
    h=Comment.objects.filter(products=product)
    for i in h:
        if str(request.user.id) in i.products.participants:
            i.read+=str(request.user)+' '
            i.save()

    #put a participant id in product to receive notifications for that product
    if str(request.user.id) not in product.participants:

        product.participants+=str(request.user.id)
        product.save()

    form=ProductCommentForm(request.POST)
    if form.is_valid():
        Name=form.cleaned_data['Name']
        comment=form.cleaned_data['comment']
        
        if request.user.is_authenticated():
            comm=Comment(Name=request.user,comment=comment,products=product,read=request.user)
            comm.save()
        else:
            comm=Comment(Name=Name,comment=comment,products=product,read=request.user)
            comm.save()
        #reset all reads to include only poster
        Comment.objects.filter(products=product.id).update(read=str(request.user))
    
    return render(request,'product_details.html',locals())

def ProductUpload(request):

    try:
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
        
    except:
        error2="please select an image for pic1"
        return redirect('/')
    return render(request,'UploadProduct.html',locals())
