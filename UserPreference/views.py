from django.shortcuts import render
from .forms import preferenceForm
from main.models import Category
from .models import Preference
from register.models import userprofile

# Create your views here.

def Prefer(request):
    pref=Category.objects.all().__dict__.items()
    if 1==1:
        form=preferenceForm(request.POST)
        if form.is_valid():
            
            kl=request.POST.getlist('I_like')
            cg=(form.cleaned_data['I_like'])
         
            Use_r=userprofile.objects.get(first_name=request.user)

            cf=Preference(I_like=cg,use_r=Use_r)
            #nl='hhhhhhhhhhhhhhhhhhhhhhh'
            cf.save()
    else:
        kl="request.POST('I_like')"
        form=preferenceForm()
    return render(request,'preferences.html',locals())
