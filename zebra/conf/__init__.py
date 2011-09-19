from zebra.conf import defaults
from django.conf import settings as _settings
from django.conf import UserSettingsHolder

ush = UserSettingsHolder(_settings)
for attr in dir(defaults):
    if attr.upper().startswith('ZEBRA') or attr.upper().startswith('STRIPE'):
        if not hasattr(ush, attr):
            setattr(ush, attr, getattr(defaults, attr))


if not hasattr(ush, "ZEBRA_CUSTOMER_MODEL") and hasattr(ush, "ZEBRA_ENABLE_APP") and getattr(ush, "ZEBRA_ENABLE_APP"):
    setattr(ush, "ZEBRA_CUSTOMER_MODEL", "zebra.Customer")
settings = ush