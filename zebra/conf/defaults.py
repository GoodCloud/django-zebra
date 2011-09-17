"""
Defualt settings for zebra
"""
import datetime
import os

STRIPE_API_KEY = os.environ['STRIPE_API_KEY']
ZEBRA_ENABLE_APP = False
ZEBRA_TODAY = datetime.date.today()
ZEBRA_CARD_YEARS = range(ZEBRA_TODAY.year, ZEBRA_TODAY.year+10)
ZEBRA_CARD_YEARS_CHOICES = [(i,i) for i in ZEBRA_CARD_YEARS]

ZEBRA_MAXIMUM_STRIPE_CUSTOMER_LIST_SIZE = 100
