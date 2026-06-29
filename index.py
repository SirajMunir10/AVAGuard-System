import os
import sys

# Add the web_portal directory to Python's module path
sys.path.append(os.path.join(os.path.dirname(__file__), "web_portal"))

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
