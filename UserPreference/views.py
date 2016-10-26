from django.shortcuts import render,redirect
from .forms import preferenceForm
from main.models import Category
from .models import Preference
from register.models import userprofile

# Create your views here.

def Prefer(request):
    pref=Category.objects.all().__dict__.items()
    if request.method=='POST':
        form=preferenceForm(request.POST)
        if form.is_valid():
            
            kl=request.POST.getlist('I_like')
            cg=(form.cleaned_data['I_like'])
         
            Use_r=userprofile.objects.get(first_name=request.user)
            try:
                Preference.objects.get(use_r__first_name=request.user)
                preference=Preference.objects.filter(use_r__first_name=request.user)
                po=preference.update(I_like=cg,use_r=Use_r)
                print "opopop"
                
            except:

                cf=Preference(I_like=cg,use_r=Use_r)
                cf.save()
                print "kkkkkkkkkkk"
                
                
            
            finally:pass
            
        else: pass
        return redirect('Sign_up:profile')
                
        
    else:
        kl="request.POST('I_like')"
        form=preferenceForm()
    
    return render(request,'preferences.html',locals())
