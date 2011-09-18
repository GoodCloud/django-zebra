from django.db import models

from zebra import mixins
from zebra.conf import settings


class DatesModelBase(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class StripeCustomer(models.Model, mixins.StripeMixin, mixins.StripeCustomerMixin):
    stripe_customer_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True


class StripePlan(models.Model, mixins.StripeMixin, mixins.StripePlanMixin):
    stripe_plan_id = models.CharField(max_length=50)
    
    class Meta:
        abstract = True


class StripeSubscription(models.Model, mixins.StripeMixin, mixins.StripeSubscriptionMixin):
    """
    You need to provide a stripe_customer attribute. See zebra.models for an
    example implimentation.
    """
    class Meta:
        abstract = True
    

# Non-abstract classes must be enabled in your project's settings.py
if settings.ZEBRA_ENABLE_APP:
    class Customer(DatesModelBase, StripeCustomer):
        def __unicode__(self):
            return self.stripe_customer_id
    
    class Plan(DatesModelBase, StripePlan):
        def __unicode__(self):
            return self.stripe_plan_id
    
    class Subscription(DatesModelBase, StripeSubscription):
        customer = models.ForeignKey(Customer)
        plan = models.ForeignKey(Plan)
        
        def __unicode__(self):
            return "%s: %s" % (self.customer, self.plan)
        
        @property
        def stripe_customer(self):
            return self.customer.stripe_customer

