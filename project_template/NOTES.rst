Notes
=====
Settings
--------
- Reads settings from .env via `django-dotenv
  <https://github.com/jacobian/django-dotenv>`_
- Config database via `dj-database-url
  <https://github.com/kennethreitz/dj-database-url>`_: write a env variable
  with ``DATABASE_URL`` to configure default database
- Config cach via `django-cache-url
  <https://github.com/ghickman/django-cache-url>`_: write a env variable
  with ``CACHE_URL`` to configure default cache backend

Examples can be found in our ``.env``.

PyMySQL
-------
If you want to use pymsql (instead of MySQL-python), you need to add the
following to ``manage.py`` and ``{{ project_name }}.wsgi``::

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass
