from django import forms
from .models import Article_details

class articleForm(forms.ModelForm):
    class Meta:
        model =Article_details
        exclude =('time','Pic','A_pic')

        widgets={'Title':forms.TextInput(attrs={"style":"width:100%"}),'Article':forms.Textarea(attrs={"style":"width:100%"}),'A_Name':forms.TextInput(attrs={"style":"width:100%"})}

