from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testingslow.views.home', name='home'),
    # url(r'^testingslow/', include('testingslow.foo.urls')),
    url(r'^$', 'testapp.views.about_p', name='Main_Page'),
    url(r'^hooks/', 'testapp.views.list_hooks', name='http_loggs_list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True})
)
