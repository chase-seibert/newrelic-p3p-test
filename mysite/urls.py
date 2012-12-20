from django.conf.urls import patterns, url
from mysite import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^42/eum/rum.js$', views.rum),
    url(r'^1/2d8ca8bf04$', views.beacon),
)
