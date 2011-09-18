from django.conf.urls.defaults import *
from marty import views

urlpatterns = patterns('',          
    url(r'update$',     views.update,          name='update'),
)
