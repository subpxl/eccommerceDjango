
from pathlib import Path
import os
from decouple import  config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*pifr^q0ng7q$*v%3m89+npv-3+-r@*tx^#mgo!&d3qqhz+0)t'

DEBUG = True


ALLOWED_HOSTS = ['localhost','127.0.0.1','165.232.176.185','digitalbazaar.io']

ALLOWED_HOSTS += ['ganjalust.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'accounts',
    'orders',
    'seller',
    'storefront',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ondc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # custom preporcessors
                'seller.context_processors.menu_links',
            ],
        },
    },
]

WSGI_APPLICATION = 'ondc.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'greatcart',
    #     'USER': 'postgres',
    #     'PASSWORD': 'Gaumata@321',
    #     'HOST': 'localhost',    
    # }

}



AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATICFILES_DIRS =[
    'ondc/static'
]


AUTH_USER_MODEL = 'accounts.User'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


RAZOR_KEY_ID = config('RAZOR_KEY_ID',default='')
RAZOR_KEY_SECRET = config('RAZOR_KEY_SECRET',default='')

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY',default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY',default='')

