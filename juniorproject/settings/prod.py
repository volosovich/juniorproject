from defaults import *

# SECURITY WARNING: keep the secret key used in production secret!
# Input a random string
# For random strings, try http://api.wordpress.org/secret-key/1.1/ Thanx a lot to wordpress team
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS: Please input your domain instead your-domain-hear.com
ALLOWED_HOSTS = ['your-domain-hear.com']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', 
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',},
    }
#}
