from django.shortcuts import render,redirect
from .models import music
from .forms import musicUploadForm
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def musicView(request):
    
    songList = music.objects.all()
    return render(request,'music.html',locals())

def songUpload(request):
    if request.method == 'POST':
        form = musicUploadForm(request.POST,request.FILES)
        if form.is_valid():
            artist=form.cleaned_data['Artist']
            title=form.cleaned_data['Title']
            song = form.cleaned_data['Song']

            msc=music(Title=title,Song=song,Artist=artist)
            msc.save()
            success='Success! add another song'
            form=musicUploadForm()
    else:form=musicUploadForm()
    return render(request,'songUpload.html',locals())

def songDownload(request,songId):
    d=music.objects.get(id=songId)
    filename = str(d.Song).strip('./')
    
    response = HttpResponse(d.Song, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename 
    return response

def searchSong(request):
    
    if request.method=='GET':
        g=9999
        qr=request.GET.get('q','popcaan')
        if qr!='':
            
            try:
                g=(Q(Title__icontains=qr)|
                   Q(Artist__icontains=qr))
                   #Q(Discription__icontains=qr))
                results = music.objects.filter(g)
                if list(results)==[]:
                    result2='No results found'
                
            except Exception,e: result2='No results found'+str(e)
    
    return render(request,'musicSearch.html',locals())

