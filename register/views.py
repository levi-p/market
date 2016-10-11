from django.shortcuts import render,redirect
from .forms import Sign_up_form ,Profile_form,ChangePasswordForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Sign_up,userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
import random




# Create your views here.


def Sign_up_v(request):
    
        try:
            form=Sign_up_form(request.POST)
            if form.is_valid():
                Username=form.cleaned_data['First_name']
            
                password1 = form.cleaned_data['password']
                password2=form.cleaned_data['enter_password']
            
                if password1 == password2 : 
                    user=User.objects.create_user(Username,'youremail@email.com',password1)
                    user.save()
                    logde=authenticate(username=form.cleaned_data['First_name'],password=form.cleaned_data['password'])

                    login(request,logde)
                    return redirect('Sign_up:profile_edit')
                
                
                else:
                    pass
       
    
        except Exception,e:
            error2="you are already registered, please login"+ str(e)
        return render(request,'sign_up.html',locals())

def profile(request):
    

    profile=userprofile.objects.get(email=request.user.email)
    return render(request,'profile.html',locals())

def Profile_edit(request,template):

    
    init = {"location":"ll",}
    
    if request.method == 'POST' :
        form=Profile_form(request.POST,request.FILES)
        my=request.user.id
        try:
        #
        #see if user already has already created a profile
            
            get_prof_by_user_id=userprofile.objects.get(user_id=my)
            if form.is_valid():
                location=form.cleaned_data['location']
                Phone_number=form.cleaned_data['Phone_number']
                year_of_birth = form.cleaned_data['Year_of_birth']
                last_name = form.cleaned_data['Last_name']
                #this is to update an already esisting profile
                try :
                    obj=userprofile.objects.filter(user_id=my).update(first_name=request.user,email=request.user.email,location=location,
                         Phone_number=Phone_number,Year_of_birth=year_of_birth,Last_name=last_name,)
                    return redirect('/')
                except:
                    error='Please enter a valid phone number'
            else: pass
     

        except:
            
            P_obj=userprofile(first_name=request.user,email=request.user.email,location='location',user_id=request.user.id)
            P_obj.save()
        
    elif template=='Profile_editAll.html' :
        try:
            Instance=userprofile.objects.get(user_id=request.user.id).__dict__
            form=Profile_form(initial=Instance)
        except :pass
    else: 
        try:
            
           form=Profile_form() 
        except :pass    
    return render(request,template,locals())
    
    

def changePassword(request):
     form=ChangePasswordForm(request.POST)
     if form.is_valid():
         adp=random.randrange(1,7)
         User_name=form.cleaned_data['user_name']
         u=User.objects.get(username=User_name)
         u.set_password(str(User_name) + str(adp))
         message="your password has been changed!, you will receive an sms soon"# + str(adp)
         u.save()

     return render(request,'passChange.html',locals())














