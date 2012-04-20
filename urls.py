from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/32.ico'}),
    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('lists.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^l/', include('lists.urls')),
#    url(r'^register/$', 'accounts.views.register', name="register"),
    )
