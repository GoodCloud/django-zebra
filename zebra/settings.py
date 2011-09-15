import os

# Stripe keys
STRIPE_PUBLISHABLE = 'pk_dHA9lrZx2If0QQyGU3aHUf8K8J5PW'
STRIPE_SECRET = '82H5Cfy1n0Iw2ot4BVblgc8zN8aPl7mh'

# customized settings
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(PROJECT_ROOT)
TIME_ZONE = 'America/Los_Angeles'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(SITE_ROOT, 'monospace.sqlite'),                      
    }
}
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.messages',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.staticfiles',
  'monospace'
)
BCRYPT_ROUNDS = 15

# default Django settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = 'lb-06%rmn$fmhhu!mr@3nc(&$0985qvddj%_5=t@94x@#@jcs@'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'monospace.urls'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
