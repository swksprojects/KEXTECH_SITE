web: gunicorn kextech_site.wsgi --log-file -
worker: python manage.py celery worker -B -l info