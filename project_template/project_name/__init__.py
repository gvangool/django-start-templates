VERSION = '0.0.1'

def get_version():
    from django.conf import settings
    if settings.DEBUG:
        import os
        try:
            return os.popen("git describe").readlines()[0].strip()[1:]
        except IndexError:
            pass
    return VERSION

__version__ = get_version()
