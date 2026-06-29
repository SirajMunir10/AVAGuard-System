import os
import sys
import traceback

def load_app():
    try:
        # Add the web_portal directory to Python's module path
        sys.path.append(os.path.join(os.path.dirname(__file__), "web_portal"))

        # Set the Django settings module
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

        from django.core.wsgi import get_wsgi_application
        return get_wsgi_application()
    except Exception as e:
        # Capture the error traceback IMMEDIATELY
        error_message = str(e)
        full_traceback = traceback.format_exc()
        
        def fallback_app(environ, start_response):
            status = '500 Internal Server Error'
            headers = [('Content-type', 'text/plain; charset=utf-8')]
            start_response(status, headers)
            error_msg = f"Startup Error: {error_message}\n\nFull Traceback:\n{full_traceback}"
            return [error_msg.encode("utf-8")]
        
        return fallback_app

app = load_app()
