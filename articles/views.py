from django.shortcuts import render,redirect
from .models import Comments,Article_details
from .forms import articleForm


# Create your views here.

def art_list(request):
    P_list=Article_details.objects.all()
    return render(request,'post_list.html',locals())

def Article_view(request,article_id):
    artic = Article_details.objects.get(pk=article_id)
    #html_article= html_format(artic.Article)
    return render(request,'articles.html',locals())

def writeArticle(request):

    if request.method=='POST':
        form=articleForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else: form=articleForm()


    return render(request,'writeArticle.html',locals())
