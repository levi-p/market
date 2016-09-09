from django import forms
from .models import Product


class ProductUploadForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=('seller','recommended','time','pic3')

        widgets={'Product_name':forms.TextInput(attrs={'style':'width:100%'}),'Discription':forms.Textarea(attrs={'style':'width:100%;height:20%'}),'category_name':forms.Select(attrs={'style':'width:100%'}),'Price':forms.TextInput(attrs={'style':'width:100%'})}
