from django.shortcuts import render,redirect
from .forms import orderForm
from .models import order
from main.t import sendMessage
from main.models import Product

# Create your views here.

def orderView(request,PD):
    pd=Product.objects.get(pk=PD)
    

    if request.method=='POST':

        form=orderForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            phonenumber=form.cleaned_data['phoneNumber']
        
            orderOb=order(phoneNumber=phonenumber,Name=name,product_name=pd)
            orderOb.save()
            msg=str(PD) + " " + "order by " + " " + str(name)
            try:
                send = sendMessage('0881460566',msg)
                send.go()
            except: pass
            return redirect("success")
    else: form=orderForm()




    return render(request,'order.html',locals())
