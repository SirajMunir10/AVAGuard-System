import os
import sys
import traceback

# ── Add web_portal to path so Django can find 'config.settings' ──
_here = os.path.dirname(os.path.abspath(__file__))
_web_portal = os.path.join(_here, "web_portal")
if _web_portal not in sys.path:
    sys.path.insert(0, _web_portal)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# ── Must be defined at module top-level so Vercel's scanner finds it ──
app = None
_startup_error = None

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as _e:
    _startup_error = (
        f"AVAGuard Startup FAILED\n"
        f"{'='*60}\n"
        f"Error: {type(_e).__name__}: {_e}\n\n"
        f"Full Traceback:\n{traceback.format_exc()}\n\n"
        f"--- Diagnostics ---\n"
        f"VERCEL         = {os.getenv('VERCEL', 'NOT SET')}\n"
        f"DEBUG          = {os.getenv('DEBUG', 'NOT SET')}\n"
        f"DB_ENGINE      = {os.getenv('DB_ENGINE', 'NOT SET')}\n"
        f"SECRET_KEY     = {'SET' if os.getenv('SECRET_KEY') else 'MISSING'}\n"
        f"DB_HOST        = {os.getenv('DB_HOST', 'NOT SET')}\n"
        f"sys.path       = {sys.path}\n"
    )

    def app(environ, start_response):
        # Return 200 so Vercel shows our diagnostic instead of its own 500 page
        start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
        return [_startup_error.encode("utf-8")]


# Vercel checks for any of these names
application = app
handler = app
