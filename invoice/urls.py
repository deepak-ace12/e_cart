from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^cart/(?P<pk>\d+)/$', views.view_invoice, name='view_invoice'),
    url(r'^bag/(?P<action>.+)/(?P<pk>\d+)/$', views.cart, name='cart'),
    url(r'^checkout/(?P<pk>\d+)/$', views.save_qty, name='checkout'),
    url(r'^pdf/(?P<pk>\d+)/$', views.generate_pdf, name='save_pdf'),
    url(r'^save/(?P<pk>\d+)/$', views.save_qty, name='save_qty'),
    url(r'^adjust/(?P<pk>\d+)/$', views.adjustment, name='adjust'),
]