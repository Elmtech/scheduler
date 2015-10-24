# -*- coding: utf-8 -*-

from config.settings.common import *

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
