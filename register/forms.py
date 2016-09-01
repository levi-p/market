from django import forms
from .models import Sign_up,userprofile
#

class Sign_up_form(forms.ModelForm):
    
    class Meta():
        



        model=Sign_up
        fields=('Name','enter_password','password')

        widgets={'enter_password':forms.PasswordInput(attrs={}),'password':forms.PasswordInput(attrs={}),'Email':forms.EmailInput()}

class Profile_form(forms.ModelForm):
      class Meta():
        



        model=userprofile
        exclude=('first_name','email','profile_pic')
