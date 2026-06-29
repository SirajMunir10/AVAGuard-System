#!/bin/bash
# Install requirements using the flag to override the externally managed environment
python3 -m pip install -r web_portal/requirements.txt --break-system-packages

# Run migrations
python3 web_portal/manage.py migrate --noinput

# Collect static files
python3 web_portal/manage.py collectstatic --noinput
