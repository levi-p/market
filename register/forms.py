from django import forms
from .models import Sign_up,userprofile
#

class Sign_up_form(forms.ModelForm):
    
    class Meta():
        



        model=Sign_up
        fields=('Name','enter_password','password')

        widgets={'Name':forms.TextInput(attrs={'style':'width:100%;color:gray;','value':'enter your first name','onfocus':"if (this.value=='enter your first name') this.value='';"}),
'enter_password':forms.PasswordInput(attrs={'style':'width:100%;'}),'password':forms.PasswordInput(attrs={'style':'width:100%;'}),'Email':forms.EmailInput()}

class Profile_form(forms.ModelForm):
      class Meta():
        



        model=userprofile
        exclude=('first_name','email','profile_pic','user_id')
