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
from zebra.forms import StripePaymentForm
from zebra.signals import *

stripe.api_key = settings.STRIPE_SECRET

# In a real implementation, do login required, etc.
def edit(request):
    user = request.user
    success_updating = False

    if request.method == 'POST':
        zebra_form = StripePaymentForm(request.POST)
        if zebra_form.is_valid():

            customer = stripe.Customer.retrieve(user.stripe_id)
            customer.card = zebra_form.cleaned_data['stripe_token']
            customer.save()

            profile = user.get_profile()
            profile.last_4_digits = zebra_form.cleaned_data['last_4_digits']
            profile.stripe_customer_id = customer.id
            profile.save()

            success_updating = True

    else:
        zebra_form = StripePaymentForm()

    return render_to_response('basic_update.html',
        {
          'zebra_form': zebra_form,
          'publishable': settings.STRIPE_PUBLISHABLE,
          'success_updating': success_updating,
        },
        context_instance=RequestContext(request)
    )



def webhooks(request):
    """Handles all known webhooks from stripe, and calls signals. Plug in as you need."""

    assert request.method == "POST"
    json = simplejson.loads(request.POST["json"])

    if json["event"] == "recurring_payment_failed":
        zebra_webhook_recurring_payment_failed.send(sender=None, customer=json["customer"], full_json=json)

    elif json["event"] == "invoice_ready":
        zebra_webhook_invoice_ready.send(sender=None, customer=json["customer"], full_json=json)

    elif json["event"] == "recurring_payment_succeeded":
        zebra_webhook_recurring_payment_succeeded.send(sender=None, customer=json["customer"], full_json=json)

    elif json["event"] == "subscription_trial_ending":
        zebra_webhook_subscription_trial_ending.send(sender=None, customer=json["customer"], full_json=json)

    elif json["event"] == "subscription_final_payment_attempt_failed":
        zebra_webhook_subscription_final_payment_attempt_failed.send(sender=None, customer=json["customer"], full_json=json)

    return HttpResponse(status=200)
    
