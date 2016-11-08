from django.shortcuts import render,redirect

# Create your views here.

from register.models import userprofile
from .models import Message,Followers
from .forms import sendMessageForm
from django.contrib.auth.decorators import login_required


def peopleOnSite(request):
    allP = userprofile.objects.all()
    return render(request,'people.html',locals())
@login_required(redirect_field_name='login',login_url="Sign_up:log")
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
    message1 = Message.objects.filter(From__first_name__id=From).filter(To__id=to)
    message2 = Message.objects.filter(From__id=to).filter(To__first_name__id=From)

    messages1 = [x for x in message1 ]
    messages2 = [i for i in message2 ]
    messagesAll = messages1 + messages2
    
        
    return render(request,'sendMsg.html',locals())

def followSomeOne(request,userToFollowId):
    try:
        followp=Followers.objects.filter(userToFollow__id=userToFollowId)
        d1=str([x.followers for x in followp])

        if str(request.user) not in d1 :
            theyFeelme=[x.followers for x in follow]
            add=str(theyFeelme) + str(request.user)
        
            fobj=followp.update(followers=add)
            fobj.save()

    except:
        followthis=userprofile.objects.get(first_name__id=userToFollowId)
        j=Followers(userToFollow=followthis.first_name,followers=str(request.user))
        j.save()
        follow=Followers.objects.filter(userToFollow__id=userToFollowId)
        #d=str([x.followers for x in follow])
    
    return redirect('anthu:allPeople')
    #return render(request,'',locals())
@login_required(redirect_field_name='login',login_url="Sign_up:log")
def viewSomeUser(request,userId):
    userView = userId
    current=str(request.user)
    profile = userprofile.objects.get(id=userView)
    try:
        followinTrue =str( Followers.objects.get(userToFollow__id = profile.first_name.id).followers)
    
    except:
        followinTrue = []
    return render(request,'anotherProfile.html',locals())
