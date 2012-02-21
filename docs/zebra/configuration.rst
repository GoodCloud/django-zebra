.. py:module:: zebra.config.options

Configuration
=============

There are several options for Zebra. To override any of these options simply
add them to your ``settings.py`` with the value your desire.


-------------------------------------------------------------------------------


.. py:data:: STRIPE_PUBLISHABLE

    default:
        ``''``
    
    **Required to use the Stripe API.**
    
    Your Stripe API publishable key.


-------------------------------------------------------------------------------


.. py:data:: STRIPE_SECRET

    default:
        ``''``
    
    **Required to use the Stripe API.**
    
    Your Stripe API secret key.


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_AUDIT_RESULTS

    default ::
    
        {
            'active': 'active',
            'no_subscription': 'no_subscription',
            'past_due': 'past_due',
            'suspended': 'suspended',
            'trialing': 'trialing',
            'unpaid': 'unpaid',
            'cancelled': 'cancelled'
        }
    
    Dictionary in which the keys are possible responses from Stripe when
    checking the status of a subscription. Values are returned when the key
    matches the subscription status returned from Stripe.


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_AUTO_CREATE_STRIPE_CUSTOMERS

    default:
        ``True``
    
    
    Defaults to ``True`` but is only applicable if :py:data:`ZEBRA_ENABLE_APP`
    is ``True``.
    
    Boolean to control whether accessing ``stripe_customer`` on
    :py:data:`ZEBRA_CUSTOMER_MODEL` automatically creates a stripe customer
    if one doesn't exist for the instance.


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_CARD_YEARS

    default:
        ``range(_today.year, _today.year+12)``
    
    List of years used to populate :py:data:`ZEBRA_CARD_YEARS_CHOICES`.


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_CARD_YEARS_CHOICES

    default:
        ``[(i,i) for i in ZEBRA_CARD_YEARS]``
    
    List of pairs (Django choices format) to be used in the credit card year
    field in :py:class:`StripePaymentForm`.


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_CUSTOMER_MODEL

    default:
        ``None``
    
    If :py:data:`ZEBRA_ENABLE_APP` is ``True`` then the default value is
    ``zebra.Customer``


-------------------------------------------------------------------------------


.. py:data:: ZEBRA_ENABLE_APP

    default:
        ``False``
    
    Boolean that enables the default models and admin that comes with zebra.
    Not to be confused with ``marty``.

    
-------------------------------------------------------------------------------


.. py:data:: ZEBRA_MAXIMUM_STRIPE_CUSTOMER_LIST_SIZE

    default:
        ``100``
    
    Number of customers to return from querying Stripe when running the
    managment command to delete test users.


-------------------------------------------------------------------------------



.. py:data:: ZEBRA_ACTIVE_STATUSES

    default:
        ``('active', 'past_due', 'trialing')``

    Iterable of strings that should be considered active based on the values
    in :py:data:`ZEBRA_AUDIT_RESULTS`.

-------------------------------------------------------------------------------


.. py:data:: ZEBRA_INACTIVE_STATUSES

    default:
        ``('cancelled', 'suspended', 'unpaid', 'no_subscription')``
    
    Iterable of strings that should be considered inactive based on the values
    in :py:data:`ZEBRA_AUDIT_RESULTS`.

