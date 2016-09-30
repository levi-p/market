from django.shortcuts import render,redirect
from .models import Product,Category,Comment
from register.models import userprofile
from django import forms
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
    
    form=ProductCommentForm(request.POST)#,sub_c='Electronics')
    if form.is_valid():
        Name=form.cleaned_data['Name']
        comment=form.cleaned_data['comment']
        
        if request.user.is_authenticated():
            comm=Comment(Name=request.user,comment=comment,products=product,read=request.user)
            comm.save()
            form=ProductCommentForm()
            return redirect(product.get_absolute_url())
        else:
            
            comm=Comment(Name=Name,comment=comment,products=product,read=request.user)
            comm.save()
            form=ProductCommentForm()
        #reset all reads to include only poster
        Comment.objects.filter(products=product.id).update(read=str(request.user))
    
    return render(request,'product_details.html',locals())
    
    
    
def ProductUpload(request,Pk):
   
    

    #ProductUploadForm.base_fields['sub_c'].querset=forms.ModelChoiceField(queryset=Product.objects.filter(sub_c_id=1))
    cc=1
    form=ProductUploadForm(request.POST,request.FILES,cc=Pk)
    
    if form.is_valid():
        sub=form.cleaned_data['sub_c']
        Product_name=form.cleaned_data['Product_name']
        price=form.cleaned_data['Price']
        discription= form.cleaned_data['Discription']
        category=form.cleaned_data['sub_c']
        pic1=form.cleaned_data['pic1']
        pic2=form.cleaned_data['pic2']
        
        
        P_d=Product(sub_c=sub,seller=request.user,Product_name=Product_name,Discription=discription,Price=price,pic1=pic1,pic2=pic2)
        #P_d=Product(Product_name=Product_name,Discription=discription,Price=price,pic1=pic1,pic2=pic2,pic3=pic3)
        P_d.save()
        fd=P_d.sub_c.category_name
        categ=Category.objects.get(Name=fd)
        return redirect(categ.get_absolute_url())
        
    else:
        error='errr'
        
    #except:
     #   error2="please select an image for pic1"
      #  return redirect('/')
    return render(request,'UploadProduct.html',locals())
