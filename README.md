Overview
========

Zebra is a library that makes using Stripe with Django even easier.

It's made of:

* `zebra`, the core library, with forms, webhook handlers, abstract models, mixins, signals, and templatetags that cover most stripe implementations.
* `marty`, an example app for how to integrate zebra, that also serves as its test suite.

Pull requests are quite welcome!


Usage
=====

## Installation ##

1. `pip install django-zebra`

2. Edit your `settings.py:`

	```
	INSTALLED_APPS += ("zebra",)
	STRIPE_SECRET = "YOUR-SECRET-API-KEY"
	STRIPE_PUBLISHABLE = "YOUR-PUBLISHABLE-API-KEY"
    # Set any optional settings (below)
    ```

3. (optional) `./manage.py syncdb` if you have `ZEBRA_ENABLE_APP = True`

4. (optional) Add in the webhook urls:

	```
	urlpatterns += patterns('',          
		url(r'zebra/',   include('zebra.urls',  namespace="zebra",  app_name='zebra') ),
	)
	```

5. Enjoy easy billing.


### Optional Settings:

* `ZEBRA_ENABLE_APP` 
	Defaults to `False`.  Enables Customer, Plan, and Subscription django models, as a part of zebra.
* `ZEBRA_CUSTOMER_MODEL` 
	The app+model string for the model that implements the StripeCustomerMixin. ie `"myapp.MyCustomer"`.  If `ZEBRA_ENABLE_APP` is true, defaults to `"zebra.Customer"`. 
* `ZEBRA_AUTO_CREATE_STRIPE_CUSTOMERS` 
	Defaults to `True`.  Automatically creates a stripe customer object on stripe_customer access, if one doesn't exist.


## Webhooks ##

Zebra handles all the webhooks that stripe sends back and calls a set of signals that you can plug your app into.  To use the webhooks:

* Include the zebra urls
* Update your stripe account to point to your webhook URL (aka https://www.mysite.com/zebra/webhooks)
* Plug into any webhook signals you care about.  

**Note: The initial Stripe webhook system is being deprecated. See below for a description of Zebra's support for the new system.**

Zebra provides:

* `zebra_webhook_recurring_payment_failed`
* `zebra_webhook_invoice_ready`
* `zebra_webhook_recurring_payment_succeeded`
* `zebra_webhook_subscription_trial_ending`
* `zebra_webhook_subscription_final_payment_attempt_failed`

All of the webhooks provide the same arguments:

* `customer` - if `ZEBRA_CUSTOMER_MODEL` is set, returns an instance that matches the `stripe_customer_id`, or `None`.  If `ZEBRA_CUSTOMER_MODEL` is not set, returns `None`.
* `full_json` - the full json response, parsed with simplejson.


So, for example, to update the customer's new billing date after a successful payment, you could:

(assuming you've set `ZEBRA_CUSTOMER_MODEL` or are using `ZEBRA_ENABLE_APP`):

```
from zebra.signals import zebra_webhook_recurring_payment_succeeded

def update_last_invoice_date(sender, **kwargs):
	customer = kwargs.pop("customer", None)
	full_json = kwargs.pop("full_json", None)
	customer.billing_date = full_json.date
	customer.save()

zebra_webhook_recurring_payment_succeeded.connect(update_last_invoice_date)
```

### Webhooks Update ###

Stripe recently updated their webhook implementation (see https://stripe.com/blog/webhooks). Zebra includes an implementation of the new system.

* Include the zebra urls
* Update your stripe account to point to your webhook URL (aka https://www.mysite.com/zebra/webhooks/v2/)
* Plug into any webhook signals you care about.  

Zebra provides:

* `zebra_webhook_charge_succeeded`
* `zebra_webhook_charge_failed`
* `zebra_webhook_charge_refunded`
* `zebra_webhook_charge_disputed`
* `zebra_webhook_customer_created`
* `zebra_webhook_customer_updated`
* `zebra_webhook_customer_deleted`
* `zebra_webhook_customer_subscription_created`
* `zebra_webhook_customer_subscription_updated`
* `zebra_webhook_customer_subscription_deleted`
* `zebra_webhook_customer_subscription_trial_will_end`
* `zebra_webhook_customer_discount_created`
* `zebra_webhook_customer_discount_updated`
* `zebra_webhook_customer_discount_deleted`
* `zebra_webhook_invoice_created`
* `zebra_webhook_invoice_updated`
* `zebra_webhook_invoice_payment_succeeded`
* `zebra_webhook_invoice_payment_failed`
* `zebra_webhook_invoiceitem_created`
* `zebra_webhook_invoiceitem_updated`
* `zebra_webhook_invoiceitem_deleted`
* `zebra_webhook_plan_created`
* `zebra_webhook_plan_updated`
* `zebra_webhook_plan_deleted`
* `zebra_webhook_coupon_created`
* `zebra_webhook_coupon_updated`
* `zebra_webhook_coupon_deleted`
* `zebra_webhook_transfer_created`
* `zebra_webhook_transfer_failed`
* `zebra_webhook_ping`

Zebra also provides an easy map of all the signals as `zebra.signals.WEBHOOK_MAP`, which maps events (`charge_succeeded`) to the Zebra signal (`zebra_webhook_charge_succeeded`). To assign a handler to all the signals that zebra sends, for example, loop over the items in the map:

    for event_key, webhook_signal in WEBHOOK_MAP.iteritems():
        webhook_signal.connect(webhook_logger)


## Forms ##

The StripePaymentForm sets up a form with fields like [the official stripe example](https://gist.github.com/1204718#file_stripe_tutorial_page.html).

In particular, the form is stripped of the name attribute for any of the credit card fields, to prevent accidental submission. Media is also provided to set up stripe.js (it assumes you have jQuery).

Use it in a view like so:

```
if request.method == 'POST':
    zebra_form = StripePaymentForm(request.POST)
    if zebra_form.is_valid():
    	my_profile = request.user.get_profile()
        stripe_customer = stripe.Customer.retrieve(my_profile.stripe_customer_id)
        stripe_customer.card = zebra_form.cleaned_data['stripe_token']
        stripe_customer.save()

        my_profile.last_4_digits = zebra_form.cleaned_data['last_4_digits']
        my_profile.stripe_customer_id = stripe_customer.id
        my_profile.save()

        # Do something kind for the user

else:
    zebra_form = StripePaymentForm()
```

## Template Tags ##

There are a couple of template tags that take care of setting up the stripe env, and rendering a basic cc update form.  Note that it's expected your `StripePaymentForm` is called either `zebra_form` or `form`.

To use in a template:

```
{% extends "base.html" %}{% load zebra_tags %}

{% block head %}{{block.super}}
	{% zebra_head_and_stripe_key %}
{% endblock %}

{% block content %}
	{% zebra_card_form %}
{% endblock %}

```

That's it - all the stripe tokeny goodness happens, and errors are displayed to your users.

## Models and Mixins ##

Model and Mixin docs coming.  For now, the code is pretty self-explanatory, and decently documented inline.


## Other Useful Bits ##

Zebra comes with a manage.py command to clear out all the test customers from your account.  To use it, run:

```
./manage.py clear_stripe_test_customers
```

It responds to `--verbosity=[0-3]`.


Credits
=======

I did not write any of stripe.  It just makes me happy to use, and inspired to make better APIs for my users.  For Stripe info, ask them: [stripe.com](http://stripe.com)

Code credits are in the AUTHORS file.   Pull requests welcome!


