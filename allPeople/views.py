from django.shortcuts import render

# Create your views here.

from register.models import userprofile
from .models import Message,Followers
from .forms import sendMessageForm


def peopleOnSite(request):
    allP = userprofile.objects.all()
    return render(request,'people.html',locals())

def sendMessage(request,From,to):
    toSend=to
    if request.method=='POST':
        form = sendMessageForm(request.POST)
        if form.is_valid():
            From2=userprofile.objects.get(first_name__id=From)
            To2 = userprofile.objects.get(id=to)
            Message2 = form.cleaned_data['message']
            
            msg = Message(From=From2,To=To2,message=Message2)
            msg.save()
    else: form = sendMessageForm()
    tohp=to
        
    return render(request,'sendMsg.html',locals())

def followSomeOne(request):
    followerS=Followers.objects.filter(id=userToFollowId)
    if request.user not in followerS.followers:
        followerS.update(followers)

    return redirect('anthu:allPeople')

def viewSomeUser(request,userId):
    userView = userId
    profile = userprofile.objects.get(first_name__id=userView)

    return render(request,'anotherProfile.html',locals())
