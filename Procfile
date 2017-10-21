web: gunicorn kextech_site.wsgi --log-file -
worker: celery -A kextech_site worker -l info --without-gossip --without-mingle --without-heartbeat