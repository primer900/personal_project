__author__ = 'chrispro'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<movie_id>[0-9]+)/review/$', views.review, name='review'),
]
