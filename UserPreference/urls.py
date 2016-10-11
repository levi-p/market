from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^preference',views.Prefer,name="prefer"),
               ]
