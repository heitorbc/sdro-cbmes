"""
WSGI config for sdro_cbmes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
##comentar/descomentar
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdro_cbmes.settings")

application = get_wsgi_application()
##comentar/descomentar
application = DjangoWhiteNoise(application)