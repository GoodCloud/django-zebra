from zebra.conf import defaults
from django.conf import settings

for attr in dir(defaults):
    if not hasattr(settings, attr):
        setattr(settings, attr, getattr(defaults, attr))
