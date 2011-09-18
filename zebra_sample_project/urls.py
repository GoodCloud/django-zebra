from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'zebra/',   include('zebra.urls',  namespace="zebra",  app_name='zebra') ),
    url(r'',         include('marty.urls',  namespace="marty",  app_name='marty') ),
)
