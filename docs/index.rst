.. django-zebra documentation master file, created by
   sphinx-quickstart on Thu Feb 16 22:57:53 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-zebra
============

Zebra is a library that makes using Stripe_ with Django_ even easier.

Please report errors and omissions at
https://github.com/GoodCloud/django-zebra/issues

django-zebra contains two components:

- ``zebra`` which is the core library providing forms, webhook handlers,
  abstract models, mixins, signals, and template tags that cover most of
  the Stripe functionality for many implementations.
- ``marty`` which is an example app that integrates django-zebra and provides
  a test suite.

.. _Django: http://www.djangoproject.com/
.. _Stripe: http://www.stripe.com/


Installation
============

**Install django-zebra**::

    pip install django-zebra


**Edit your Django settings**::

    INSTALLED_APPS += ('zebra',)
    STRIPE_SECRET = "YOUR-SECRET-API-KEY"
    STRIPE_PUBLISHABLE = "YOUR-PUBLISHABLE-API-KEY"


**Enable optional settings**

See :doc:`zebra/configuration` for settings available.


**Enable Webhook URLs**

This is optional and only if you wish to use zebra's webhook signals.

::

  urlpatterns += patterns('',          
    url(r'zebra/', include('zebra.urls', namespace="zebra", app_name='zebra')),
  )


Quick Start
===========

By default, adding zebra to your installed apps will not provide any
functionality beyond the webhooks *if* you enable the url pattern.

The library was designed to be as flexible as possible so it doesn't step on
your toes or get in your way.

So following along from the installation above you'll discover that running
``syncdb`` has no affect. At this point you have 2 options:

- Use the mixins and abstract base classes to extend your own models
- Enable the default application (models & admin)

Customizing your existing application with ABCs and mixins
--------------------------------------------------------------

If you already have an existing model for customers you can still use the
default zebra application and simply provide your model class (see the next
section).

If you want to forego using the default application you can find all the
documentation on this site and in the source code which can be viewed in the
`GitHub repo`_.

The easiest way to get started is to extend one of the base classes provided.

Check out :doc:`zebra/mixins` for a list of all the mixins that come with the
zebra library. The :doc:`tutorial` also goes into detail on mixing zebra with
an existing application.


Enabling the default application
--------------------------------

To enable the default application simply edit your projects settings and
include::

    ZEBRA_ENABLE_APP = True

Then run ``syncdb`` to install the models.

You should now find the zebra application listed in the admin with three default
models:

- Customers
- Plans
- Subscriptions

If you already have a model that you want to use for customers simply
add the following setting::

    ZEBRA_CUSTOMER_MODEL = 'your_app.YourCustomerModel'

Then in your models file simply update your model in inherit from
``zebra.models.StripeCustomer`` abstract base class::

    from zebra.models import StripeCustomer
    
    class YourCustomerModel(StripeCustomer):
        ...

Now ``YourCustomerModel`` will have 2 new attributes, ``stripe`` and
``stripe_customer`` along with a new field, stripe_customer_id. If you've
decided to go this route, simply replace ``zebra.models.Customer`` with
``your_app.models.YourCustomerModel`` in the examples below.

By defualt ``ZEBRA_AUTO_CREATE_STRIPE_CUSTOMERS`` is ``True`` so creating new
customers is a breeze by simply using the mixed-in helper. Simply instantiate
your customer class and access the ``stripe_customer`` attribute.

    >>> import zebra
    >>> c = zebra.models.Customer()
    >>> c.stripe_customer_id
    >>> c.id
    >>> c.stripe_customer
    <Customer customer id=cus_A0FULkVQwzwlUz at 0x101b2d7d0> JSON: {
      "account_balance": 0, 
      "created": 1329775998, 
      "id": "cus_A0FULkVQwzwlUz", 
      "livemode": false, 
      "object": "customer"
    }
    >>> c.id
    1
    >>> c.stripe_customer_id
    u'cus_A0FULkVQwzwlUz'

As you can see in the example above, with the default customer model there is
only 1 field so once the model is in a savable state (all required fields
containing valid values) simply calling ``c.stripe_customer`` created a new
customer within Stripe, updated the instance with the newly created customer ID
and returned the Stripe API customer instance.

Let's charge our new customer $10.

First we must give our customer a credit card::

    >>> card = {
    ... 'number': '4242424242424242',
    ... 'exp_month': '03',
    ... 'exp_year': '2013',
    ... 'cvc': '123',
    ... 'name': 'John Doe'
    ... }
    >>> stripe_cust = c.stripe_customer
    >>> stripe_cust.card = card
    >>> stripe_cust.save()
    <Customer customer id=cus_A0FULkVQwzwlUz at 0x101b2d7d0> JSON: {
      "account_balance": 0, 
      "active_card": {
        "country": "US", 
        "cvc_check": "pass", 
        "exp_month": 3, 
        "exp_year": 2013, 
        "last4": "4242", 
        "name": "John Doe", 
        "object": "card", 
        "type": "Visa"
      }, 
      "created": 1329775998, 
      "id": "cus_A0FULkVQwzwlUz", 
      "livemode": false, 
      "object": "customer"
    }

Now we can charge John $10 for that pizza we split::

    >>> stripe.Charge.create(
    ... amount=1000,
    ... currency='usd',
    ... customer=c.stripe_customer_id,
    ... description='the money you owed me for the pizza'
    ... )
    <Charge charge id=ch_lCSjHD3hAxXcjO at 0x101e0ff10> JSON: {
      "amount": 1000, 
      "card": {
        "country": "US", 
        "cvc_check": "pass", 
        "exp_month": 3, 
        "exp_year": 2013, 
        "last4": "4242", 
        "name": "John Doe", 
        "object": "card", 
        "type": "Visa"
      }, 
      "created": 1329776973, 
      "currency": "usd", 
      "customer": "cus_A0FULkVQwzwlUz", 
      "description": "the money you owed me", 
      "disputed": false, 
      "fee": 59, 
      "id": "ch_lCSjHD3hAxXcjO", 
      "livemode": false, 
      "object": "charge", 
      "paid": true, 
      "refunded": false
    }



Contents:
=========

.. toctree::
   :maxdepth: 2
   :glob:
   
   *
   zebra/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _GitHub repo: https://github.com/GoodCloud/django-zebra/
