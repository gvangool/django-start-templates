if DEBUG:
    from fnmatch import fnmatch

    class glob_list(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt):
                    return True
            return False

    INTERNAL_IPS = glob_list(('127.0.0.1', ))
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ('debug_toolbar',)
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        DEBUG_TOOLBAR_CONFIG = {
                'INTERCEPT_REDIRECTS': False,
        }

# Uncomment if you want logging of the SQL statements
#LOGGING['loggers']['django.db.backends'] = {
#    'handlers': ['console', ],
#    'level': 'DEBUG',
#}
