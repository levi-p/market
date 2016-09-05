from django.shortcuts import render,redirect
from .forms import Sign_up_form ,Profile_form
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Sign_up,userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login




# Create your views here.

#@csrf_protect
def Sign_up_v(request):
    
        try:
            form=Sign_up_form(request.POST)
            if form.is_valid():
                Username=form.cleaned_data['Name']
            #Email=form.cleaned_data['Email']
                password1 = form.cleaned_data['password']
                password2=form.cleaned_data['enter_password']
            
                if password1 == password2 : 
                #form.save()
                #d=Sign_up(Username,Email,password1)
                #d.save()
                    user=User.objects.create_user(Username,'youremail@email.com',password1)
                    user.save()
                    logde=authenticate(username=form.cleaned_data['Name'],password=form.cleaned_data['password'])

                    login(request,logde)
                    return redirect('Sign_up:profile_edit')
                
                
                else:
                    pass
    #else:   
     #   form=Sign_up_form()
        except:
            error2="you are already registered, please login"
        return render(request,'sign_up.html',locals())

def profile(request):
    

    profile=userprofile.objects.get(email=request.user.email)
    return render(request,'profile.html',locals())

def Profile_edit(request):
    form=Profile_form(request.POST,request.FILES)
    my=request.user.id
    try:
        get_prof_by_user_id=userprofile.objects.get(user_id=my)
    
    
        if form.is_valid():
        
            location=form.cleaned_data['location']
        #profile_pic=form.cleaned_data['profile_pic']
            Phone_number=form.cleaned_data['Phone_number']

            try :
                obj=userprofile.objects.filter(user_id=my).update(first_name=request.user,email=request.user.email,location=location,Phone_number=Phone_number)
                return redirect('/')
            except:
                error='Please enter a valid phone number'

    except:
        P_obj=userprofile(first_name=request.user,email=request.user.email,location='location',user_id=request.user.id)
        P_obj.save()
            
         

        
    return render(request,'Profile_edit.html',locals())
    
    












