#!/bin/bash
# Install requirements
pip install -r web_portal/requirements.txt

# Run migrations
python web_portal/manage.py migrate

# Collect static files
python web_portal/manage.py collectstatic --noinput
