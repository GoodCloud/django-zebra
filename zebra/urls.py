from django.conf.urls.defaults import *

from zebra import views

urlpatterns = patterns('',
    url(r'webhooks/$',     views.webhooks,          name='webhooks'),
    url(r'webhooks2/$',     views.webhooks2,          name='webhooks2'),
)
