from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^cart/$', views.view_invoice, name='view_invoice'),
    url(r'^bag/(?P<action>.+)/(?P<pk>\d+)/$', views.cart, name='cart'),
    url(r'^checkout/(?P<pk>\d+)/$', views.checkout, name='checkout'),
    url(r'^pdf/$', views.generate_pdf, name='save_pdf'),
]