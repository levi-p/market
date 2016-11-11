from django import forms
from .models import order

class orderForm(forms.ModelForm):
    class Meta:
        model=order
        exclude=('email','time','product_name')

        widgets={'phoneNumber':forms.TextInput(attrs={'style':'width:90%',}),'Name':forms.TextInput(attrs={'style':'width:90%',}),}
