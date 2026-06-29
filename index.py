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

try:
    from django.core.wsgi import get_wsgi_application
    app = get_wsgi_application()
except Exception as _e:
    _tb = traceback.format_exc()
    _diag = (
        f"VERCEL={os.getenv('VERCEL')} "
        f"DEBUG={os.getenv('DEBUG')} "
        f"SECRET_KEY={'SET' if os.getenv('SECRET_KEY') else 'MISSING'} "
        f"DB_ENGINE={os.getenv('DB_ENGINE', 'not set')}"
    )
    _err_body = f"AVAGuard startup error:\n{_e}\n\n{_tb}\n\nDiagnostics: {_diag}".encode()

    def app(environ, start_response):
        start_response("500 Internal Server Error", [("Content-Type", "text/plain")])
        return [_err_body]

# Vercel checks for any of these names
application = app
handler = app
