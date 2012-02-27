from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^', include('lists.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^l/', include('lists.urls')),
#    url(r'^register/$', 'accounts.views.register', name="register"),
#    url(r'^accounts/', include('accounts.urls')),
)
