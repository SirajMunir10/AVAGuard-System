import os
import django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1. Update .env
# NOTE: This script does NOT write your API key automatically.
# Add your DeepSeek API key to web_portal/.env manually:
#   DEEPSEEK_API_KEY=<your-key-here>
# You can get a key at: https://platform.deepseek.com/api_keys
env_path = BASE_DIR / '.env'
env_content = env_path.read_text() if env_path.exists() else ""
if "DEEPSEEK_API_KEY" not in env_content:
    print("WARNING: DEEPSEEK_API_KEY not found in .env")
    print("  Add it manually: DEEPSEEK_API_KEY=<your-key>  (see https://platform.deepseek.com/api_keys)")
else:
    print("DEEPSEEK_API_KEY already set in .env — OK")

# 2. Update Database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Organization
from ai_ops.models import AISettings

orgs = Organization.objects.all()
if not orgs.exists():
    print("No organizations found.")
else:
    org = orgs.first()
    settings, created = AISettings.objects.get_or_create(organization=org)
    settings.is_enabled = True
    settings.llm_provider = 'deepseek'
    settings.model_name = 'deepseek-chat'
    settings.save()
    print(f"Enabled AI Settings for organization: {org.name}")
