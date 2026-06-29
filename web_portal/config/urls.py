"""
URL configuration for AVAGuard Web Portal.
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Django admin is available in development by default.
# In production, set DJANGO_ADMIN_ENABLED=True to explicitly enable it.
# Operational management should use the AVAGuard SuperAdmin panel instead.
_admin_enabled = os.getenv('DJANGO_ADMIN_ENABLED', 'True' if settings.DEBUG else 'False') == 'True'

urlpatterns = []

if _admin_enabled:
    urlpatterns.append(path('admin/', admin.site.urls))

urlpatterns += [
    # API endpoints
    path('api/', include('api.urls', namespace='api')),

    # AI Operations API
    path('api/ai/', include('ai_ops.urls', namespace='ai_ops')),

    # AI Operations UI templates
    path('ai/', include('ai_ops.urls_ui', namespace='ai_ops_ui')),

    # Core views (dashboard, etc.)
    path('', include('core.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
