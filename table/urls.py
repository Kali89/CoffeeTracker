from django.conf.urls import patterns, url

from table import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^hello/$', views.table, name='table'),
            )
