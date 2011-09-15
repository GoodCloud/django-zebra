Overview
========

Zebra aims to be a simple set of django helper forms and widgets that make handling Stripe credit cards even easier.

It includes a sample view and template, and pull requests are quite welcome!


Usage
=====

## Installation ##

* pip install (from here, for the moment: `pip install -e git://git@github.com:GoodCloud/django-zebra.git#egg=zebra` )
* Add to `INSTALLED_APPS`
* Enjoy.


## Forms ##

The StripePaymentForm sets up a form like [this one](https://gist.github.com/1204718#file_stripe_tutorial_page.html).

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


Credits
=======

I did not write any of stripe.  It just makes me happy to use, and inspired to make better APIs for my users.  For Stripe info, ask them: [stripe.com](http://stripe.com)

Initial coding by Steven Skoczen of [GoodCloud](http://www.agoodcloud.com).  Pull requests welcome!


