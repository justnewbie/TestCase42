from django.conf.urls import patterns, include, url
from django.contrib import admin

import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testingslow.views.home', name='home'),
    # url(r'^testingslow/', include('testingslow.foo.urls')),
    url(r'^manage/([1-9])', 'testapp.views.manage_p', name='manage_main_page'),
    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login_view'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}, name='logout_view'),
    url(r'^$', 'testapp.views.about_p', name='main_page'),
    url(r'^requests/([0-1])', 'testapp.views.list_request', name='http_loggs_list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True})
)
