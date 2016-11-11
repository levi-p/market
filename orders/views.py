from django.shortcuts import render
from .forms import orderForm
from .models import order
from main.t import sendMessage

# Create your views here.

def orderView(request,PD):
    pd=PD

    if request.method=='POST':

        form=orderForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            phonenumber=form.cleaned_data['phoneNumber']
        
            orderOb=order(phoneNumber=phonenumber,Name=name,product_name=PD)
            orderOb.save()
            msg=str(PD) + " " + "order by " + " " + str(name)
            send = sendMessage('0881460566',msg)
            send.go()
    else: form=orderForm()




    return render(request,'order.html',locals())
