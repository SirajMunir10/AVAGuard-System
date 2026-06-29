"""
AVAGuard Desktop - Enhanced Desktop Application
Enterprise-grade compliance scanner with SRS-compliant features.
"""

import sys
import os
import sqlite3
import configparser
import logging
import uuid
import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Tuple, Any, ClassVar, Type
from dataclasses import dataclass, field
import pathlib
from utils.session_manager import GlobalSessionManager
from utils.exceptions import SessionRevokedError
import time







# ============================================================================
# INITIALIZATION & PATHS (SRS-COMPLIANT)
# ============================================================================
# Calculate absolute paths
current_file = os.path.abspath(__file__)
workers_dir = os.path.dirname(current_file)
project_root = os.path.dirname(workers_dir)      # desktop_app/
ava_root = os.path.dirname(project_root)          # AVA/

# Define library paths
core_path = os.path.join(ava_root, 'avaguard-core')
cli_path = os.path.join(ava_root, 'avaguard-cli')

# Add to system path for imports - PRIORITIZE local folders to resolve nested modules
for path in [core_path, cli_path, project_root, ava_root]:
    if path and path not in sys.path:
        sys.path.insert(0, path)

print("[AVAGuard Desktop] Initializing AVAGuard Desktop v1.0...")
print(f"Project Root: {project_root}")
print(f"Core Path: {core_path}")

# Since we installed via pip -e, we can import directly
try:
    import avaguard_core
    from avaguard_core.reporter import EnhancedReporter as Reporter, ReportMetadata, ReportTier
    import avaguard.cli
    print("[SUCCESS] AVAGuard libraries found.")
except ImportError as e:
    print(f"[CRITICAL ERROR] Libraries not installed. {e}")
    print("Run: pip install -e ./avaguard-core && pip install -e ./avaguard-cli")
    sys.exit(1)










# ============================================================================
# SETUP LOGGING
# ============================================================================
log_dir = Path(project_root) / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / f"avaguard_desktop_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logger = logging.getLogger(__name__)

# ============================================================================
# PYQT6 IMPORTS
# ============================================================================
print("Importing PyQt6...")
try:
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QPushButton, QTextEdit, QLabel, QProgressBar, QCheckBox,
        QTabWidget, QTableWidget, QTableWidgetItem,
        QHeaderView, QFileDialog, QLineEdit, QComboBox, QGroupBox, 
        QFormLayout, QSpinBox, QMenu, QToolBar, QStatusBar,
        QDialog, QDialogButtonBox, QListWidget, QListWidgetItem,
        QSplitter, QFrame
    )
    from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer, QSize, QUrl
    from PyQt6.QtGui import QColor, QFont, QIcon, QPalette, QBrush, QAction, QDesktopServices
    print("[SUCCESS] PyQt6 imported successfully")
except ImportError as e:
    print(f"[ERROR] PyQt6 not found. Install with: pip install PyQt6")
    logger.critical(f"PyQt6 import failed: {e}")
    sys.exit(1)

# ============================================================================
# CORE IMPORTS
# ============================================================================
print("Importing Core Libraries...")
try:
    from avaguard_core.checks import AVAILABLE_CHECKS, FREE_TIER_CHECKS, PREMIUM_CHECKS
    from avaguard_core.checks.base_check import CheckResult, CheckStatus, CISSeverity, BaseCheck
    from avaguard_core.reporter import EnhancedReporter, ReportMetadata, ReportTier
    from avaguard_core.risk_scorer import RiskScorer
    from avaguard_core.auth import AzureAuthenticator
    from web_client import WebPortalClient
    from workers.sync_worker import SyncWorker
    from workers.scan_queue import ScanQueueManager, QueueItem
    from workers.check_runnable import CheckRunnable
    from workers.telemetry import PerformanceProfiler, ProviderMetricsTracker
    from models.evidence_store import EvidenceStore
    from workers.evidence_writer import EvidenceWriterThread
    print(f"[SUCCESS] Core imported. Found {len(AVAILABLE_CHECKS)} checks.")
except ImportError as e:
    print(f"[CORE IMPORT ERROR] {e}")
    AVAILABLE_CHECKS = {}
    FREE_TIER_CHECKS = {}
    PREMIUM_CHECKS = {}
    # Create dummy BaseCheck for type hints
    class BaseCheck: pass
    import traceback
    traceback.print_exc()
    sys.exit(1)

def check_internet(host="8.8.8.8", port=53, timeout=3):
    """Check for internet connectivity."""
    import socket
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

# ============================================================================
# ENHANCED DATABASE MANAGER (SRS-COMPLIANT)
# ============================================================================
from models.database import ScanMetadata, EnhancedDatabaseManager

class EnhancedScanWorker(QThread):
    """SRS-compliant enhanced scan worker."""
    
    # Signals
    log_message = pyqtSignal(str, str)  # message, level
    check_completed = pyqtSignal(object)  # CheckResult
    scan_progress = pyqtSignal(int, str)  # percent, status
    scan_finished = pyqtSignal(bool, ScanMetadata, list)  # success, metadata, results
    performance_metrics = pyqtSignal(dict)  # performance data
    session_revoked = pyqtSignal(str)  # Session revoked message
    scan_paused = pyqtSignal(bool)  # Pause state changed
    
    def __init__(self, use_mock: bool = True, config_path: str = None, tier: str = None, portal_url: str = None, access_token: str = None, db_path: str = None):
        super().__init__()
        self.use_mock = use_mock
        self.portal_url = portal_url
        self.access_token = access_token
        self.is_running = True
        self.client = None
        self.scan_results: List[CheckResult] = []
        self.scan_metadata = ScanMetadata()
        self.start_time: Optional[datetime] = None
        
        # Resolve DB path
        if not db_path:
            repo_root = os.path.dirname(project_root)
            self.db_path = os.path.join(repo_root, 'avaguard_enterprise.db')
        else:
            self.db_path = db_path
        
        # Configuration
        self.config = configparser.ConfigParser()
        self.config_path = config_path or os.path.join(project_root, 'config.ini')
        self.config.read(self.config_path)
        
        
        # FIX: Use the tier passed from UI, otherwise fallback to config
        config_tier = self.config.get('General', 'tier', fallback='FREE')
        self.tier = tier if tier else config_tier
        
        self.scan_metadata.tier = self.tier
        self.scan_metadata.environment = 'MOCK' if use_mock else 'LIVE'
        self.scan_metadata.initiated_by = self.config.get('General', 'user', fallback='system')
        
        # Check configuration
        self.check_config = {
            'inactivity_days': self.config.getint('Checks', 'inactivity_days', fallback=90),
            'exclude_guests': self.config.getboolean('Checks', 'exclude_guests', fallback=False),
            'tier': self.tier,
            'verbose': True,
            'tenant_id': self.config.get('Azure', 'tenant_id', fallback=''),
            'scan_id': self.scan_metadata.scan_id
        }
        
        # Performance tracking
        self.total_api_calls = 0
        self.check_timings: List[float] = []
        
        # Concurrency & scheduling
        self.is_paused = False
        self.queue_manager = ScanQueueManager()
        
        # Evidence store pipeline (Phase 2)
        self.evidence_store = EvidenceStore(self.db_path)
        self.evidence_writer = EvidenceWriterThread(self.evidence_store)
    
    def run(self):
        """Main scan execution loop."""
        
        # Debug: List all available checks
        try:
            from avaguard_core.checks import AVAILABLE_CHECKS, FREE_TIER_CHECKS, PREMIUM_CHECKS
            # Check if it's a dict or list
            if isinstance(AVAILABLE_CHECKS, dict):
                print(f"DEBUG: Total available checks: {len(AVAILABLE_CHECKS)}")
                print(f"DEBUG: Free tier checks: {len(FREE_TIER_CHECKS)}")
                print(f"DEBUG: Premium tier checks: {len(PREMIUM_CHECKS)}")
                
                # Show first few checks as example
                for i, (check_id, check_class) in enumerate(list(AVAILABLE_CHECKS.items())[:5]):
                    print(f"  - {check_id}: {check_class.TITLE if hasattr(check_class, 'TITLE') else check_class.__name__}")
                if len(AVAILABLE_CHECKS) > 5:
                    print(f"  ... and {len(AVAILABLE_CHECKS) - 5} more")
            else:
                print(f"DEBUG: AVAILABLE_CHECKS is a {type(AVAILABLE_CHECKS).__name__} with {len(AVAILABLE_CHECKS)} items")
                print("It should be a dictionary! Fix avaguard_core.checks.__init__.py")
        except Exception as e:
            print(f"DEBUG: Error importing checks: {e}")
            import traceback
            traceback.print_exc()

        self.start_time = datetime.now()
        self.scan_progress.emit(0, "Initializing...")
        
        try:
            # 1. Initialize
            if not self._initialize():
                self.scan_finished.emit(False, self.scan_metadata, [])
                return
            
            # 2. Select checks - NOW RETURNS DICTIONARY
            checks_dict = self._select_checks()
            if not checks_dict:
                self.log_message.emit("No checks available for selected tier", "error")
                self.scan_finished.emit(False, self.scan_metadata, [])
                return
            
            # Debug: Show what checks were selected
            print(f"DEBUG: Selected {len(checks_dict)} checks for {self.tier} tier:")
            for check_id, check_class in checks_dict.items():
                class_name = check_class.__name__ if check_class else "None"
                print(f"  - {check_id}: {class_name}")
            
            total_checks = len(checks_dict)
            self.scan_metadata.total_checks = total_checks
            self.log_message.emit(f"Running {total_checks} checks ({self.tier} Tier)", "info")
            
            # Start background evidence writer pipeline
            self.evidence_writer.start()
            
            try:
                # 3. Execute checks - PASS THE DICTIONARY
                self._execute_checks(checks_dict)
            finally:
                # Ensure all evidence is flushed to disk cleanly
                self.log_message.emit("Flushing evidence database...", "info")
                self.evidence_writer.stop()
            
            if not self.is_running:
                self.log_message.emit("Scan cancelled", "warning")
                self.scan_finished.emit(False, self.scan_metadata, self.scan_results)
                return
            
            # 4. Calculate metrics
            self._calculate_metrics()
            
            # 5. Generate reports
            self._generate_reports()
            
            # 6. Emit success
            self.scan_progress.emit(100, "Completed")
            self.scan_finished.emit(True, self.scan_metadata, self.scan_results)
            
        except Exception as e:
            error_msg = f"Critical error: {str(e)}"
            logger.exception(error_msg)
            self.log_message.emit(error_msg, "error")
            self.scan_finished.emit(False, self.scan_metadata, self.scan_results)
    
    def _initialize(self) -> bool:
        """Initialize scan client with better error handling."""
        try:
            if self.use_mock:
                self.log_message.emit("Initializing mock client...", "info")
                
                # mock_file = self.config.get('General', 'mock_data_file',
                #                            fallback='AVAMockData.json')
                
                mock_file = self.config.get('General', 'mock_data_file',
                                           fallback='datasets/failure_0.json')

                mock_path_obj = pathlib.Path(mock_file).expanduser().resolve()
                
                # If absolute path doesn't exist, try resolving against project roots
                if not mock_path_obj.exists():
                    for base in [project_root, ava_root]:
                        attempt = (pathlib.Path(base) / mock_file).resolve()
                        if attempt.exists():
                            mock_path_obj = attempt
                            break
                
                if not mock_path_obj.exists():
                    self.log_message.emit(
                        f"Mock data not found. Attempted to load from: {mock_path_obj}",
                        "error"
                    )
                    return False
                
                mock_path = str(mock_path_obj)
                
                # Validate the file is readable JSON and check schema
                try:
                    import json
                    with open(mock_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                    if not isinstance(data, dict):
                        raise ValueError("Dataset must be a JSON object.")
                    if "users" not in data:
                        raise ValueError("Dataset missing 'users' key.")
                    
                    user_count = len(data["users"])
                    self.log_message.emit(f"Validating dataset... Found {user_count} users.", "info")
                    try:
                        pct = data.get("metadata", {}).get("config", {}).get("generation", {}).get("failure_injection_rate", 0)
                        self.expected_failure_pct = pct * 100
                        self.expected_failure_count = int(user_count * pct)
                        self.log_message.emit(f"Expected Failures: {self.expected_failure_count} ({self.expected_failure_pct}%)", "info")
                    except Exception as e:
                        self.expected_failure_count = -1
                        logger.warning(f"Could not parse expected failures: {e}")
                    if user_count < 1000:
                        raise ValueError(f"Dataset contains {user_count} users. Minimum required is 1000.")
                        
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    self.log_message.emit(
                        f"Selected dataset file is invalid or cannot be read: {e}",
                        "error"
                    )
                    return False
                except ValueError as ve:
                    self.log_message.emit(
                        f"Dataset Validation Error: {ve}",
                        "error"
                    )
                    return False
                
                try:
                    # Try new import first
                    try:
                        from avaguard.mock_graph_client import MockGraphAPIClient
                    except ImportError:
                        # Fallback to old location
                        from avaguard_core.mock_graph_client import MockGraphAPIClient
                    
                    self.log_message.emit(f"📂 Loading dataset from: {mock_path}", "info")
                    self.client = MockGraphAPIClient(mock_path)
                    
                    # Log scenario profile / failure rate to confirm correct dataset is driving logic
                    if hasattr(self.client, 'data') and 'metadata' in self.client.data:
                        meta = self.client.data['metadata']
                        fail_rate = meta.get('config', {}).get('generation', {}).get('failure_injection_rate', 'unknown')
                        self.log_message.emit(f"✓ Dataset loaded: {os.path.basename(mock_path)} (Failure Rate: {fail_rate})", "success")
                        logger.info(f"Loaded dataset {mock_path} fresh for this scan run. Failure Rate: {fail_rate}")
                    else:
                        self.log_message.emit(f"✓ Mock data loaded: {os.path.basename(mock_path)}", "success")
                        logger.info(f"Loaded dataset {mock_path} fresh for this scan run.")
                    return True
                except ImportError as e:
                    self.log_message.emit(f"Mock client import failed: {e}", "error")
                    return False
            else:
                # Live Azure client initialization
                self.log_message.emit("Initializing Azure client...", "info")
                
                tenant_id = self.config.get('Azure', 'tenant_id', fallback='')
                client_id = self.config.get('Azure', 'client_id', fallback='')
                client_secret = self.config.get('Azure', 'client_secret', fallback='')
                
                if not all([tenant_id, client_id, client_secret]):
                    self.log_message.emit("Azure credentials not configured", "error")
                    return False
                
                try:
                    from avaguard_core.auth import AzureAuthenticator
                    from avaguard_core.graph_api_client import GraphAPIClient
                    
                    authenticator = AzureAuthenticator(tenant_id, client_id, client_secret)
                    access_token = authenticator.get_token()
                    self.client = GraphAPIClient(access_token)
                    self.log_message.emit("✓ Azure authentication successful", "success")
                    return True
                except Exception as e:
                    self.log_message.emit(f"Azure authentication failed: {e}", "error")
                    return False
                    
        except Exception as e:
            self.log_message.emit(f"Initialization failed: {str(e)}", "error")
            logger.exception("Client initialization error")
            return False
    











    def _select_checks(self) -> Dict[str, Type[BaseCheck]]:
        """
        Select checks based on tier, configuration, and portal active policies.
        
        Returns:
            Dictionary mapping check IDs to their class objects
        """
        from avaguard_core.checks import AVAILABLE_CHECKS, FREE_TIER_CHECKS
        
        # 1. Determine base selection based on Tier
        if self.tier == 'PREMIUM':
            selected_checks = AVAILABLE_CHECKS.copy()
        else:
            selected_checks = FREE_TIER_CHECKS.copy()
            
        # 2. Fetch Active Policies from Portal if available
        policy_check_ids = None
        if self.portal_url and self.access_token:
            try:
                from web_client import WebPortalClient, AuthToken, SessionRevokedException
                from datetime import timedelta
                client = WebPortalClient(self.portal_url)
                client._token = AuthToken(
                    access_token=self.access_token,
                    refresh_token="",
                    expires_at=datetime.now() + timedelta(hours=1),
                    user_email="",
                    user_role="",
                    organization_id=""
                )
                success, policies = client.get_active_policies()
                if success and isinstance(policies, list):
                    policy_check_ids = [p.get('check_id') for p in policies if p.get('check_id')]
                    self.log_message.emit(f"Fetched {len(policy_check_ids)} active policies from portal", "info")
                else:
                    self.log_message.emit("Could not fetch active policies — using local config", "warning")
            except Exception as e:
                # A 403/revoked error on policy fetch does NOT mean the current session
                # is globally revoked — the portal may reject stale policy queries.
                # Fall back to local config silently.
                if 'revoked' in str(e).lower() or e.__class__.__name__ in ('SessionRevokedException', 'SessionRevokedError'):
                    logger.warning(f"Policy fetch returned revoked-session error: {e}. Falling back to local config.")
                    self.log_message.emit("Portal policy fetch rejected (stale session data) — using local config", "warning")
                else:
                    self.log_message.emit(f"Error fetching active policies: {e}", "error")
        
        # 3. Filter by configuration and policies
        enabled_checks = self.config.get('Checks', 'enabled_checks', fallback='')
        if enabled_checks:
            enabled_list = [c.strip() for c in enabled_checks.split(',') if c.strip()]
            
            # If we fetched policies from the portal and there are active policies, intersect with them
            if policy_check_ids:
                enabled_list = [c for c in enabled_list if c in policy_check_ids]
                
            filtered_checks = {}
            ignored_checks = []

            for check_id in enabled_list:
                if check_id in selected_checks:
                    filtered_checks[check_id] = selected_checks[check_id]
                else:
                    ignored_checks.append(check_id)
            
            if ignored_checks:
                logger.warning(f"Ignored checks (invalid ID, disabled by policy, or not in {self.tier} tier): {ignored_checks}")
            
            selected_checks = filtered_checks
            
        # If no local config was used, but we have active policies, filter by policies
        elif policy_check_ids:
            filtered_checks = {}
            for check_id in policy_check_ids:
                if check_id in selected_checks:
                    filtered_checks[check_id] = selected_checks[check_id]
            selected_checks = filtered_checks
            
        logger.info(f"Selected {len(selected_checks)} checks for tier: {self.tier}")
        return selected_checks


    def _execute_checks(self, checks_dict: Dict[str, Type[BaseCheck]]):
        """Execute all selected checks concurrently using QThreadPool, ScanQueueManager, and telemetry."""
        from PyQt6.QtCore import QThreadPool, QCoreApplication
        
        if not checks_dict or not self.is_running:
            return []

        total = len(checks_dict)
        logger.info(f"Running {total} checks ({self.tier} Tier) concurrently")
        self.log_message.emit(f"Initializing concurrent execution queue ({total} checks)...", "info")

        # Telemetry & Profiler Setup
        profiler = PerformanceProfiler.get_instance()
        metrics_tracker = ProviderMetricsTracker()
        
        # We default provider to "mock" or "azure"
        default_provider = "mock" if self.use_mock else "azure"
        
        # Clean queue manager
        self.queue_manager.clear()

        # Enqueue all checks as QueueItems
        for check_id, check_class in checks_dict.items():
            # Estimate duration based on metrics
            prov_metrics = metrics_tracker.get_metrics(default_provider)
            est_duration = prov_metrics.get("estimated_check_duration_ms", 150.0)
            
            # Extract severity
            severity = "LOW"
            if hasattr(check_class, "SEVERITY") and check_class.SEVERITY:
                severity = str(check_class.SEVERITY)
            elif hasattr(check_class, "TITLE") and "mfa" in str(check_class.TITLE).lower():
                severity = "HIGH"
                
            item = QueueItem(
                check_id=check_id,
                check_class_name=check_class.__name__,
                provider_id=default_provider,
                severity=severity,
                estimated_duration_ms=est_duration
            )
            self.queue_manager.enqueue(item)
            
        logger.info(f"Enqueued {self.queue_manager.size()} items to the ScanQueueManager.")

        results = []
        active_checks = {}  # check_id -> QueueItem
        
        # Setup signals/slots for async processing
        def check_started(c_id):
            logger.debug(f"Check {c_id} execution started in thread pool.")

        def check_completed(res, timing):
            nonlocal active_checks
            c_id = res.check_id
            if c_id in active_checks:
                item = active_checks.pop(c_id)
                provider = item.provider_id
                
                # Check status and record telemetry/AIMD adjustments
                duration_ms = timing.total_wall_time_ms
                self.check_timings.append(duration_ms / 1000.0)
                
                # Feed to AIMD
                is_429 = res.status == CheckStatus.ERROR and "429" in (res.error_message or "").lower()
                if is_429:
                    self.queue_manager.record_throttle(provider)
                    metrics_tracker.record_throttle(provider)
                elif res.status == CheckStatus.ERROR:
                    self.queue_manager.record_error(provider)
                    metrics_tracker.record_error(provider)
                else:
                    self.queue_manager.record_success(provider, duration_ms)
                    metrics_tracker.record_success(provider, duration_ms)
                
                # Performance profiling instrumentation
                with profiler.context(f"check/{c_id}"):
                    if hasattr(res, 'api_calls_count'):
                        self.total_api_calls += getattr(res, 'api_calls_count', 0)
                
                # Phase 2: Evidence classification & background storage pipeline
                try:
                    raw_evidence = getattr(res, 'evidence', None)
                    if raw_evidence:
                        # Ensure raw_evidence is a list of resource dicts for classification
                        if isinstance(raw_evidence, dict):
                            raw_resources = [raw_evidence]
                        elif isinstance(raw_evidence, list):
                            raw_resources = raw_evidence
                        else:
                            raw_resources = [{"details": str(raw_evidence)}]
                            
                        # Classify evidence into 4 tiers
                        from avaguard_core.providers.evidence import classify_evidence
                        classified = classify_evidence(raw_resources)
                        
                        # Bounded submit each tier to the background writer thread
                        retention_days = self.check_config.get('inactivity_days', 90)
                        
                        for tier_name, tier_payload in classified.items():
                            self.evidence_writer.submit(
                                scan_id=self.scan_metadata.scan_id,
                                check_id=c_id,
                                payload={tier_name: tier_payload},
                                classification=tier_name.upper(),
                                retention_days=retention_days
                            )
                except Exception as ee:
                    logger.error(f"Failed to process and queue evidence for check {c_id}: {ee}")

                results.append(res)
                self.scan_results.append(res)
                self._update_metadata_from_result(res)
                self.check_completed.emit(res)

                # Log results
                status = res.status.value if hasattr(res.status, 'value') else str(res.status)
                icon = "✓" if status == "PASS" else "✗" if status == "FAIL" else "!"
                self.log_message.emit(
                    f"  └─ [{icon} {status}] {res.details}",
                    "success" if status == "PASS" else "warning"
                )
                logger.info(f"Check {c_id} completed: {status}")

        def check_rate_limited(provider, retry_after):
            self.queue_manager.record_throttle(provider, retry_after)
            metrics_tracker.record_throttle(provider)
            self.log_message.emit(f"⚠️ Provider {provider} hit 429 rate limit. Backing off for {retry_after}s.", "warning")

        def check_error(c_id, err_msg):
            self.log_message.emit(f"Check {c_id} error signal received: {err_msg}", "error")

        # Set up QThreadPool
        thread_pool = QThreadPool.globalInstance()
        # Ensure thread pool limit is high enough, AIMD concurrency controller manages actual active dispatch counts
        thread_pool.setMaxThreadCount(16)

        # Cooperative execution loop
        while (self.queue_manager.size() > 0 or len(active_checks) > 0) and self.is_running:

            # Global revocation check
            if GlobalSessionManager().is_revoked():
                self.log_message.emit("Scan aborted by global session revocation token.", "warning")
                self.is_running = False
                logger.info(f"Scan cancellation started at {datetime.now().isoformat()}")
                self.scan_progress.emit(100, "Scan cancelled due to session revocation.")
                logger.info(f"Scan cancellation ended at {datetime.now().isoformat()}")
                raise SessionRevokedError("Session revoked during check execution")

            # Pause handling
            if self.is_paused:
                time.sleep(0.05)
                continue

            # Determine concurrency limit dynamically from AIMD
            controller = self.queue_manager.get_controller(default_provider)
            current_limit = controller.current_limit()

            # Emit concurrency telemetry periodic updates (throttle to 1Hz)
            now = time.time()
            if not hasattr(self, '_last_perf_emit') or (now - self._last_perf_emit) >= 1.0:
                self._last_perf_emit = now
                perf_metrics = {
                    'concurrency_limit': current_limit,
                    'active_threads': len(active_checks),
                    'queue_backlog': self.queue_manager.size()
                }
                self.performance_metrics.emit(perf_metrics)

            if len(active_checks) < current_limit:
                # Retrieve next execution task
                item = self.queue_manager.dequeue(default_provider)
                if item:
                    check_class = checks_dict.get(item.check_id)
                    if check_class:
                        active_checks[item.check_id] = item
                        
                        runnable = CheckRunnable(
                            check_id=item.check_id,
                            check_class=check_class,
                            client=self.client,
                            config=self.check_config
                        )
                        
                        # Connect slot signals
                        runnable.signals.started.connect(check_started, Qt.ConnectionType.DirectConnection)
                        runnable.signals.completed.connect(check_completed, Qt.ConnectionType.DirectConnection)
                        runnable.signals.rate_limited.connect(check_rate_limited, Qt.ConnectionType.DirectConnection)
                        runnable.signals.error.connect(check_error, Qt.ConnectionType.DirectConnection)
                        
                        # Dispatch task
                        thread_pool.start(runnable)
                        
                        # Progress status updates
                        title = getattr(check_class, 'TITLE', check_class.__name__)
                        progress_pct = int(((total - self.queue_manager.size() - len(active_checks)) / total) * 100)
                        self.scan_progress.emit(max(0, min(99, progress_pct)), f"Running: {title} (Concurrency: {len(active_checks)}/{current_limit})")
                        self.log_message.emit(f"Running: {title}...", "info")
                    else:
                        logger.error(f"Class mapping missing for check ID {item.check_id}")
                else:
                    # Queue dequeued None (circuit breaker open or queues empty while threads complete)
                    time.sleep(0.02)
            else:
                # Concurrency limit reached, wait for slots to open up
                time.sleep(0.02)

        # Wait for all running checks to finalize if scan stopped or completed
        while len(active_checks) > 0:
            time.sleep(0.02)

        actual_failures = sum(1 for r in results if r.status != CheckStatus.PASS)
        if hasattr(self, "expected_failure_count") and self.expected_failure_count >= 0:
            if actual_failures != self.expected_failure_count:
                logger.warning(f"SCAN SUMMARY DEVIATION: Expected {self.expected_failure_count} failures, but found {actual_failures}")
                self.log_message.emit(f"Validation Warning: Found {actual_failures} failures (Expected {self.expected_failure_count})", "warning")
            else:
                logger.info(f"SCAN SUMMARY VALIDATED: Exactly {actual_failures} failures detected as expected.")
                self.log_message.emit(f"Validation Match: Exactly {actual_failures} failures detected.", "success")
        
        # Save telemetry report on scan finish
        try:
            profiler.save_report()
        except Exception as te:
            logger.warning(f"Could not save telemetry report: {te}")

        return results






                
    
    def _update_metadata_from_result(self, result: CheckResult):
        """Update scan metadata from check result."""
        status = result.status.value if hasattr(result.status, 'value') else str(result.status)
        
        if status == "PASS":
            self.scan_metadata.passed_checks += 1
        elif status == "FAIL":
            self.scan_metadata.failed_checks += 1
        elif status == "ERROR":
            self.scan_metadata.error_checks += 1
        elif status == "WARNING":
            self.scan_metadata.warning_checks += 1
    
    def _calculate_metrics(self):
        """Calculate scan metrics."""
        total = self.scan_metadata.total_checks
        self.scan_metadata.overall_score = RiskScorer.calculate_score(self.scan_results)
        
        # Calculate duration
        if self.start_time:
            self.scan_metadata.duration_seconds = (datetime.now() - self.start_time).total_seconds()
        
        # Set API calls
        self.scan_metadata.api_calls_count = self.total_api_calls
        
        # Emit performance metrics
        perf_metrics = {
            'total_duration': self.scan_metadata.duration_seconds,
            'avg_check_duration': sum(self.check_timings) / len(self.check_timings) if self.check_timings else 0,
            'total_api_calls': self.total_api_calls,
            'checks_per_second': total / self.scan_metadata.duration_seconds if self.scan_metadata.duration_seconds > 0 else 0
        }
        self.performance_metrics.emit(perf_metrics)
    
    def _generate_reports(self):
        """Generate comprehensive reports."""
        try:
            self.log_message.emit("Generating reports...", "info")
            
            # Create reporter with SRS-compliant metadata
            reporter_metadata = ReportMetadata(
                scan_id=self.scan_metadata.scan_id,
                tier=ReportTier.ENTERPRISE if self.scan_metadata.tier == 'PREMIUM' else ReportTier.BASIC,
                environment=self.scan_metadata.environment,
                scope=self.scan_metadata.scope,
                initiated_by=self.scan_metadata.initiated_by,
                target_tenant=self.scan_metadata.target_tenant,
                overall_score=float(self.scan_metadata.overall_score),
                total_checks=self.scan_metadata.total_checks,
                passed_checks=self.scan_metadata.passed_checks,
                failed_checks=self.scan_metadata.failed_checks,
                error_checks=self.scan_metadata.error_checks
            )
            
            reporter = EnhancedReporter(
                output_dir=os.path.join(project_root, 'output', 'reports'),
                metadata=reporter_metadata
            )
            
            # Generate reports
            generated_files = reporter.generate_reports(
                self.scan_results,
                formats=["html", "json", "csv"]
            )
            
            # Log generated files
            for filepath in generated_files:
                if filepath and os.path.exists(filepath):
                    filename = os.path.basename(filepath)
                    ext = os.path.splitext(filename)[1].lstrip('.').upper()
                    self.log_message.emit(f"✓ {ext} report: {filename}", "success")
            
        except Exception as e:
            self.log_message.emit(f"Report generation failed: {str(e)}", "error")
            logger.exception("Report generation error")
    
    def on_revocation(self, reason: str = "Session Revoked"):
        """Explicitly trigger revocation sequence from external heartbeat."""
        self.is_running = False
        self.log_message.emit(f"⚠️ {reason}", "error")
        self.session_revoked.emit(reason)
        self.stop()
    
    def stop(self):
        """Stop the scan."""
        self.is_running = False
        if hasattr(self, "queue_manager"):
            self.queue_manager.clear()
        self.log_message.emit("Stopping scan...", "warning")

    def pause(self):
        """Pause the scan."""
        self.is_paused = True
        self.scan_paused.emit(True)
        self.log_message.emit("Scan paused.", "warning")

    def resume(self):
        """Resume the scan."""
        self.is_paused = False
        self.scan_paused.emit(False)
        self.log_message.emit("Scan resumed.", "info")
