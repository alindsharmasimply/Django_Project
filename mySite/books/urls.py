from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about', views.about, name="about"),
    url(r'^personal$', views.personal, name='personal'),
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
]
