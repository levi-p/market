from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'orders',views.orderView,name='order')
    ]
