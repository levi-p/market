from django.shortcuts import render,redirect
from .forms import Sign_up_form ,Profile_form,ChangePasswordForm,loginForm,Profile_form2
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Sign_up,userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
import random
from main.t import sendMessage
from django.contrib.auth.decorators import login_required
from main.models import Product
from UserPreference.models import Preference
 




# Create your views here.

def signIn(request):
    
    try:
        form=loginForm(request.POST)
        if form.is_valid():
            User_phone=form.cleaned_data['Phone_number']
            
            password1 = form.cleaned_data['password']

            number = userprofile.objects.get(Phone_number = User_phone)
            User_name = str(number.first_name)

            log=authenticate(username=User_name,password=form.cleaned_data['password'])

            login(request,log)
            return redirect('Sign_up:profile')
        #else: return redirect('/')


    except Exception,e: error="enter the correct phone number"+str(e)
    return render(request,'login.html',locals())


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
@login_required(redirect_field_name='login',login_url="Sign_up:log")
def profile(request):
    
    products=Product.objects.all()
    try:
        preference=Preference.objects.get(use_r__first_name=request.user)
        productlist=[i for i in products if str(i.sub_c.category_name) in preference.I_like ]
    except: pass
    
    profile=userprofile.objects.get(first_name__id=request.user.id)
    return render(request,'profile.html',locals())

@login_required(redirect_field_name='login',login_url="Sign_up:log")
def Profile_edit(request,template):

    
    init = {"location":"ll",}
    my=request.user.id
    form2=Profile_form2(request.POST,request.FILES)
    if template=='Profile_edit.html' :
        
        
        try:
        #
        #see if user already has already created a profile
            
            get_prof_by_user_id=userprofile.objects.get(user_id=my)
            
            if form2.is_valid():
                
                location=form2.cleaned_data['location']
                Phone_number=form2.cleaned_data['Phone_number']
                #year_of_birth = form.cleaned_data['Year_of_birth']
                #last_name = form.cleaned_data['Last_name']
                #this is to update an already esisting profile
                try :
                    obj=userprofile.objects.filter(user_id=my).update(location=location,
                         Phone_number=Phone_number)
                    return redirect('/')
                except Exception,e:
                    error='Please enter a valid phone number'+ str(e)
            else: form2=Profile_form2()
     

        except:
            
            P_obj=userprofile(first_name=request.user,email=request.user.email,location='location',user_id=request.user.id)
            P_obj.save()
        
    elif template=='Profile_editAll.html' :
     # if request.method=='POST':

        form=Profile_form(request.POST,request.FILES)
        if   form.is_valid():
                location=form.cleaned_data['location']
                Phone_number=form.cleaned_data['Phone_number']
                year_of_birth = form.cleaned_data['Year_of_birth']
                last_name = form.cleaned_data['Last_name']
                try:
                    
                    

            
                    obj=userprofile.objects.filter(user_id=my).update(first_name=request.user,email=request.user.email,location=location,
                         Phone_number=Phone_number,Year_of_birth=year_of_birth,Last_name=last_name,)
                    return redirect('pref:prefer')    #
                except Exception,e:
                    error='Please enter a valid phone number'+ str(e)
        
        else: 
      #return redirect('pref:prefer')  
        
    #else: 
            try:
               Instance=userprofile.objects.get(user_id=request.user.id).__dict__ 
               form=Profile_form(initial=Instance)
            except :pass    
    return render(request,template,locals())
    
    

def changePassword(request):
    form=ChangePasswordForm(request.POST)
    try: 
     if form.is_valid():
         adp=random.randrange(1,7)
         User_phone=form.cleaned_data['user_name']
         number = userprofile.objects.get(Phone_number = User_phone)
         User_name = number.first_name


         u=User.objects.get(username=User_name)
         password=str(User_name) + str(adp)
         u.set_password(password)
         u.save()
         first_name = u.username
         msg= str(User_name) + " " + "your password at affixmw.com is" + " " + password
         #username)
         phone=str(number.Phone_number)
         send=sendMessage(phone,msg)
         send.go()
         return redirect('/')
     else: pass
        
    except Exception,e:error="please enter the correct username" + str(e)
         

    return render(request,'passChange.html',locals())














