from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^home/$', views.view_companies, name='view_companies'),
    url(r'^login/$', login, {'template_name': 'company/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'company/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]