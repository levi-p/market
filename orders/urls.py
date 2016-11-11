from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'orders/(?P<PD>[a-z]+)',views.orderView,name='order')
    ]
