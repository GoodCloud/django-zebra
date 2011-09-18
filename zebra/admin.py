from django.contrib import admin

from zebra.conf import settings
from zebra.models import Customer, Subscription

if settings.ZEBRA_ENABLE_APP:
    admin.site.register(Customer)
    admin.site.register(Subscription)