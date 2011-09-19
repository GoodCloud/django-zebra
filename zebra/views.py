from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
try:
    import simplejson
except:
    from django.utils import simplejson

from zebra.conf import settings
import stripe
from zebra.signals import *
from django.db.models import get_model


stripe.api_key = settings.STRIPE_SECRET

def _try_to_get_customer_from_customer_id(stripe_customer_id):
    if hasattr(settings, "ZEBRA_CUSTOMER_MODEL"):
        m = get_model(*settings.ZEBRA_CUSTOMER_MODEL.split('.'))
        try:
            return m.objects.get(stripe_customer_id=stripe_customer_id)
        except:
            pass
    return None


def webhooks(request):
    """Handles all known webhooks from stripe, and calls signals. Plug in as you need."""

    assert request.method == "POST"
    json = simplejson.loads(request.POST["json"])

    if json["event"] == "recurring_payment_failed":
        zebra_webhook_recurring_payment_failed.send(sender=None, customer=_try_to_get_customer_from_customer_id(json["customer"]), full_json=json)

    elif json["event"] == "invoice_ready":
        zebra_webhook_invoice_ready.send(sender=None, customer=_try_to_get_customer_from_customer_id(json["customer"]), full_json=json)

    elif json["event"] == "recurring_payment_succeeded":
        zebra_webhook_recurring_payment_succeeded.send(sender=None, customer=_try_to_get_customer_from_customer_id(json["customer"]), full_json=json)

    elif json["event"] == "subscription_trial_ending":
        zebra_webhook_subscription_trial_ending.send(sender=None, customer=_try_to_get_customer_from_customer_id(json["customer"]), full_json=json)

    elif json["event"] == "subscription_final_payment_attempt_failed":
        zebra_webhook_subscription_final_payment_attempt_failed.send(sender=None, customer=_try_to_get_customer_from_customer_id(json["customer"]), full_json=json)
    
    else:
        return HttpResponse(status=400)

    return HttpResponse(status=200)
    
