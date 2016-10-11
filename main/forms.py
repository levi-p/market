from django import forms
from .models import Product,Comment,SubCategory
from django.db import models


class Noti(forms.Form):
      Read=forms.CharField(initial='yes',widget=forms.TextInput(attrs={'value':'yes'}))


class ProductUploadForm(forms.ModelForm):

    class Meta:
        model=Product
        exclude=('seller','recommended','time','pic3','views','participants','is_sold')

        widgets={'Product_name':forms.TextInput(attrs={'style':'width:100%;color:gray;','value':'enter product name','onfocus':"if (this.value=='enter product name') this.value='';"}),'Discription':forms.Textarea(attrs={'style':'width:100%;height:20%'}),'category_name':forms.Select(attrs={'style':'width:100%'}),'Price':forms.TextInput(attrs={'style':'width:100%'})}

    def __init__(self, * args, ** kwargs):
        self.cc = kwargs.pop('cc', None)
        super(ProductUploadForm, self).__init__( * args, ** kwargs)
        self.fields['sub_c'].queryset =SubCategory.objects.filter(category_name__id=self.cc) #forms.ModelChoiceField()#queryset=Product.objects.filter(sub_c__name=''))



class ProductCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=('time','products')
