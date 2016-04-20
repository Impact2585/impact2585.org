from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

from _Impact2585_org import views

urlpatterns = patterns('',
		url(r'^$', views.index),
		url(r'^media/', views.media),
		url(r'^robots/', views.robots),
		url(r'^aboutus/', views.aboutus),
		url(r'^sponsors/', views.sponsors),
    url(r'^admin/', include(admin.site.urls)),

)
