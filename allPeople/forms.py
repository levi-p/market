from django import forms
from .models import Message

class sendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('date','From','To')

        widgets = {'message':forms.Textarea(attrs={"style":"background-color:white;height:70px",}),}
