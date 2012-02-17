from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('lists.views',
    url(r'^$', 'user_lists'),
    url(r'^(?P<user_name>[\w\s\d]+)/$', 'user_lists'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/$', 'view_list'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/add/(?P<new_item>[\w\s\d]+)$', 'add_item'),
    url(r'^(?P<user_name>[\w\s\d]+)/(?P<list_name>[\w\s\d]+)/remove/(?P<pk>[\w\s\d]+)$', 'remove_item'),
)
