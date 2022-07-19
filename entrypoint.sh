#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input


# gunicorn boom.wsgi:application --bind 0.0.0.0:8000
# gunicorn boom.asgi:application -k uvicorn.workers.UvicornWorker

gunicorn boom.asgi:application --forwarded-allow-ips='*' --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
# gunicorn boom:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80