from django.conf import settings
from django.core.management.base import BaseCommand

import stripe

class Command(BaseCommand):
    help = "Clear all test mode customers from your stripe account."
    __test__ = False

    def handle(self, *args, **options):
        stripe.api_key = settings.STRIPE_SECRET
        print "Clearing stripe test customers..."
        for c in stripe.Customer.all():
            print "Deleting %s..." % (c.description),
            if not c.livemode:
                c.delete()
                print "done"
