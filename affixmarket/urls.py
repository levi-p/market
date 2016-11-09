"""affixmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import views
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^music/',include('music.urls', namespace='music')),
    url(r'order/',include('orders.urls' ,namespace='order')),
    url(r'^uploadWay', views.call,name='uploadWay'),
    url(r'^products/(?P<name_id>[0-9]+)/',views.categoryView,name='category_all'),
    url(r'^productsSub/(?P<sub_id>[0-9]+)/',views.subCategoryView,name='subCategory_all'),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^signUp/', include('register.urls', namespace='Sign_up')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^preference/', include('UserPreference.urls',namespace='pref')),
    url(r'^$',views.home,name="home"),
    
    url(r'^admin/', admin.site.urls),
    url(r'^people/', include('allPeople.urls',namespace='anthu')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})]
