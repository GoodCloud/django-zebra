import datetime
REASONABLE_YEARS = range(datetime.date.today().year, datetime.date.today().year+40)
REASONABLE_YEAR_CHOICES = [(i,i) for i in REASONABLE_YEARS]

MAXIMUM_STRIPE_CUSTOMER_LIST_SIZE = 100