from django.db import models

from zebra import mixins
from zebra.conf import settings


class DatesModelBase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class StripeCustomer(models.Model, mixins.StripeCustomerMixin):
    customer_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    
    @property
    def stripe_customer_id(self):
        return self.subscription_id


class StripeSubscription(models.Model, mixins.StripeSubscriptionMixin):
    subscription_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    
    @property
    def stripe_subscription_id(self):
        return self.subscription_id
    

# Non abstract classes must be enabled in your project's settings.py
if settings.ZEBRA_ENABLE_APP:
    class Customer(DatesModelBase, StripeCustomer):
        pass

