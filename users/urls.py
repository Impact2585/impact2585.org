from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
  url(r'^login/$', views.register, name='register')
 )