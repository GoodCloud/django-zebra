#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "zebra",
    description = "Library for Django and Stripe",
    author = "Steven Skoczen",
    author_email = "steven@agoodcloud.com",
    url = "https://github.com/GoodCloud/django-zebra",
    version = "0.2",
    packages = find_packages(),
    zip_safe = False,
)