from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^truck/', include('truck.urls')),
    url(r'^location/', include('location.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
