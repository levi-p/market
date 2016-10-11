from django import forms
from .models import Preference
from main.models import Category

class preferenceForm(forms.ModelForm):
      
      class Meta:
          pref=Category.objects.all()
          prefb=[(x,x) for x in pref]
          model=Preference
          exclude=('use_r',)
          widgets={'I_like':forms.CheckboxSelectMultiple(choices=prefb)}

      def __init__(self, *args,**kwargs):
          
          super(preferenceForm,self).__init__( * args,**kwargs)
          self.fields['I_like'].querset=(('ffff','tttt'),('k','ttlljkt'))#pref
          
