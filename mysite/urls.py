from django.conf.urls import patterns, url
from mysite import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^js$', views.js),
    url(r'^ajax$', views.ajax),
)
