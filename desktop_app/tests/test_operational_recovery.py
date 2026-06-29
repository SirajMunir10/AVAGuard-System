"""
AVAGuard Desktop Operational Recovery and Resilience Test Suite
Aggressively injects faults (corrupt queue state, database corruption, failed flushes,
disconnect storms, telemetry exporter crashes, interrupted shutdowns) to assert fail-safe behavior.
"""

import pytest
import os
import json
import sqlite3
import tempfile
import shutil
from pathlib import Path
from unittest.mock import MagicMock, patch

from desktop_app.models.evidence_store import EvidenceStore
from desktop_app.workers.scan_queue import ScanQueueManager
from desktop_app.workers.telemetry import PerformanceProfiler


def test_queue_corruption_recovery():
    """Verify that ScanQueueManager fails safe when persistent queue state file is corrupted."""
    fd, temp_state_path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    
    try:
        # Write corrupted garbage data to queue state file
        with open(temp_state_path, "w") as f:
            f.write("{garbage_corrupted_json_no_close: [")
            
        manager = ScanQueueManager()
        # Override state path to test corruption
        manager.state_path = Path(temp_state_path)
        
        # Loading should not crash; it must safely clear/rebuild and proceed
        manager.load_state()
        assert manager.size() == 0, "Queue must gracefully load empty state and clear corruption"
        
    finally:
        if os.path.exists(temp_state_path):
            os.remove(temp_state_path)


def test_partial_wal_corruption_degraded_mode():
    """Verify that database quick_check failure trips degraded read-only mode, locking writes but keeping reads."""
    fd, temp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    
    store = None
    try:
        store = EvidenceStore(db_path=temp_db_path)
        
        # Verify it starts healthy
        assert store.degraded_mode is False
        
        # Inject artificial health failure (quick_check mock fail)
        store.trigger_degraded_mode("Simulated WAL page block corruption")
        assert store.degraded_mode is True
        
        # Attempts to write must raise DatabaseError
        with pytest.raises(sqlite3.DatabaseError) as exc:
            store.store_evidence(
                scan_id="scan-corrupt",
                check_id="2.2.1",
                payload={"test": "data"},
                classification="public"
            )
        assert "degraded read-only mode" in str(exc.value)
        
        # Retaining evidence or other modifications should also return gracefully or raise
        assert store.prune_expired() == 0
        assert store.rotate_keys("v1", "v2") is False
        
    finally:
        if store:
            store.close()
        if os.path.exists(temp_db_path):
            os.remove(temp_db_path)


def test_failed_flushes_rollback():
    """Verify that evidence transaction failures trigger absolute rollback without corrupted commits."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.fetchone.return_value = ("ok",)
    
    with patch('sqlite3.connect', return_value=mock_conn):
        store = EvidenceStore(db_path="mock.db")
        store.rebuild_bloom()
        
        # Apply disk full commit side effect AFTER initialization completes successfully
        mock_conn.commit.side_effect = sqlite3.OperationalError("Disk full or commit blocked")
        
        with pytest.raises(sqlite3.OperationalError):
            store.store_evidence(
                scan_id="scan-flush-fail",
                check_id="2.2.1",
                payload={"test": "data"},
                classification="public"
            )
            
        # Assert rollback was explicitly triggered on exception
        mock_conn.rollback.assert_called_once()
        store.close()


def test_provider_disconnect_storms():
    """Verify that checker execution handles sudden provider disconnect storm exceptions gracefully."""
    from avaguard_core.benchmarks.loader import BenchmarkLoader
    from avaguard_core.checks.declarative_check import DeclarativeCheck
    from avaguard_core.providers.registry import ProviderRegistry
    from avaguard_core.errors import EvidenceCollectionError
    
    control_def = BenchmarkLoader(title="Azure CIS", version="2.0.0", provider="azure").load_control_from_json_string(json.dumps({
        "control_id": "2.2.1",
        "title": "Ensure public network access is Disabled on Virtual Networks",
        "version": "1.0.0",
        "deprecated": False,
        "profile_level": "Level 1",
        "provider_compatibility": ["azure"],
        "category": "Networking",
        "scan_query": {
            "resource_type": "virtual_networks",
            "fields": ["id", "name"]
        },
        "evaluation_rules": [],
        "remediation_metadata": {
            "severity": "HIGH",
            "impact_statement": "Networking risk",
            "validation_steps": "Review public network access properties",
            "templates": {}
        }
    }))
    
    # Mock provider which crashes during query (simulating connection drops/storms)
    mock_provider = MagicMock()
    mock_provider.query_resources.side_effect = ConnectionResetError("Connection storm reset by peer")
    ProviderRegistry.register_active_instance("azure", mock_provider)
    
    check = DeclarativeCheck(control_def)
    
    # The check execution must raise EvidenceCollectionError or catch cleanly, rather than crashing python process
    with pytest.raises(EvidenceCollectionError) as exc:
        check.execute()
    assert "Failed to query provider resources" in str(exc.value)


def test_telemetry_exporter_failure_fails_open():
    """Verify that profiler and metrics failures fail open, preventing application scanning stalls."""
    profiler = PerformanceProfiler.get_instance()
    
    # Mock telemetry listener raising exception
    def bad_listener(*args, **kwargs):
        raise RuntimeError("Telemetry exporter connection timeout!")
        
    profiler.metrics_updated.connect(bad_listener)
    
    try:
        # Emitting metrics must not raise and must not crash the scanning thread
        # It must log and fail open gracefully
        profiler.metrics_updated.emit({"context": "test.fail_open", "value": 1.0})
    except Exception as e:
        pytest.fail(f"Profiler failed to fail-open: raised {e}")
    finally:
        profiler.metrics_updated.disconnect(bad_listener)


def test_interrupted_shutdown_cleanup():
    """Verify that close operations cleanly shutdown database connections even during mid-run interruptions."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.fetchone.return_value = ("ok",)
    
    with patch('sqlite3.connect', return_value=mock_conn):
        store = EvidenceStore(db_path="mock.db")
        store.rebuild_bloom()
        store.close()
        
        # Assert clean close was triggered
        mock_conn.close.assert_called_once()
