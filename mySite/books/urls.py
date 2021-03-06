from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^all', views.database_access, name="database_access"),
    url(r'^about', views.about, name="about"),
    url(r'^personal$', views.personal, name='personal'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
