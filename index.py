import os
import sys
import traceback

try:
    # Add the web_portal directory to Python's module path
    sys.path.append(os.path.join(os.path.dirname(__file__), "web_portal"))

    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as e:
    # Print the exception to stderr so it shows up in Vercel Runtime Logs
    print(f"FATAL ERROR ON STARTUP: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    
    # Still raise it so Vercel knows it failed, or return a fake app that prints the error
    def fallback_app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, headers)
        error_msg = f"Startup Error:\n{traceback.format_exc()}"
        return [error_msg.encode("utf-8")]
    
    app = fallback_app
