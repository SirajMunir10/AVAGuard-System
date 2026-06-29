import os
import sys
import traceback

# ── Critical: add web_portal to the Python path so Django can find 'config.settings' ──
_here = os.path.dirname(os.path.abspath(__file__))  # project root
_web_portal = os.path.join(_here, "web_portal")
if _web_portal not in sys.path:
    sys.path.insert(0, _web_portal)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def _make_error_app(error_message, full_traceback, diagnostics):
    """Return a minimal WSGI app that outputs startup errors for debugging."""
    def fallback_app(environ, start_response):
        status = "500 Internal Server Error"
        headers = [("Content-type", "text/plain; charset=utf-8")]
        start_response(status, headers)
        body = (
            f"AVAGuard Startup Error\n"
            f"{'='*60}\n"
            f"{error_message}\n\n"
            f"Full Traceback:\n{full_traceback}\n\n"
            f"Diagnostics:\n{diagnostics}"
        )
        return [body.encode("utf-8")]
    return fallback_app


try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    app = application
    handler = app
except Exception as e:
    _tb = traceback.format_exc()
    _diag = (
        f"VERCEL={os.getenv('VERCEL')}\n"
        f"DEBUG={os.getenv('DEBUG')}\n"
        f"SECRET_KEY set: {'YES' if os.getenv('SECRET_KEY') else 'NO'}\n"
        f"JWT_SIGNING_KEY set: {'YES' if os.getenv('JWT_SIGNING_KEY') else 'NO'}\n"
        f"DB_ENGINE={os.getenv('DB_ENGINE', 'not set')}\n"
        f"Python path: {sys.path}\n"
    )
    app = _make_error_app(str(e), _tb, _diag)
    handler = app
    application = app
