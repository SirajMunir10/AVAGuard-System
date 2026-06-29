"""
AVAGuard Web Portal - Health & Diagnostic Endpoints

Designed for orchestrators (Kubernetes, AWS ECS), load balancers,
and enterprise monitoring systems (Prometheus, Datadog).
Provides separate, unauthenticated liveness and readiness probes.
"""

import time
import logging
from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache

logger = logging.getLogger(__name__)

# Start time to calculate uptime
_START_TIME = time.time()


def liveness_check(request):
    """
    Simple liveness probe (/health/live/).
    Confirms the application process is running and able to handle HTTP requests.
    Does not check downstream dependencies like database or cache.
    """
    uptime = int(time.time() - _START_TIME)
    
    return JsonResponse({
        'status': 'healthy',
        'probe': 'liveness',
        'uptime_seconds': uptime,
        'timestamp': time.time()
    }, status=200)


def readiness_check(request):
    """
    Comprehensive readiness probe (/health/ready/).
    Verifies all critical downstream dependencies are fully operational.
    Checks:
    1. Database connectivity and responsiveness.
    2. Cache connection (Redis/LocMem).
    3. Core scanning library availability.
    """
    checks = {}
    overall_status = 'healthy'
    status_code = 200

    # 1. Check Database
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
        checks['database'] = {'status': 'ok'}
    except Exception as e:
        logger.error(f"Readiness check failed - Database error: {e}")
        checks['database'] = {'status': 'error', 'message': str(e)}
        overall_status = 'unhealthy'
        status_code = 503

    # 2. Check Cache
    try:
        cache.set('health_readiness_ping', 'pong', timeout=5)
        val = cache.get('health_readiness_ping')
        if val == 'pong':
            checks['cache'] = {'status': 'ok'}
        else:
            checks['cache'] = {'status': 'degraded', 'message': 'Cache write succeeded but read failed'}
            overall_status = 'degraded'
    except Exception as e:
        logger.error(f"Readiness check failed - Cache error: {e}")
        checks['cache'] = {'status': 'error', 'message': str(e)}
        overall_status = 'unhealthy'
        status_code = 503

    # 3. Check Core Scanning Library
    try:
        from avaguard_core.checks import AVAILABLE_CHECKS
        checks['core_library'] = {
            'status': 'ok',
            'checks_available': len(AVAILABLE_CHECKS)
        }
    except ImportError:
        checks['core_library'] = {
            'status': 'degraded',
            'message': 'avaguard_core scanning library not found in path'
        }
        if overall_status == 'healthy':
            overall_status = 'degraded'

    uptime = int(time.time() - _START_TIME)

    # Resolve App Version
    try:
        import avaguard_core
        app_version = getattr(avaguard_core, '__version__', '0.1.0')
    except ImportError:
        app_version = "0.1.0"

    response_data = {
        'status': overall_status,
        'probe': 'readiness',
        'uptime_seconds': uptime,
        'version': app_version,
        'checks': checks,
        'timestamp': time.time()
    }

    return JsonResponse(response_data, status=status_code)
