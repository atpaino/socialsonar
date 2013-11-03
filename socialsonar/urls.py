from django.conf.urls import patterns, include, url
from socialsonar import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'socialsonar.views.home', name='home'),
    url(r'^ping/latitude=([^&]+)\&longitude=(.+)$', 'socialsonar.views.ping', name='home'),
    # url(r'^socialsonar/', include('socialsonar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
