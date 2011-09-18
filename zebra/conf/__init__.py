from zebra.conf import defaults
from django.conf import settings as _settings
from django.conf import UserSettingsHolder

ush = UserSettingsHolder(_settings)
for attr in dir(defaults):
    if attr.upper().startswith('ZEBRA') or attr.upper().startswith('STRIPE'):
        if not hasattr(ush, attr):
            setattr(ush, attr, getattr(defaults, attr))
settings = ush