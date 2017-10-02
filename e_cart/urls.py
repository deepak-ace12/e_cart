from django.conf.urls import include, url
from django.contrib import admin
from e_cart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^company/', include('company.urls',  namespace='company')),
    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^invoice/', include('invoice.urls', namespace='invoice')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
