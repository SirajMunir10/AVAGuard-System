"""
Django settings for AVAGuard Web Portal.

Hardened for team collaboration:
- All config read from .env with safe fallbacks
- OTP_ENABLED flag to skip 2FA during development
- Auto-creates logs/ directory
- Console email fallback when credentials missing
"""

import os
import sys
import secrets, base64
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env FIRST — before anything else reads env vars
# BASE_DIR = web_portal/, so .env lives directly inside it
load_dotenv(BASE_DIR / '.env')

# --- AVAGuard Core Integration ---
# (Web Portal directly imports avaguard_core using the installed package)
PROJECT_ROOT = BASE_DIR.parent

# ==============================================================================
# Core Settings (from .env with safe fallbacks)
# ==============================================================================
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    # Generate a temporary secret key when none is provided
    SECRET_KEY = base64.urlsafe_b64encode(secrets.token_bytes(48)).decode()
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
if not ALLOWED_HOSTS:
    # Allow all hosts in serverless env (override in production if needed)
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = [h.strip() for h in ALLOWED_HOSTS.split(',') if h.strip()]

# JWT Signing Key — MUST be separate from SECRET_KEY.
# If SECRET_KEY leaks (error pages, git history), JWTs remain safe.
# Falls back to SECRET_KEY in development only.
JWT_SIGNING_KEY = os.getenv('JWT_SIGNING_KEY')
if not JWT_SIGNING_KEY:
    # Generate a temporary JWT signing key when none is provided
    JWT_SIGNING_KEY = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
# No else needed – JWT_SIGNING_KEY now always has a value

# OTP / 2FA toggle — set OTP_ENABLED=True in .env to enforce 2FA
OTP_ENABLED = os.getenv('OTP_ENABLED', 'False') == 'True'

# ── FAIL-FAST SAFETY ──
# Block production deployment with default insecure key
if not DEBUG and SECRET_KEY == 'dev-insecure-key-change-in-production':
    raise RuntimeError(
        'FATAL: SECRET_KEY is set to the default insecure value. '
        'Set a strong SECRET_KEY in .env before running with DEBUG=False.'
    )

if not DEBUG and JWT_SIGNING_KEY == '':
    raise RuntimeError(
        'FATAL: JWT_SIGNING_KEY is not set. '
        'Set a strong JWT_SIGNING_KEY in .env for production (must differ from SECRET_KEY).'
    )

# Secure cookie settings for production
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True

# ==============================================================================
# Application definition
# ==============================================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    # Local apps
    'core',
    'api',
    'ai_ops',
]

# Conditionally add OTP apps only when enabled
if OTP_ENABLED:
    INSTALLED_APPS += [
        'django_otp',
        'django_otp.plugins.otp_totp',
        'two_factor',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

# Conditionally add OTP middleware
if OTP_ENABLED:
    MIDDLEWARE.append('django_otp.middleware.OTPMiddleware')

MIDDLEWARE += [
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # AVAGuard Security Middleware
    'core.middleware.RateLimitMiddleware',
    'core.middleware.SecurityHeadersMiddleware',
    'core.tenant_middleware.TenantMiddleware',
    'core.middleware.FirstLoginMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ai_ops.context_processors.ai_mode_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# ==============================================================================
# Database — Auto-switches based on environment
#   Local/Desktop: SQLite (default, zero config)
#   Team/Production: PostgreSQL via Supabase (set DB_ENGINE in .env)
# ==============================================================================
_db_engine = os.getenv('DB_ENGINE', 'sqlite3')

if _db_engine == 'postgresql':
    # PostgreSQL — Supabase or any hosted PostgreSQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME', 'postgres'),
            'USER': os.getenv('DB_USER', 'postgres'),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
            'CONN_MAX_AGE': int(os.getenv('DB_CONN_MAX_AGE', '60')),
            'CONN_HEALTH_CHECKS': True,
            'OPTIONS': {
                'sslmode': os.getenv('DB_SSLMODE', 'require'),
            },
        }
    }
else:
    # Use in‑memory SQLite when the filesystem is read‑only (Vercel) or when VERCEL env var is set
    if os.getenv('VERCEL') == '1' or not os.access(BASE_DIR, os.W_OK):
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

# ==============================================================================
# Password validation
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 12}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Custom User Model
AUTH_USER_MODEL = 'core.User'

# ==============================================================================
# Authentication Redirects
# ==============================================================================
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/auth/login/'

# ==============================================================================
# Internationalization
# ==============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# Static files
# ==============================================================================
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==============================================================================
# Request / Upload Limits (prevent OOM via oversized payloads)
# ==============================================================================
DATA_UPLOAD_MAX_MEMORY_SIZE = int(os.getenv('DATA_UPLOAD_MAX_MEMORY_SIZE', 10 * 1024 * 1024))  # 10MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = int(os.getenv('DATA_UPLOAD_MAX_NUMBER_FIELDS', 5000))

# Maximum number of individual check results per scan upload
SCAN_UPLOAD_MAX_RESULTS = int(os.getenv('SCAN_UPLOAD_MAX_RESULTS', 500))

# ==============================================================================
# Default primary key field type
# ==============================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================================================================
# Django REST Framework
# ==============================================================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

# ==============================================================================
# JWT Configuration
# ==============================================================================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': JWT_SIGNING_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
}

# ==============================================================================
# CORS Configuration (for Desktop App)
# ==============================================================================
import os
CORS_ALLOWED_ORIGINS = [
    os.getenv('PORTAL_CORS_ORIGIN', 'http://localhost:8000'),
    os.getenv('PORTAL_CORS_ORIGIN_ALT', 'http://127.0.0.1:8000'),
]
CORS_ALLOW_CREDENTIALS = True

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True

# ==============================================================================
# Logging Configuration (auto-creates logs/ directory)
# ==============================================================================
# On Vercel, the filesystem is read-only, so we fallback to /tmp or just disable file logging.
if os.getenv("VERCEL") == "1" or not os.access(BASE_DIR, os.W_OK):
    LOGS_DIR = Path('/tmp/logs')
else:
    LOGS_DIR = BASE_DIR / 'logs'

try:
    os.makedirs(LOGS_DIR, exist_ok=True)
except Exception:
    pass


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOGS_DIR / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'api': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# ==============================================================================
# Email Configuration
# ==============================================================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = 'AVAGuard Security <noreply@avaguard.com>'

# Fallback to console if email not configured
if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ==============================================================================
# Cache Configuration — AI Query Cache + Rate Limiting
# ==============================================================================
#
# CURRENT BEHAVIOUR (no REDIS_URL set):
#   - LocMemCache: in-process only. Cache is NOT shared across Gunicorn workers.
#   - Each worker has an independent cache. Cache hits only occur within one worker.
#   - Appropriate for: single-worker dev server, unit tests.
#
# PRODUCTION MIGRATION (multi-worker / multi-server):
#   To switch to Redis, set REDIS_URL in your .env file. No code changes needed.
#
#   Step-by-step migration:
#     1. Install redis-py:
#           pip install redis
#     2. Start Redis (Docker example):
#           docker run -d -p 6379:6379 redis:7-alpine
#     3. Add to .env:
#           REDIS_URL=redis://localhost:6379/1
#     4. Restart Gunicorn. Cache is now shared across all workers.
#     5. Verify with: python manage.py shell -c "from django.core.cache import cache; cache.set('test',1); print(cache.get('test'))"
#
#   Behaviour changes when switching to Redis:
#     - AI query cache hits shared across all Gunicorn workers (correct multi-worker behaviour)
#     - Cache persists across server restarts (TTL still applies — 1 hour for query cache)
#     - cache.clear() in build_index.py clears ALL workers at once (already implemented)
#     - Rate-limit counters (login attempts, OTP) are accurate across all workers
#     - AI per-user rate limit (ai_query_rate_<user_id>) works correctly under load
#
#   IVF migration trigger reminder:
#     - Keep IndexFlatL2 up to 3,000 documents (exact, O(n) scan acceptable)
#     - At 3,000-5,000 docs: prototype IndexIVFFlat in staging, benchmark latency vs accuracy
#     - Above 5,000 docs: migrate production to IndexIVFFlat (nlist=128 or sqrt(n))
#     - Latency threshold to force migration: any query exceeding 2,000ms P95 on the pipeline
#
_redis_url = os.getenv('REDIS_URL', '')

if _redis_url:
    # Production: Redis cache — shared across workers, persists across restarts
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': _redis_url,
            'TIMEOUT': 3600,  # 1 hour default TTL (AI query cache uses same)
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }
else:
    # Development / single-worker: In-memory cache — not shared across workers
    # Switch to Redis (above) before any multi-worker or multi-server deployment.
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'avaguard-rate-limit-cache',
        }
    }

# ==============================================================================
# Security Settings
# ==============================================================================
RATE_LIMIT_LOGIN_ATTEMPTS = 5
RATE_LIMIT_LOCKOUT_MINUTES = 15
RATE_LIMIT_OTP_ATTEMPTS = 10
RATE_LIMIT_OTP_LOCKOUT_MINUTES = 30

# Default Organization
DEFAULT_ORGANIZATION_NAME = 'AVAGuard'

# Sudo-mode validity window (seconds)
SUDO_VALIDITY_SECONDS = 300  # 5 minutes

# ==============================================================================
# Production Deployment Settings
# ==============================================================================
# The following settings are flagged by `python manage.py check --deploy`.
# They are deliberately disabled in local development to prevent breaking the local dev server.
# In production, ensure these are configured via environment variables or a production settings file:
# - SECURE_HSTS_SECONDS: Must be set to a positive integer (e.g., 31536000) when served over HTTPS.
# - SECURE_SSL_REDIRECT: Must be True to force HTTPS.
# - SESSION_COOKIE_SECURE: Must be True for secure session cookies.
# - CSRF_COOKIE_SECURE: Must be True for secure CSRF cookies.
# - SECRET_KEY: Must be a long, random, securely generated value.
# - DEBUG: Must be False.

# ==============================================================================
# AI Retrieval Configuration (Phase 5)
# ==============================================================================
# Path to the FAISS index directory. Set to None or leave unset to use MockRetriever.
AI_INDEX_DIR = os.getenv('AI_INDEX_DIR', str(PROJECT_ROOT / 'rag-train' / 'll-finetuning' / 'rag' / 'faiss_index'))

# Path to the raw corpus directory.
AI_CORPUS_DIR = os.getenv('AI_CORPUS_DIR', str(PROJECT_ROOT / 'rag-train' / 'll-finetuning' / 'rag' / 'corpus'))

# AI Retrieval Architecture Constants (Phase 0 & 1)
AI_EMBEDDING_MODEL = os.getenv('AI_EMBEDDING_MODEL', 'BAAI/bge-base-en-v1.5')
AI_RERANKER_MODEL = os.getenv('AI_RERANKER_MODEL', 'cross-encoder/ms-marco-MiniLM-L-6-v2')
AI_MIN_RELEVANCE_SCORE = float(os.getenv('AI_MIN_RELEVANCE_SCORE', '-0.5'))
AI_RETRIEVAL_K_CANDIDATES = int(os.getenv('AI_RETRIEVAL_K_CANDIDATES', '20'))
AI_RETRIEVAL_K_FINAL = int(os.getenv('AI_RETRIEVAL_K_FINAL', '5'))
AI_RRF_CONSTANT = int(os.getenv('AI_RRF_CONSTANT', '60'))

# LLM API key for generation. Supports DeepSeek (default), OpenAI, or Azure OpenAI.
# Leave empty to use MockLLMService (no external calls).
AI_LLM_API_KEY = os.getenv('AI_LLM_API_KEY', os.getenv('DEEPSEEK_API_KEY', ''))

