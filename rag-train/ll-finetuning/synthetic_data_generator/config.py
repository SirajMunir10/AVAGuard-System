"""
AVAGuard Security AI - Configuration Module
Central configuration for API providers, generation parameters, and quality thresholds.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
CONFIG_DIR = Path(__file__).parent.parent / "config"
ENV_FILE = CONFIG_DIR / ".env"
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)
else:
    load_dotenv()  # Try default .env location

# ============================================
# PROJECT PATHS
# ============================================
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
GENERATED_DIR = DATA_DIR / "generated"
VALIDATED_DIR = DATA_DIR / "validated"
CHECKPOINTS_DIR = DATA_DIR / "checkpoints"
LOGS_DIR = PROJECT_ROOT / "logs"
DB_PATH = PROJECT_ROOT / "question_registry" / "questions.db"
CONFIG_PATH = CONFIG_DIR / "domain_map.yaml"
TOKEN_STATE_FILE = DATA_DIR / ".token_usage.json"

# Create directories if they don't exist
for d in [GENERATED_DIR, VALIDATED_DIR, CHECKPOINTS_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ============================================
# API PROVIDER CONFIGURATION
# ============================================
# Priority order: 1 = try first, higher = fallback
# Free tier limits are approximate monthly token budgets

API_PROVIDERS = {
    "gemini": {
        "model": "gemini-2.5-flash-lite",
        "api_key_env": "GEMINI_API_KEY",
        "free_tier_limit": 2_000_000,
        "priority": 1,
        "type": "google",
        "rate_limit_rpm": 15,
        "description": "Google Gemini - 1000 RPD FREE (flash-lite), supports multi-key rotation"
    },
    "deepseek": {
        "model": "deepseek-chat",
        "api_key_env": "DEEPSEEK_API_KEY",
        "base_url": "https://api.deepseek.com",
        "free_tier_limit": 500_000,
        "priority": 2,
        "type": "openai_compatible",
        "rate_limit_rpm": 60,
        "description": "DeepSeek - 500K tokens free credit, excellent for code"
    },
    "groq": {
        "model": "llama-3.3-70b-versatile",
        "api_key_env": "GROQ_API_KEY",
        "base_url": "https://api.groq.com/openai/v1",
        "free_tier_limit": 10_000_000,  # Rate-limited but generous
        "priority": 3,
        "type": "openai_compatible",
        "rate_limit_rpm": 30,
        "description": "Groq - Very fast inference, Llama-3.3-70B free"
    },
    "together": {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "api_key_env": "TOGETHER_API_KEY",
        "base_url": "https://api.together.xyz/v1",
        "free_tier_limit": 300_000,
        "priority": 4,
        "type": "openai_compatible",
        "rate_limit_rpm": 60,
        "description": "Together.ai - $25 free credit, access to Llama-3.3-70B"
    },
    "mistral": {
        "model": "mistral-small-latest",
        "api_key_env": "MISTRAL_API_KEY",
        "base_url": "https://api.mistral.ai/v1",
        "free_tier_limit": 100_000,
        "priority": 5,
        "type": "openai_compatible",
        "rate_limit_rpm": 30,
        "description": "Mistral AI - Free tier with rate limits"
    },
    "claude": {
        "model": "claude-sonnet-4-20250514",
        "api_key_env": "CLAUDE_API_KEY",
        "free_tier_limit": 100_000,
        "priority": 6,
        "type": "anthropic",
        "rate_limit_rpm": 5,
        "description": "Anthropic Claude - $5 free credit, best reasoning"
    },
    "openai": {
        "model": "gpt-4o-mini",
        "api_key_env": "OPENAI_API_KEY",
        "free_tier_limit": 100_000,
        "priority": 7,
        "type": "openai_native",
        "rate_limit_rpm": 3,
        "description": "OpenAI - $5 free credit, GPT-4o-mini"
    },
    "cohere": {
        "model": "command-a-03-2025",
        "api_key_env": "COHERE_API_KEY",
        "free_tier_limit": 50_000,
        "priority": 8,
        "type": "cohere",
        "rate_limit_rpm": 10,
        "description": "Cohere - Trial key, 1000 calls/month"
    },
    "openrouter": {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "api_key_env": "OPENROUTER_API_KEY",
        "base_url": "https://openrouter.ai/api/v1",
        "free_tier_limit": 1_000_000,
        "priority": 9,
        "type": "openai_compatible",
        "rate_limit_rpm": 20,
        "description": "OpenRouter - Free models (Llama-3.3-70B, etc.)"
    },
    "huggingface": {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "api_key_env": "HF_API_KEY",
        "base_url": "https://router.huggingface.co/v1",
        "free_tier_limit": 500_000,
        "priority": 10,
        "type": "openai_compatible",
        "rate_limit_rpm": 10,
        "description": "Hugging Face - Free serverless inference (OpenAI-compatible)"
    }
}

# ============================================
# GENERATION PARAMETERS
# ============================================
GENERATION_CONFIG = {
    "temperature_questions": 0.9,       # Higher creativity for diverse questions
    "temperature_answers": 0.7,         # Balanced for accuracy + variety
    "max_tokens_question": 1500,        # Max tokens for question generation
    "max_tokens_answer": 2500,          # Max tokens for answer generation
    "batch_size": 25,                   # Questions per API call
    "checkpoint_interval": 100,         # Save checkpoint every N entries
    "retry_attempts": 3,                # Retries on API failure
    "retry_delay_base": 2,              # Base delay for exponential backoff (seconds)
    "quality_threshold": 7.5,           # Minimum score to keep (0-10)
    "quality_threshold_strict": 8.5,    # Score for "high quality" label
}

# ============================================
# DIFFICULTY DISTRIBUTION
# ============================================
DIFFICULTY_DISTRIBUTION = {
    "beginner": 0.25,       # 25% basic questions
    "intermediate": 0.45,   # 45% intermediate
    "advanced": 0.20,       # 20% advanced
    "expert": 0.10          # 10% expert-level
}

# ============================================
# QUESTION TYPES
# ============================================
QUESTION_TYPES = [
    "conceptual",        # "What is...?", "Explain..."
    "procedural",        # "How do I...?", "Steps to..."
    "troubleshooting",   # "A user reports...", "Error when..."
    "detection",         # "How can I detect...?", "Write a query..."
    "best_practice",     # "What is the recommended...?"
    "comparison",        # "What's the difference between...?"
    "scenario",          # "Your organization is...", "During an IR..."
    "compliance",        # "How to satisfy CIS control...?"
    "code_command",      # "Write a script/command to..."
    "architecture",      # "Design a...", "Architecture for..."
]

# ============================================
# EXPERT PERSONAS (System Prompts)
# ============================================
EXPERT_PERSONAS = {
    "azure_security": """You are a Microsoft Azure Security Architect with 15+ years of experience.
You hold AZ-500, SC-100, and AZ-305 certifications.
Always include: Azure Portal paths, PowerShell/CLI commands, ARM/Bicep templates when relevant.
Reference actual Azure service names and features. Provide actionable, production-ready guidance.""",

    "aws_security": """You are an AWS Security Specialist with AWS Security Specialty and Solutions Architect Professional certifications.
Always include: AWS CLI commands, CloudFormation templates, and IAM policy examples.
Reference actual AWS service names, ARNs, and console paths.""",

    "gcp_security": """You are a Google Cloud Security Engineer with Professional Cloud Security Engineer certification.
Include: gcloud CLI commands, Terraform examples, and IAM policy configurations.
Reference actual GCP service names, resource hierarchies, and security features.""",

    "cis_benchmarks": """You are a CIS Benchmark auditor and compliance consultant with 10+ years experience.
Always cite specific CIS control numbers (e.g., "CIS Azure 2.0.0 - Control 2.1.1").
Include both audit procedures AND remediation steps with automation scripts.""",

    "nist_frameworks": """You are a NIST Cybersecurity Framework specialist and federal compliance consultant.
Reference specific NIST SP 800-53 controls, CSF core functions, and implementation tiers.
Map controls to practical implementation steps.""",

    "sentinel_kql": """You are a Microsoft Sentinel architect and KQL expert specializing in threat detection.
Write production-ready KQL queries that are copy-paste ready.
Include inline comments, explain detection logic, and suggest tuning recommendations.""",

    "incident_response": """You are a senior Incident Response Manager with GCIH, GCFA, and GREM certifications.
Walk through systematic IR procedures: detection, analysis, containment, eradication, recovery, lessons learned.
Include forensic commands, SIEM queries, and artifact analysis.""",

    "mitre_attack": """You are a MITRE ATT&CK subject matter expert and threat intelligence analyst.
Reference specific technique IDs (T-codes), sub-techniques, and procedure examples.
Map detections to data sources and provide hunting queries.""",

    "compliance_general": """You are a senior compliance consultant with CISA, CISSP, and CISM certifications.
Expert in ISO 27001, PCI-DSS, HIPAA, SOC 2, and GDPR.
Provide practical implementation guidance, not just theoretical explanations.""",

    "network_security": """You are a senior network security engineer with 15+ years experience.
Expert in firewalls, IDS/IPS, Zero Trust, VPNs, and network forensics.
Include CLI commands for common network equipment (Cisco, Palo Alto, etc.).""",

    "malware_analysis": """You are a senior malware analyst with GREM certification.
Expert in static analysis, dynamic analysis, reverse engineering, and IOC extraction.
Include tool usage (IDA Pro, Ghidra, Process Monitor, Wireshark) and YARA rules.""",

    "devsecops": """You are a DevSecOps engineer expert in CI/CD security, container security, and IaC scanning.
Include pipeline configurations, Dockerfile security, Terraform security, and secret management.
Reference tools like Trivy, Checkov, Snyk, SonarQube.""",

    "general_security": """You are a senior cybersecurity professional with CISSP, CEH, and OSCP certifications.
Provide comprehensive, accurate, and actionable security guidance.
Include relevant tools, commands, and frameworks in your answers."""
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_api_key(provider: str) -> str | None:
    """Get the primary API key for a provider from environment variables."""
    if provider not in API_PROVIDERS:
        return None
    env_var = API_PROVIDERS[provider]["api_key_env"]
    return os.getenv(env_var)


def get_api_keys(provider: str) -> list[str]:
    """Get ALL API keys for a provider (supports multi-account rotation).
    
    Checks for: PROVIDER_API_KEY, PROVIDER_API_KEY_2, PROVIDER_API_KEY_3, etc.
    This allows using multiple free-tier accounts to multiply quota.
    
    Example .env:
        GEMINI_API_KEY=key1
        GEMINI_API_KEY_2=key2
        GEMINI_API_KEY_3=key3
        GROQ_API_KEY=key1
        GROQ_API_KEY_2=key2
    """
    if provider not in API_PROVIDERS:
        return []
    keys = []
    env_var = API_PROVIDERS[provider]["api_key_env"]
    # Primary key
    primary = os.getenv(env_var)
    if primary and not primary.startswith("your_"):
        keys.append(primary)
    # Additional keys: _2, _3, ... _10
    for i in range(2, 11):
        extra = os.getenv(f"{env_var}_{i}")
        if extra and not extra.startswith("your_"):
            keys.append(extra)
    return keys


def get_available_providers() -> list[str]:
    """Return list of providers that have API keys configured."""
    available = []
    for provider in sorted(API_PROVIDERS.keys(), key=lambda x: API_PROVIDERS[x]["priority"]):
        if get_api_keys(provider):  # Uses multi-key aware function
            available.append(provider)
    return available


def get_provider_info() -> list[dict]:
    """Get info about all providers for dashboard display."""
    info = []
    for name, config in sorted(API_PROVIDERS.items(), key=lambda x: x[1]["priority"]):
        keys = get_api_keys(name)
        num_keys = len(keys)
        info.append({
            "name": name,
            "model": config["model"],
            "has_key": num_keys > 0,
            "num_keys": num_keys,
            "free_limit": config["free_tier_limit"],
            "priority": config["priority"],
            "description": config["description"],
            "status": f"✅ Active ({num_keys} key{'s' if num_keys > 1 else ''})" if num_keys > 0 else "❌ No API Key"
        })
    return info
