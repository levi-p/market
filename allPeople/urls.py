from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^users/',views.peopleOnSite,name='allPeople'),
    url(r'^message/(?P<From>[0-9]+)/(?P<to>[0-9]+)',views.sendMessage, name = 'msg'),
    url(r'^profileView/(?P<userId>[0-9]+)/',views.viewSomeUser, name = 'ona'),
    url(r'^anotherprofileView/(?P<userToFollowId>[0-9]+)/',views.followSomeOne, name = 'follow'),
      ]
