from django.conf.urls import url,include
from . import views

#
urlpatterns=[
url(r'^signUp/', views.Sign_up_v,name='Sign_up'),
url(r'^Login/', views.signIn,name='log'),
url(r'^profile/',views.profile,name='profile'),
url(r'^profileEdit/',views.Profile_edit,{'template':'Profile_edit.html'},name='profile_edit'),
url(r'^profileEditAll/',views.Profile_edit,{'template':'Profile_editAll.html'},name='profile_editAll'),
url(r'^resetpassword/',views.changePassword,name="reset")]
