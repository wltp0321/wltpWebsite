sudo /home/odroid/wltp_website/venv/bin/hypercorn config.asgi:application --bind 0.0.0.0:443 --certfile django.crt --keyfile django.key
