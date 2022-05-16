web: waitress-serve --port=$PORT fashion_shop.wsgi:application
web: gunicorn fashion_shop.wsgi:application --log-file - --log-level debug

manage.py migrate