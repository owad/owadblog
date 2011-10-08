from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('article.urls')),
    url(r'^article/', include('comment.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='accounts_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='accounts_logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
