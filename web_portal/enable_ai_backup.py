import os
import django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

#1. Update .env
env_path = BASE_DIR / '.env'
env_content = env_path.read_text() if env_path.exists() else ""
if "DEEPSEEK_API_KEY" not in env_content:
    with open(env_path, "a") as f:
        f.write("\nDEEPSEEK_API_KEY=your_api_key_here\n")
    print("Added DEEPSEEK_API_KEY placeholder to .env")

#2. Update Database
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