"""
Defualt settings for zebra
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
ZEBRA_CARD_YEARS = range(ZEBRA_TODAY.year, ZEBRA_TODAY.year+10)
ZEBRA_CARD_YEARS_CHOICES = [(i,i) for i in ZEBRA_CARD_YEARS]

ZEBRA_MAXIMUM_STRIPE_CUSTOMER_LIST_SIZE = 100

ZEBRA_AUDIT_RESULTS = {
    'active': (True, 'active'),
    'no_subscription': (False, 'no_subscription'),
    'past_due': (True, 'past_due'),
    'suspended': (False, 'suspended'),
    'trialing': (True, 'trialing'),
    'unpaid': (False, 'cancelled')
}
