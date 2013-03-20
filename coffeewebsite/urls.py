from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^table/', include('table.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
##if not settings.DEBUG:
##    urlpatterns += patterns('',
##        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
##    )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
