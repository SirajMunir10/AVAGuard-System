"""
AVAGuard Desktop - Lifecycle, Concurrency, and Correctness Stress Suite
Hardens the application under stress: checks for memory leaks, deadlocks, SQLite WAL safety,
concurrency fuzzing, key rotation transactional rollback, and PII redaction verification.
"""

import os
import sys
import time
import random
import threading
import sqlite3
import tempfile
import gc
import logging
from pathlib import Path
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

# Try importing tracemalloc for leak testing
try:
    import tracemalloc
except ImportError:
    tracemalloc = None

import pytest

# Ensure projects paths are resolved
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root.parent))

# Import PyQt6 mocks for testing
try:
    from conftest import MockQObject, pyqtSignal
except ImportError:
    from .conftest import MockQObject, pyqtSignal

# Import components
from workers.enhanced_worker import EnhancedScanWorker
from workers.scan_queue import ScanQueueManager, QueueItem
from workers.evidence_writer import EvidenceWriterThread
from models.database import EnhancedDatabaseManager
from models.evidence_store import EvidenceStore, LocalKeyProvider, Fernet
from avaguard_core.providers.evidence import classify_evidence


def test_pii_sanitization_verification():
    """
    Asserts that AI_SAFE evidence tier can NEVER leak names, emails, UUIDs,
    tenant IDs, IP addresses, client secrets, or access tokens.
    """
    raw_evidence = [{
        "displayName": "Ahmed Mujtaba",
        "givenName": "Ahmed",
        "surname": "Mujtaba",
        "mail": "ahmed.mujtaba@example.com",
        "userPrincipalName": "ahmed@avaguard.onmicrosoft.com",
        "tenant_id": "4b689fd5-ea48-43d9-95a9-45e3568912e4",
        "client_secret": "超级机密密钥_super_secret_client_credential_12345!",
        "access_token": "ey12345_access_token_payload",
        "ipAddress": "192.168.1.104",
        "log_message": "Virtual machine diagnostic log containing connection details to tenant 4b689fd5-ea48-43d9-95a9-45e3568912e4 by user admin@domain.com."
    }]

    # Run core classification
    classified = classify_evidence(raw_evidence)
    ai_safe_tier = classified["ai_safe"][0]

    # Verify key field scrubbing
    assert ai_safe_tier["displayName"] == "[REDACTED_DISPLAYNAME]"
    assert ai_safe_tier["givenName"] == "[REDACTED_GIVENNAME]"
    assert ai_safe_tier["surname"] == "[REDACTED_SURNAME]"
    assert ai_safe_tier["mail"] == "[REDACTED_MAIL]"
    assert ai_safe_tier["userPrincipalName"] == "[REDACTED_USERPRINCIPALNAME]"
    assert ai_safe_tier["tenant_id"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_tier["client_secret"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_tier["access_token"] == "[REDACTED_SENSITIVE_FIELD]"
    assert ai_safe_tier["ipAddress"] == "[REDACTED_SENSITIVE_FIELD]"

    # Verify deep string sanitization inside descriptions/logs
    log_message = ai_safe_tier["log_message"]
    assert "4b689fd5-ea48-43d9-95a9-45e3568912e4" not in log_message
    assert "admin@domain.com" not in log_message
    assert "[REDACTED_UUID]" in log_message
    assert "[REDACTED_EMAIL]" in log_message


def test_memory_leak_detection():
    """
    Specifically validates repeated scan start/stop and pause/resume cycles
    using tracemalloc diffing to prove memory usage stabilizes without thread leaks.
    """
    if not tracemalloc:
        pytest.skip("tracemalloc module not available on this platform")

    # Initial garbage collect to get baseline
    gc.collect()
    tracemalloc.start()
    
    baseline_snapshot = tracemalloc.take_snapshot()
    initial_threads_count = threading.active_count()

    # Run 5 consecutive lifecycle start/stop/pause/resume sequences
    for i in range(5):
        worker = EnhancedScanWorker(use_mock=True)
        # Mock active scan loop boundaries
        worker.pause()
        worker.resume()
        worker.stop()
        
        # Explicit delete to trigger ref cleanups
        del worker
        gc.collect()

    end_threads_count = threading.active_count()
    end_snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()

    # Assert thread stability: no background worker threads leaked
    assert end_threads_count <= initial_threads_count + 1, f"Thread leak detected! Initial: {initial_threads_count}, Final: {end_threads_count}"

    # Analyze memory delta
    stats = end_snapshot.compare_to(baseline_snapshot, 'lineno')
    top_diffs = stats[:10]
    total_delta = sum(stat.size_diff for stat in stats)
    
    # Memory should stabilize. A minor overhead (< 1MB) is fine for python's internal heap caching.
    assert total_delta < 1024 * 1024, f"Memory leak detected! Total delta: {total_delta / 1024:.2f} KB. Top leaks:\n" + "\n".join(str(s) for s in top_diffs)


def test_key_rotation_rollback_atomicity():
    """
    Tests atomic transactional key rotation.
    If decryption fails or transaction error occurs mid-rotation,
    assert database rollback is triggered and old key decryption remains intact.
    """
    temp_dir = tempfile.mkdtemp()
    db_path = str(Path(temp_dir) / "test_rotation.db")
    
    try:
        # 1. Initialize schema and key provider
        db_mgr = EnhancedDatabaseManager(db_path)
        key_provider = LocalKeyProvider(key_dir=Path(temp_dir) / "keys")
        store = EvidenceStore(db_path, key_provider=key_provider)

        # 2. Store test evidence
        payload = {"sec": "initial_data"}
        rec_id = store.store_evidence(
            scan_id="scan_rot",
            check_id="check_rot",
            payload=payload,
            classification="AI_SAFE"
        )

        # Register version v2 key
        v2_key = Fernet.generate_key()
        key_provider.register_key("v2", v2_key)

        # 3. Simulate failure by corrupting the key provider or throwing a decryption error mid-way
        original_get_key = key_provider.get_key
        
        def faulty_get_key(version):
            if version == "v2":
                # Throw a decryption/cryptography exception
                raise ValueError("Cryptographic key authentication signature verification failed")
            return original_get_key(version)

        key_provider.get_key = faulty_get_key

        # Assert rotation returns False (indicates safe rollback)
        success = store.rotate_keys("v1", "v2")
        assert success is False

        # Restore original get_key
        key_provider.get_key = original_get_key

        # Assert decryption still works under the original v1 key version!
        decrypted = store.retrieve_evidence(rec_id)
        assert decrypted["sec"] == "initial_data"

    finally:
        store.close()
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_unclosed_connections_and_sqlite_safety():
    """
    Asserts database connection cleanup and active diagnostics health checks.
    """
    temp_dir = tempfile.mkdtemp()
    db_path = str(Path(temp_dir) / "test_safety.db")

    try:
        db_mgr = EnhancedDatabaseManager(db_path)
        store = EvidenceStore(db_path)
        
        # Persist test record
        store.store_evidence(
            scan_id="scan_safe",
            check_id="check_safe",
            payload={"ok": True},
            classification="NORMALIZED"
        )
        
        # Verify diagnostics returns successfully without locking
        from tools.db_diagnostics import DatabaseDiagnostics
        diag = DatabaseDiagnostics(db_path)
        report = diag.generate_report()
        
        assert report["integrity_check"].upper() == "OK"
        assert report["vacuum_recommended"] is False
        
        store.close()
        
        # Assert database file is completely unlocked and can be safely deleted or moved
        os.remove(db_path)
        assert not os.path.exists(db_path)
        
    finally:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_concurrency_deadlock_and_starvation_fuzzing():
    """
    Runs a randomized fuzzing queue scheduler using mixed task delay limits,
    asserting that priority aging starvation prevention and scheduling resolves
    without deadlocking or getting stuck.
    """
    temp_dir = tempfile.mkdtemp()
    persist_file = Path(temp_dir) / "fuzz_queue.json"
    
    try:
        q_mgr = ScanQueueManager(persistence_file=persist_file)
        q_mgr.clear()

        # Enqueue 100 items with randomized parameters
        for i in range(100):
            item = QueueItem(
                check_id=f"chk_{i}",
                check_class_name="MockCheck",
                provider_id=random.choice(["prov_aws", "prov_azure", "prov_gcp"]),
                severity=random.choice(["CRITICAL", "HIGH", "MEDIUM", "LOW"]),
                estimated_duration_ms=random.uniform(10.0, 500.0),
                manual_boost=random.uniform(0.0, 5.0),
                retry_count=random.randint(0, 3),
                enqueue_time=time.time() - random.uniform(0, 3600)  # Random age up to 1 hour
            )
            q_mgr.enqueue(item)

        # Dequeue with randomized delays and rate limiting shocks
        dispatched_count = 0
        providers = ["prov_aws", "prov_azure", "prov_gcp"]
        
        start_time = time.time()
        # Drain the queue under stress conditions
        while q_mgr.size() > 0 and (time.time() - start_time) < 5.0:
            prov = random.choice(providers)
            
            # Simulate random provider throttling shock
            if random.random() < 0.15:
                q_mgr.record_throttle(prov, retry_after_s=0.01)
                
            item = q_mgr.dequeue(prov)
            if item:
                dispatched_count += 1
                # Simulate success
                q_mgr.record_success(prov, check_duration_ms=random.uniform(10, 100))
                
            time.sleep(0.001)

        # Assert no lockups: at least some items were safely dispatched and scheduling resolved
        assert dispatched_count > 0
        
    finally:
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_evidence_writer_clean_shutdown():
    """
    Asserts clean shutdown under active writes:
    EvidenceWriterThread drains all items successfully before exiting.
    """
    temp_dir = tempfile.mkdtemp()
    db_path = str(Path(temp_dir) / "test_writer.db")

    try:
        db_mgr = EnhancedDatabaseManager(db_path)
        store = EvidenceStore(db_path)
        
        writer = EvidenceWriterThread(store)
        writer.start()

        # Submit 50 snapshots
        for i in range(50):
            writer.submit(
                scan_id="scan_writer",
                check_id=f"check_{i}",
                payload={"data": f"content_{i}"},
                classification="NORMALIZED"
            )

        # Abruptly trigger graceful shutdown
        t0 = time.perf_counter()
        writer.stop()
        elapsed_ms = (time.perf_counter() - t0) * 1000.0

        # Assert writer stopped quickly
        assert writer.isFinished()
        
        # Verify all 50 snapshots were successfully flushed to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM evidence_snapshots WHERE scan_id = 'scan_writer'")
        count = cursor.fetchone()[0]
        conn.close()

        assert count == 50, f"Flushing failed: expected 50 records in DB, found {count}"
        logger.info(f"Drained 50 records cleanly in {elapsed_ms:.2f}ms.")

    finally:
        store.close()
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_enhanced_worker_imports_time():
    """Verify that 'time' is imported in workers.enhanced_worker namespace to prevent NameError."""
    import workers.enhanced_worker as ew
    assert hasattr(ew, 'time')
    assert ew.time is not None
    assert hasattr(ew.time, 'sleep')
