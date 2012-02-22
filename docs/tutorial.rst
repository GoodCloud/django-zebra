Tutorial
==========

**THIS DOCUMENT IS STILL UNDER DEVELOPMENT**

This is an example quickstart that makes many assumptions about your development
environment. Please report errors and omissions at
https://github.com/GoodCloud/django-zebra/issues


Activate Environment
--------------------

Create or activate your development environment.

For this example we will be using virtual environment and virtual environment
wrapper to create a demo environment.

::

    mkvirtualenv --no-site-packages --distribute zebra-demo


Install Dependencies
--------------------

``django-zebra`` is a library for integrating Stripe payments into Django
applications so you will need to install the following dependencies:

- pycurl *(recommended but not required)*
- django
- stripe
- django-zebra

::

    pip install pycurl django stripe django-zebra


Configure Django
----------------

You'll need to include your Stripe account information in your environment and
there are 2 supported ways to do this.

#. Environment Variables
#. Django's settings file

**Environment Variables**

In BASH just export the variables::

    export STRIPE_PUBLISHABLE=YOUR_PUB_KEY
    export STRIPE_SECRET=YOUR_SECRET_KEY

**Django Settings**

Append the following lines to your project's settings.py file::

    STRIPE_PUBLISHABLE = "YOUR_PUB_KEY"
    STRIPE_SECRET = "YOUR_SECRET_KEY"


