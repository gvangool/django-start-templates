"""
WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

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
    '''
    # Trick Django into thinking proxied traffic is coming in via HTTPS,
    # but only if the HTTP_X_FORWARDED_SSL is "on".
    if environ.get('HTTP_X_FORWARDED_PROTOCOL', 'http') == 'https' or \
       environ.get('HTTP_X_FORWARDED_SSL', 'off') == 'on':
        environ['wsgi.url_scheme'] = 'https'
    return _application(environ, start_response)
