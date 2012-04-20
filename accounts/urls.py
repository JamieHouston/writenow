from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
    url(r'^login/',
        'login_user',
        name='login_user'
    ),
    url(r'^register/',
        'create_user',
        name='register_user'
    )
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^logout/$',
        'logout', {'next_page': '/'},
        name='logout'),
    url(r'^password_change/$',
        'password_change',
        name='password_change'),
    url(r'^password_change/done/$',
        'password_change_done',
        name='password_change_done'),
    )
