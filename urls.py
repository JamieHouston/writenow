from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('lists.views',
    # Examples:
    # url(r'^$', 'writenow.views.home', name='home'),
    # url(r'^writenow/', include('writenow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^l/$', 'user_lists'),
    url(r'^l/(?P<list_name>[\w\s\d]+)/$', 'view_list'),
    url(r'^l/(?P<list_name>[\w\s\d]+)/add/(?P<new_item>[\w\s\d]+)$', 'add_item'),
    url(r'^accounts/', include('login.urls')),
)
