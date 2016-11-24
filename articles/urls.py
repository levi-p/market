from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/',views.art_list, name='list'),
    url(r'^article/(?P<article_id>[0-9]+)',views.Article_view, name='article'),
    url(r'^write/',views.writeArticle,name="write")
]
