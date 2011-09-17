from django.db import models

from zebra import mixins
from zebra.conf import settings


class DatesModelBase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class StripeCustomer(models.Model, mixins.StripeCustomerMixin):
    _sync_stripe = True
    customer_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    

# Non abstract classes must be enabled in your project's settings.py
if settings.ZEBRA_ENABLE_APP:
    class Customer(StripeCustomer):
        pass

