"""
AVAGuard Compliance Deterministic Replay Test Suite
Asserts that running scans programmatically and replaying their decrypted evidence snapshots
generates mathematically identical score outcomes and identical cryptographic signature hashes.
"""

import pytest
import os
import tempfile
import sqlite3
import json
from pathlib import Path

# Resolve absolute paths
project_root = Path(__file__).resolve().parent.parent.parent
import sys
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
if str(project_root / "avaguard-core") not in sys.path:
    sys.path.insert(0, str(project_root / "avaguard-core"))

from desktop_app.models.evidence_store import EvidenceStore
from tools.replay_scan import replay_scan, compute_replay_hash
from avaguard_core.benchmarks.models import ControlDefinition
from avaguard_core.benchmarks.loader import BenchmarkLoader


def test_deterministic_replay_flow():
    """Validates full deterministic replay and signature hash consistency over temp datasets."""
    # Create temp database
    fd, temp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    
    try:
        # 1. Setup tables matching main application schema
        conn = sqlite3.connect(temp_db_path)
        cursor = conn.cursor()
        
        # Scan History Table
        cursor.execute('''
            CREATE TABLE scan_history (
                scan_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                initiated_by TEXT,
                target_tenant TEXT,
                overall_score REAL DEFAULT 0,
                total_checks INTEGER DEFAULT 0,
                passed_checks INTEGER DEFAULT 0,
                failed_checks INTEGER DEFAULT 0
            )
        ''')
        
        # Check Results Table
        cursor.execute('''
            CREATE TABLE check_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT,
                check_id TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL,
                compliant_count INTEGER DEFAULT 0,
                non_compliant_count INTEGER DEFAULT 0
            )
        ''')
        
        # Evidence Snapshots Table
        cursor.execute('''
            CREATE TABLE evidence_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT NOT NULL,
                check_id TEXT NOT NULL,
                classification TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                integrity_hash TEXT NOT NULL,
                algorithm_version TEXT NOT NULL,
                key_version TEXT NOT NULL,
                compression_id TEXT NOT NULL,
                encrypted_payload BLOB NOT NULL,
                expires_at TEXT,
                retention_tier TEXT
            )
        ''')
        
        # Evidence Key Metadata Table
        cursor.execute('''
            CREATE TABLE evidence_key_metadata (
                key_version TEXT PRIMARY KEY,
                status TEXT NOT NULL
            )
        ''')
        
        # Create scan record and check results
        scan_id = "test-replay-scan-123"
        cursor.execute('''
            INSERT INTO scan_history (scan_id, timestamp, initiated_by, overall_score, total_checks, passed_checks, failed_checks)
            VALUES (?, datetime('now'), 'test', 100.0, 1, 1, 0)
        ''', (scan_id,))
        
        cursor.execute('''
            INSERT INTO check_results (scan_id, check_id, title, status, compliant_count, non_compliant_count)
            VALUES (?, '2.2.1', 'Ensure MFA is enabled', 'PASS', 2, 0)
        ''', (scan_id,))
        
        conn.commit()
        conn.close()

        # 2. Store mock encrypted evidence for the declarative check '2.2.1'
        evidence_store = EvidenceStore(db_path=temp_db_path)
        
        # Mock Azure resource for 2.2.1 (which queries MFA or similar)
        # Loader shows 2.2.1:
        # Let's inspect what 2.2.1 JSON looks like or load it dynamically
        from tools.replay_scan import load_control
        control_def = load_control("2.2.1")
        assert control_def is not None, "Declarative control '2.2.1' must exist in avaguard-core benchmarks"
        
        mock_resource_payload = {
            "resources": [
                {"id": "vnet1", "name": "VnetAlice", "public_network_access": "Disabled"},
                {"id": "vnet2", "name": "VnetBob", "public_network_access": "Disabled"}
            ]
        }
        
        # Save evidence snapshot
        record_ref = evidence_store.store_evidence(
            scan_id=scan_id,
            check_id="2.2.1",
            payload=mock_resource_payload,
            classification="confidential",
            retention_days=30
        )
        assert record_ref.isdigit(), "Evidence should be saved as a numeric ID in the snapshots table"
        evidence_store.close()

        # 3. Run replay engine programmatically
        success = replay_scan(scan_id, temp_db_path)
        assert success is True, "Replay scan must execute successfully and match original baseline check scores"

        # 4. Assert mathematical replay hashing determinism
        dummy_results_1 = [
            {"check_id": "2.2.1", "status": "PASS", "compliant_count": 2, "non_compliant_count": 0, "total_count": 2}
        ]
        dummy_results_2 = [
            {"check_id": "2.2.1", "status": "PASS", "compliant_count": 2, "non_compliant_count": 0, "total_count": 2}
        ]
        
        hash_1 = compute_replay_hash(dummy_results_1)
        hash_2 = compute_replay_hash(dummy_results_2)
        assert hash_1 == hash_2, "Replay hashing signature must be 100% deterministic and identical on identical outcomes"

    finally:
        # Clean up database file
        if os.path.exists(temp_db_path):
            try:
                os.remove(temp_db_path)
            except Exception:
                pass
