from defaults import *
# SECURITY WARNING: keep the secret key used in production secret!
# Input a random string
# For random strings, try http://api.wordpress.org/secret-key/1.1/ Thanx a lot to wordpress team
SECRET_KEY = '-q@0-2+d8pz6pty@&fk-48pxz7zq3(65yb%12lis61znuv2sgi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS: Please input your domain instead your-domain-hear.com
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_db',
        'USER': 'user',
        'PASSWORD': 'for_paranoik',
        'HOST': 'localhost',
        'PORT': '3306',},
    }
#}
