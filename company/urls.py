from django.conf.urls import url, include
from . import views as company_views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^home/$', company_views.view_companies, name='view_companies'),
    url(r'^login/$', login, {'template_name': 'company/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'company/logout.html'}, name='logout'),

]