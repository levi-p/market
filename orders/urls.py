from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'orders/(?P<PD>[0-9]+)',views.orderView,name='order')
    ]
