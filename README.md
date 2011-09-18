Overview
========

Zebra is a set of webhook handlers, forms and widgets that make using Stripe with Django even easier.

It includes a sample view and template, and pull requests are quite welcome!

Status
======

In active dev this weekend ( Sept 19, 2011 ).  Probably don't use it in production until monday.  This message will go away when that's changed.


Usage
=====

## Installation ##

* pip install (from here, for the moment): 
	`pip install -e git://github.com/GoodCloud/django-zebra.git#egg=zebra`
* Add to `INSTALLED_APPS`
* Add `STRIPE_SECRET` and `STRIPE_PUBLISHABLE` to your `settings.py`
* Enjoy.



## Webhooks ##

Zebra provides handling of all the webhooks that stripe sends back, and calls a set of signals, so you can plug your app in as needed. To use the webhooks.

* Include the zebra urls
* Update your stripe account to point to your webhook URL (aka https://www.mysite.com/zebra/webhooks)
* Plug into any webhook signals you care about.  


Zebra provides:

* `zebra_webhook_recurring_payment_failed`
* `zebra_webhook_invoice_ready`
* `zebra_webhook_recurring_payment_succeeded`
* `zebra_webhook_subscription_trial_ending`
* `zebra_webhook_subscription_final_payment_attempt_failed`

All of the webhooks provide the same arguments:

* `customer` - the Customer object
* `full_json` - the full json response, parsed with simplejson.


So, for example, to update the customer's new billing date after a successful payment, you could:

```
from zebra.signals import zebra_webhook_recurring_payment_succeeded

def update_last_invoice_date(sender, **kwargs):
	c = Customer.objects.get(stripe_customer_id=kwargs["customer"])
	c.billing_date = kwargs["full_json"].date
	c.save()

zebra_webhook_recurring_payment_succeeded.connect(update_last_invoice_date)
```



## Forms ##

The StripePaymentForm sets up a form with fields like [the official stripe example](https://gist.github.com/1204718#file_stripe_tutorial_page.html).

In particular, the form is stripped of the name attribute for any of the credit card fields, to prevent accidental submission.

Use it in a view like so:

```
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

That's it - all the stripe tokeny goodness happens, and errors are displayed (roughly) to your users.


## Other Useful Bits ##

Zebra comes with a manage.py command to clear out all the test customers from your account.  To use it, run:

```
./manage.py clear_stripe_test_customers
```

It responds to `--verbosity=[0-3]`, like a lot of python scripts.


Credits
=======

I did not write any of stripe.  It just makes me happy to use, and inspired to make better APIs for my users.  For Stripe info, ask them: [stripe.com](http://stripe.com)

Code credits are in the AUTHORS file.   Pull requests welcome!


