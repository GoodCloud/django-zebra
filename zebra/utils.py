from zebra.conf import settings

AUDIT_RESULTS = settings.ZEBRA_AUDIT_RESULTS

def audit_customer_subscription(customer):
    """
    Audits the provided customer's subscription against stripe and returns a pair
    that contains a boolean and a result type.
    
    Default result types can be found in zebra.conf.defaults and can be
    overridden in your project's settings.
    """
    if (hasattr(customer, 'suspended') and customer.suspended):
        result = (False, AUDIT_RESULTS['suspended'])
    else:
        if hasattr(customer, 'subscription') and customer.subscription.status == 'active':
            result = (True, AUDIT_RESULTS['active'])
        else:
            result = (False, AUDIT_RESULTS['inactive'])
    return result