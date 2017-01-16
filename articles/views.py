from django.shortcuts import render,redirect
from .models import Comments,Article_details,article_Comment
from .forms import articleForm,ArticleCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def art_list(request,template):
    page = request.GET.get('page')
    P_list=Article_details.objects.filter(public=1)
    myP_list=Article_details.objects.filter(A_Name=str(request.user))
    paginator = Paginator(P_list,5)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
# If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
# If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
        
    return render(request,template,locals())




def Article_view(request,article_id):
    artic = Article_details.objects.get(pk=article_id)
    #html_article= html_format(artic.Article)
    h=article_Comment.objects.filter(article=artic)
    
    if request.method=='POST':
        form=ArticleCommentForm(request.POST)#,sub_c='Electronics')
        
        if form.is_valid():
            Name=form.cleaned_data['Name']
            comment=form.cleaned_data['comment']
            
        
            if request.user.is_authenticated():
                comm=article_Comment(Name=request.user,comment=comment,article=artic)
                comm.save()
                form=ArticleCommentForm()
                #return redirect('/')
            else:
            
                comm=article_Comment(Name=Name,comment=comment,article=artic)
                comm.save()
                form=ProductCommentForm()
                
            #reset all reads to include only poster
            #Comment.objects.filter(products=product.id).update(read=str(request.user))
    else: 
        form=ArticleCommentForm() 
        

        
    return render(request,'articles.html',locals())

def writeArticle(request):

    if request.method=='POST':
        author=Article_details(A_Name=str(request.user))
        form=articleForm(request.POST,instance=author)
        
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else: form=articleForm()


    return render(request,'writeArticle.html',locals())
