from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^invoice', include('invoice.urls', namespace='invoice')),
    url(r'^projects/(?P<pk>\d+)/$', views.view_projects, name='view_projects'),
    url(r'^projects/items/(?P<pk>\d+)/$', views.view_items, name='view_items'),
]
