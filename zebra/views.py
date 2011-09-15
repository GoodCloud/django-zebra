from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import stripe

from zebra.forms import StripePaymentForm

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

