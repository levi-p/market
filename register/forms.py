from django import forms
from .models import Sign_up,userprofile
#

class loginForm(forms.Form):
    Phone_number = forms.CharField(required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={"type":"password"}),required=True)

class Sign_up_form(forms.ModelForm):
    class Meta():
        model=Sign_up
        fields=('First_name','enter_password','password')

        widgets={'Name':forms.TextInput(attrs={'style':'width:100%;color:gray;','value':'enter your first name','onfocus':"if (this.value=='enter your first name') this.value='';"}),
'enter_password':forms.PasswordInput(attrs={'style':'width:100%;'}),'password':forms.PasswordInput(attrs={'style':'width:100%;'}),'Email':forms.EmailInput()}

class Profile_form(forms.ModelForm):
      class Meta():
        



        model=userprofile
        exclude=('first_name','profile_pic','user_id')

        widgets={'Year_of_birth':forms.TextInput(attrs={'style':'width:22%;color:;borhder:1px solid gray;','value':'e.g 1990','onfocus':"if (this.value=='e.g 1990') this.value='';"}),
                'Last_name':forms.TextInput(attrs={'style':'width:100%;','value':'','onfocus':"if (this.value=='e.g 1990') this.value='';"}),
                'email':forms.TextInput(attrs={'style':'width:100%;color:;','onfocus':"if (this.value=='e.g 1990') this.value='';"}),
                'location':forms.TextInput(attrs={'style':'width:100%;color:;','value':'','onfocus':"if (this.value=='e.g 1990') this.value='';"}),
                'Phone_number':forms.TextInput(attrs={'style':'width:100%;color:;','value':'','onfocus':"if (this.value=='e.g 1990') this.value='';"}),
                 }

class ChangePasswordForm(forms.Form):
    user_name=forms.CharField()
