#!/bin/sh

python manage.py migrate
python manage.py compilemessages
exec "$@"
