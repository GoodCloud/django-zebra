from django.db import models

from zebra import mixins
from zebra.conf import settings


class DatesModelBase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class StripeCustomer(models.Model, mixins.StripeCustomerMixin):
    stripe_customer_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True


class StripePlan(models.Model, mixins.StripePlanMixin):
    stripe_plan_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    

# Non-abstract classes must be enabled in your project's settings.py
if settings.ZEBRA_ENABLE_APP:
    class Customer(DatesModelBase, StripeCustomer):
        pass
    
    class Plan(DatesModelBase, StripePlan):
        pass
    
    class Subscription(DatesModelBase, mixins.StripeSubscriptionMixin):
        customer = models.ForeignKey(Customer)
        plan = models.ForeignKey(Plan)
        
        @property
        def stripe_customer(self):
            return self.customer.stripe_customer

