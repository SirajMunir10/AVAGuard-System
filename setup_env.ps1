Write-Host "AVAGuard - Zero-to-Hero Environment Setup"
Write-Host "============================================="

# 1. Check Python version
$pythonVersion = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
Write-Host "Python version: $pythonVersion"
if ([double]$pythonVersion -ge 3.13) {
    Write-Host "[WARNING] Python 3.13+ detected. AI libraries (PyTorch/sentence-transformers) may crash on Windows. Python 3.12 is highly recommended." -ForegroundColor Yellow
}

# 2. Create Virtual Environment
Write-Host "Creating Virtual Environment (.venv)..."
python -m venv .venv

# 3. Activate Virtual Environment
Write-Host "Activating Virtual Environment..."
. .venv\Scripts\Activate.ps1

# 4. Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# 5. Install avaguard-core
Write-Host "Installing avaguard-core..."
pip install -e ./avaguard-core

# 6. Install avaguard-cli
Write-Host "Installing avaguard-cli..."
pip install -e ./avaguard-cli

# 7. Install requirements.txt
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# 8. Setup .env file
if (-not (Test-Path web_portal\.env)) {
    Write-Host "Setting up web_portal\.env from .env.example..."
    Copy-Item -Path web_portal\.env.example -Destination web_portal\.env
}

# 9. Perform migrations
Write-Host "Running database migrations..."
python web_portal/manage.py migrate

# 10. Create superuser if missing
Write-Host "Provisioning admin user..."
python web_portal/manage.py create_superuser_if_missing

# 11. Initial mock data load
Write-Host "Initializing initial dataset..."
python web_portal/manage.py seed_dev

Write-Host "============================================="
Write-Host "Setup Complete! You can now start the applications:"
Write-Host "1. CLI Engine: python -m avaguard.cli scan"
Write-Host "2. Web Portal: python web_portal/manage.py runserver"
Write-Host "3. Desktop UI: python desktop_app/main.py"

# ─── RAG-Train Python Dependencies ──────────────────────────────────────────
# Dependency Map:
# - sentence-transformers: Embedding model (build_index.py, retrieval.py)
# - faiss-cpu: Vector database (build_index.py, retrieval.py, query_index.py)
# - numpy: FAISS dependency, vector math
# - openai: DeepSeek API client (llm_service.py, generate_corpus.py)
# - google-generativeai: Gemini API client (synthetic_data_generator fallback)
# - torch: Required by sentence-transformers
# - huggingface_hub, transformers: sentence-transformers deps
# - tqdm, tiktoken, nltk: Text processing, chunking (generate_corpus.py)
# - pyyaml: CSV/YAML config reading (topics.csv, hardware_profiles.yaml)
# - ragas, rouge-score: Evaluation metrics

Write-Host "`n[RAG-Train] Installing indexing and embedding stack..." -ForegroundColor Cyan

function Install-Safe {
    param([string]$Package, [string]$ExtraArgs="")
    try {
        Write-Host "Installing $Package..."
        if ($ExtraArgs) {
            Invoke-Expression "pip install $Package $ExtraArgs" -ErrorAction Stop
        } else {
            Invoke-Expression "pip install $Package" -ErrorAction Stop
        }
    } catch {
        Write-Host "[WARNING] Failed to install $Package - continuing..." -ForegroundColor Yellow
    }
}

Install-Safe "sentence-transformers"
Install-Safe "faiss-cpu"
Install-Safe "numpy"
Install-Safe "openai"
Install-Safe "google-generativeai"
Install-Safe "torch" "--index-url https://download.pytorch.org/whl/cpu"
Install-Safe "huggingface_hub"
Install-Safe "transformers"
Install-Safe "tqdm"
Install-Safe "tiktoken"
Install-Safe "nltk"
Install-Safe "pyyaml"
Install-Safe "rank-bm25"

Write-Host "`n[Eval] Installing RAG evaluation tools..." -ForegroundColor Cyan
Install-Safe "ragas"
Install-Safe "rouge-score"

Write-Host "`n[Validation] Verifying critical imports..." -ForegroundColor Yellow
python -c "
import sys

def check_import(name, version_attr=None):
    print(f'Checking {name}... ', end='', flush=True)
    try:
        mod = __import__(name, fromlist=['*'])
        ver = getattr(mod, version_attr) if version_attr and hasattr(mod, version_attr) else 'present'
        print(f'[OK] ({ver})')
    except Exception as e:
        print(f'[FAIL]: {e}')
        sys.exit(1)

check_import('faiss', '__version__')
check_import('sentence_transformers', '__version__')
check_import('openai', '__version__')
check_import('google.generativeai')
check_import('django', '__version__')
check_import('rank_bm25')
print('[PASS] All RAG-Train imports OK')
"
if ($LASTEXITCODE -eq 0) {
    Write-Host "[Validation] Complete." -ForegroundColor Green
} else {
    Write-Host "[Validation] Failed. Note: If it failed on 'sentence_transformers' without an error message, it is a native crash due to Python 3.13+ on Windows." -ForegroundColor Red
}

