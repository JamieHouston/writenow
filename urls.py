from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'writenow.views.home', name='home'),
    # url(r'^writenow/', include('writenow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^l/(?P<list_name>[a-z]+)/$', 'lists.views.view_list'),
    url(r'^l/(?P<list_name>[a-z]+)/add/(?P<new_item>[a-z]+)$', 'lists.views.add_item'),
)
