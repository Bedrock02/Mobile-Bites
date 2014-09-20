from django.conf.urls import patterns, url

urlpatterns = patterns(
    'truck.views',
    url(r'^add/$',            'add'),
    url(r'^get/$',            'get'),
)