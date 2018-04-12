web: gunicorn mysite.wsgi --log-file -
web: python3 mysite/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT mysite/settings.py 

