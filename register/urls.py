from django.conf.urls import url,include
from . import views

#
urlpatterns=[
url(r'^sign_up/', views.Sign_up_v,name='Sign_up'),
url(r'^profile/',views.profile,name='profile'),
url(r'^profile_edit/',views.Profile_edit,{'template':'Profile_edit.html'},name='profile_edit'),
url(r'^profile_editAll/',views.Profile_edit,{'template':'Profile_editAll.html'},name='profile_editAll'),
url(r'^resetpassword/',views.changePassword,name="reset")]
