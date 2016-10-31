from django.shortcuts import render
from .forms import orderForm
from .models import order

# Create your views here.

def orderView(request):

    if request.method=='POST':

        form=orderForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            phonenumber=form.cleaned_data['phoneNumber']
        
            orderOb=order(phoneNumber=phonenumber,Name=name)
            orderOb.save()
    else: form=orderForm()




    return render(request,'order.html',locals())
