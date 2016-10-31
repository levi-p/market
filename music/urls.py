from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^song/',views.musicView,name="music"),
    url(r'^songDownload/(?P<songId>[0-9]+)',views.songDownload,name="Download"),
    url(r'^songDownload/',views.songUpload,name="upload"),
    url(r'^songSearch/',views.searchSong,name="search"),
    ]
