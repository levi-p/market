from django import forms
from .models import Message

class sendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('date','From','To')
