# -*- coding: utf-8 -*-
from config.settings.common import *

import environ


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ADMINS = []
for admin in env('ADMINS').split(';'):
    ADMINS.append(admin.split(','))

MANAGERS = ADMINS

STATIC_ROOT = env('STATIC_ROOT')
MEDIA_ROOT = env('MEDIA_ROOT')

EMAIL_URL = env.email_url('EMAIL_URL')

EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']

EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX')
