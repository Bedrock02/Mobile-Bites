from django.conf.urls import patterns, url

urlpatterns = patterns(
    'location.views',
    url(r'^add/$',            'add'),
    url(r'^get/$',            'get'),
)