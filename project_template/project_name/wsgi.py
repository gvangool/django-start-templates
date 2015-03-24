"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/wsgi/
"""
import os

# Specify the settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

def application(environ, start_response):
    '''
    WSGI wrapper

    Figure out whether incoming traffic came from HTTP.
    It checks via ``X-Forwarded-Protocol`` (set to ``https``) or
    ``X-Forwarded-Ssl`` (set to ``on``).
    '''
    # Trick Django into thinking proxied traffic is coming in via HTTPS.
    if environ.get('HTTP_X_FORWARDED_PROTOCOL', 'http') == 'https' or \
       environ.get('HTTP_X_FORWARDED_SSL', 'off') == 'on':
        environ['wsgi.url_scheme'] = 'https'
    return _application(environ, start_response)
