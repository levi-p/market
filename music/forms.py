from django import forms
from .models import music

class musicUploadForm(forms.ModelForm):
    class Meta:
        model = music
        exclude=('date',)
