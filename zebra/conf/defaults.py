"""
Default settings for zebra
"""
import datetime
import os


try:
    STRIPE_PUBLISHABLE = os.environ['STRIPE_PUBLISHABLE']
except KeyError:
    STRIPE_PUBLISHABLE = ''

try:
    STRIPE_SECRET = os.environ['STRIPE_SECRET']
except KeyError:
    STRIPE_SECRET = ''

ZEBRA_ENABLE_APP = False

ZEBRA_TODAY = datetime.date.today()
ZEBRA_CARD_YEARS = range(ZEBRA_TODAY.year, ZEBRA_TODAY.year+12)
ZEBRA_CARD_YEARS_CHOICES = [(i,i) for i in ZEBRA_CARD_YEARS]

ZEBRA_MAXIMUM_STRIPE_CUSTOMER_LIST_SIZE = 100

ZEBRA_AUDIT_RESULTS = {
    'active': 'active',
    'no_subscription': 'no_subscription',
    'past_due': 'past_due',
    'suspended': 'suspended',
    'trialing': 'trialing',
    'unpaid': 'unpaid',
    'cancelled': 'cancelled'
}

ZEBRA_ACTIVE_STATUSES = ('active', 'past_due', 'trialing')
ZEBRA_INACTIVE_STATUSES = ('cancelled', 'suspended', 'unpaid', 'no_subscription')
