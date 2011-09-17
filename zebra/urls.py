from django.conf.urls.defaults import *
from zebra import views

urlpatterns = patterns('',          
    url(r'^zebra-webhooks',     views.webhooks,          name='webhooks'),
)
