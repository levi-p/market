from django import forms
from .models import Article_details,article_Comment

class articleForm(forms.ModelForm):
    class Meta:
        model =Article_details
        exclude =('time','Pic','A_pic','A_Name',)

        widgets={'Title':forms.TextInput(attrs={"style":"width:100%;background-color:white;border:1px solid grey"}),'Article':forms.Textarea(attrs={"style":"width:100%;background-color:white;border:1px solid grey;min-height:350px"}),}#'A_Name':forms.TextInput(attrs={"style":"width:100%;background-color:white;border:1px solid grey"})}

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model=article_Comment
        exclude=('time','article')
        widgets={'comment':forms.Textarea(attrs={"style":"width:100%;height:100px"}),}

