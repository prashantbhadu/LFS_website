"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()


def init_db_on_startup():
    """
    Automatic production safeguard for Render/PaaS hosting.
    Ensures database tables and custom romantic data are initialized
    even if the user only specified 'gunicorn config.wsgi:application'.
    """
    try:
        from django.core.management import call_command
        from django.db import connection
        tables = connection.introspection.table_names()
        if "love_site_sitesetting" not in tables:
            print("[Startup] Initializing database tables via migrate...")
            call_command("migrate", interactive=False)
            fixture_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "initial_data.json")
            if os.path.exists(fixture_path):
                print("[Startup] Loading initial_data.json...")
                call_command("loaddata", fixture_path)
            else:
                call_command("seed_love_data")
    except Exception as exc:
        print(f"[Startup Notice] Auto-migration status: {exc}")


init_db_on_startup()
