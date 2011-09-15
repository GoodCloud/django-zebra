from datetime.date import today
REASONABLE_YEARS = range(today().year, today().year+40)
REASONABLE_YEAR_CHOICES = [(i,i) for i in REASONABLE_YEARS]