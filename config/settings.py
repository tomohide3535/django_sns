"""
Django settings for django_website project.
Generated by 'django-admin startproject' using Django 3.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = joinpath(__file__).resolve().parent.parent 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7z7w^s)f0oz89biphu@_y&#(cub-k%w0#6^ic$fso!9eq0qs+*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['17e94fc7298348f4a82fef636b35b6e7.vfs.cloud9.ap-northeast-1.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    #'first_app',
    'accounts.apps.AccountsConfig',
    'first_app.apps.FirstAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

import dj_database_url
from dotenv import (
    find_dotenv,
    load_dotenv,
)
load_dotenv(find_dotenv())
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'dbuser',
        'PASSWORD': 'tomosun0510',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    [
        os.path.join(BASE_DIR, "static"), 
    ]
)

#プロフィール画像等アップロードしたファイルを保存するmediaディレクトリ
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = 'first_app:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
DEFAULT_FROM_EMAIL = 'admin@example.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#LOGIN_URL = 'login/'
#LOGIN_REDIRECT_URL = '/login_app/user/'
#LOGOUT_REDIRECT_URL = '/'