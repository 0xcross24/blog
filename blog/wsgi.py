"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

application = get_wsgi_application()
