from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^product/(?P<Pk>[0-9]+)/', views.ProductView,name='product_details'),
    url(r'^Uploadproduct/(?P<Pk>[0-9]+)/',views.ProductUpload,name="ProductUpload"),
    url(r'^notifications/',views.notify,name="notify"),
]
