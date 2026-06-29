"""
Comprehensive database-engine-grade test suite for EvidenceStore and EvidenceWriterThread.
Covers WAL reliability, encryption integrity, deduplication, key rotation, and writer queue safety.
"""

import os
import json
import time
import hashlib
import sqlite3
import threading
import pytest
from pathlib import Path

from models.evidence_store import EvidenceStore, LocalKeyProvider, BloomFilter, ZlibCompression
from workers.evidence_writer import EvidenceWriterThread


@pytest.fixture
def temp_db(tmp_path):
    """Creates a temporary SQLite database initialized with version 4 schema."""
    db_file = tmp_path / "test_avaguard.db"
    
    # Initialize version 4 tables
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            scan_id TEXT PRIMARY KEY,
            timestamp TEXT NOT NULL,
            initiated_by TEXT,
            target_tenant TEXT,
            overall_score REAL DEFAULT 0,
            total_checks INTEGER DEFAULT 0,
            passed_checks INTEGER DEFAULT 0,
            failed_checks INTEGER DEFAULT 0,
            error_checks INTEGER DEFAULT 0,
            warning_checks INTEGER DEFAULT 0,
            tier TEXT,
            environment TEXT,
            scope TEXT,
            duration_seconds REAL DEFAULT 0,
            api_calls_count INTEGER DEFAULT 0,
            audit_id TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            synced BOOLEAN DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evidence_snapshots (
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
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            retention_tier TEXT DEFAULT 'hot',
            FOREIGN KEY (scan_id) REFERENCES scan_history(scan_id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evidence_key_metadata (
            key_version TEXT PRIMARY KEY,
            status TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            retired_at TEXT
        )
    ''')
    # Save a fake scan so foreign key constraint is satisfied if checked
    cursor.execute('''
        INSERT OR IGNORE INTO scan_history (scan_id, timestamp)
        VALUES ('scan-123', '2026-05-24T00:00:00')
    ''')
    conn.commit()
    conn.close()
    return str(db_file)


@pytest.fixture
def temp_keys(tmp_path):
    """Temporary key directory provider."""
    return LocalKeyProvider(key_dir=tmp_path / "keys")


def test_evidence_store_crud_and_integrity(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    payload = {"control": "1.1", "status": "COMPLIANT", "users": ["Stark", "Rogers"]}
    
    # Store evidence
    rec_id = store.store_evidence(
        scan_id="scan-123",
        check_id="1.1",
        payload=payload,
        classification="AI_SAFE",
        retention_days=30
    )
    assert rec_id.isdigit()
    
    # Retrieve evidence and assert correct restoration
    restored = store.retrieve_evidence(rec_id)
    assert restored["control"] == "1.1"
    assert restored["status"] == "COMPLIANT"
    assert "Stark" in restored["users"]


def test_corruption_simulation_and_integrity_check(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    payload = {"sensitive_field": "confidential"}
    
    rec_id = store.store_evidence(
        scan_id="scan-123",
        check_id="1.2",
        payload=payload,
        classification="AUDIT_SAFE"
    )
    
    # Simulate payload bit-rot/tampering in SQLite directly
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE evidence_snapshots SET encrypted_payload = x'ffffffff' WHERE id = ?", (rec_id,))
    conn.commit()
    conn.close()
    
    # Assert that accessing tampered payload raises ValueError due to cryptographic hash verification failure
    with pytest.raises(ValueError) as exc:
        store.retrieve_evidence(rec_id)
    assert "Integrity check failed" in str(exc.value)


def test_large_payload_encryption(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # Generate a large payload using random-looking (incompressible) data ~512KB
    # Using os.urandom ensures the compression ratio stays near 1x, safely below the 100x bomb guard.
    # This tests the full crypto/storage pipeline with a large but valid payload.
    import os as _os
    large_payload = {"data": _os.urandom(512 * 1024).hex()}  # ~512KB hex string (not compressible)
    
    rec_id = store.store_evidence(
        scan_id="scan-123",
        check_id="large_check",
        payload=large_payload,
        classification="RAW",
        retention_days=10
    )
    
    # Retrieve and verify complete matches
    restored = store.retrieve_evidence(rec_id)
    assert restored["data"] == large_payload["data"]


def test_bloom_filter_false_positive_graceful_fallback(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # Seed fake item in bloom filter to simulate False Positive (Bloom contains, DB does not)
    fake_hash = hashlib.sha256(b"non-existent").hexdigest()
    store.bloom.add(fake_hash)
    
    assert store.bloom.contains(fake_hash) is True
    
    # Direct database insertion check should gracefully complete since authority validation check occurs in DB
    rec_id = store.store_evidence(
        scan_id="scan-123",
        check_id="bloom_check",
        payload={"msg": "bloom_fp_check"},
        classification="AI_SAFE"
    )
    assert rec_id.isdigit()


def test_retention_pruning_under_load(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # Store immediate expiry snapshots (retention_days = -1 to force instant expiration)
    for i in range(15):
        store.store_evidence(
            scan_id="scan-123",
            check_id=f"prune_{i}",
            payload={"id": i},
            classification="RAW",
            retention_days=-1  # Instantly expired
        )
        
    # Store active snapshot (90 days)
    active_id = store.store_evidence(
        scan_id="scan-123",
        check_id="active_check",
        payload={"status": "active"},
        classification="AI_SAFE",
        retention_days=90
    )
    
    # Prune expired entries in tiny batches of 5 to stress check transactional loop
    pruned = store.prune_expired(batch_size=5)
    assert pruned == 15
    
    # Active snapshot must remain intact
    restored = store.retrieve_evidence(active_id)
    assert restored["status"] == "active"


def test_safe_transactional_key_rotation(temp_db, temp_keys):
    # Setup key provider with v1 and register a new v2 key
    temp_keys.register_key("v2", LocalKeyProvider.get_key(temp_keys, "v1"))  # temporary duplicate
    v2_secret = LocalKeyProvider(temp_keys.key_dir) # Reload keys
    v2_secret.register_key("v2", LocalKeyProvider.get_key(temp_keys, "v1"))
    
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # Write entries with active v1 key
    id_1 = store.store_evidence("scan-123", "1.1", {"k": 1}, "AI_SAFE")
    id_2 = store.store_evidence("scan-123", "1.2", {"k": 2}, "AI_SAFE")
    
    # Validate keys are v1
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT key_version FROM evidence_snapshots")
    versions = [r[0] for r in cursor.fetchall()]
    assert "v1" in versions
    conn.close()
    
    # Rotate v1 -> v2 in batches of 1
    success = store.rotate_keys(old_version="v1", new_version="v2", batch_size=1)
    assert success is True
    
    # Assert records are decryptable using rotated v2 keys
    assert store.retrieve_evidence(id_1)["k"] == 1
    assert store.retrieve_evidence(id_2)["k"] == 2


def test_key_rotation_failure_rollback(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # Write initial valid record
    id_1 = store.store_evidence("scan-123", "1.1", {"x": "intact"}, "AI_SAFE")
    
    # Register v2 key
    temp_keys.register_key("v2", LocalKeyProvider.get_key(temp_keys, "v1"))
    
    # Manually corrupt the integrity hash or encrypted payload in DB to cause decryption failure mid-rotation
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE evidence_snapshots SET encrypted_payload = x'00000000' WHERE id = ?", (id_1,))
    conn.commit()
    conn.close()
    
    # Attempting to rotate keys will fail mid-rotation on row decryption, triggering transactional ROLLBACK
    success = store.rotate_keys(old_version="v1", new_version="v2")
    assert success is False


def test_evidence_writer_bounded_queue_overflow(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    # Instantiate writer thread with a tiny queue capacity of 3
    writer = EvidenceWriterThread(evidence_store=store, max_queue_size=3)
    
    # We submit items without starting the thread to stress queue bounds
    # 1. Enqueue critical tiers
    assert writer.submit("scan-123", "c1", {"v": 1}, "AI_SAFE") is True
    assert writer.submit("scan-123", "c2", {"v": 2}, "AUDIT_SAFE") is True
    assert writer.submit("scan-123", "c3", {"v": 3}, "AI_SAFE") is True
    
    assert writer.queue.full() is True
    
    # 2. Submit a RAW tier item. Because queue is full, it should be gracefully DROPPED to avoid UI deadlock
    assert writer.submit("scan-123", "raw_overflow", {"heavy": "payload"}, "RAW") is False
    assert writer.dropped_raw_count == 1
    
    # 3. Submit an AI_SAFE tier. Because it is critical, it will block. 
    # Since thread is not running, it will timeout after 5s and drop to prevent freeze, returning False
    start_t = time.time()
    assert writer.submit("scan-123", "critical_overflow", {"secret": "val"}, "AI_SAFE") is False
    assert time.time() - start_t >= 4.5  # Asserts block timeout worked!


def test_evidence_writer_thread_batch_saving(temp_db, temp_keys):
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    writer = EvidenceWriterThread(evidence_store=store, max_queue_size=100)
    
    # Start thread
    writer.start()
    
    # Submit multiple checks under sustained burst
    ids = []
    for i in range(25):
        writer.submit("scan-123", f"burst_{i}", {"val": i}, "AI_SAFE")
        
    # Trigger clean shutdown flush
    writer.stop()
    
    # Verify that all 25 records were correctly committed and flushed
    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM evidence_snapshots WHERE check_id LIKE 'burst_%'")
    count = cursor.fetchone()[0]
    conn.close()
    
    assert count == 25


def test_concurrent_read_write_stress(temp_db, temp_keys):
    """Stress tests WAL concurrent read during active background writes."""
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    writer = EvidenceWriterThread(evidence_store=store, max_queue_size=500)
    
    writer.start()
    
    # Writer thread is enqueuing items rapidly
    def write_stress():
        for i in range(100):
            writer.submit("scan-123", f"stress_{i}", {"data": i}, "AI_SAFE")
            time.sleep(0.001)
            
    # Reader thread is reading existing items concurrently
    reader_exceptions = []
    def read_stress():
        # Store a sentinel
        sentinel_id = store.store_evidence("scan-123", "sentinel", {"key": "value"}, "AI_SAFE")
        for _ in range(50):
            try:
                res = store.retrieve_evidence(sentinel_id)
                assert res["key"] == "value"
                time.sleep(0.002)
            except Exception as e:
                reader_exceptions.append(e)
                
    t_write = threading.Thread(target=write_stress)
    t_read = threading.Thread(target=read_stress)
    
    t_write.start()
    t_read.start()
    
    t_write.join()
    t_read.join()
    
    writer.stop()
    
    # Assert no reader exceptions occurred (WAL concurrency validated!)
    assert len(reader_exceptions) == 0


def test_decompression_bomb_oversized_low_ratio():
    """Verify that decompression fails fast when uncompressed size exceeds 10MB even at low ratio."""
    import zlib
    # 10MB + 2048 bytes of pseudorandom data (cannot compress highly, yielding low ratio)
    raw_data = os.urandom(10 * 1024 * 1024 + 2048)
    compressed = zlib.compress(raw_data, level=1)
    
    with pytest.raises(ValueError) as exc:
        ZlibCompression().decompress(compressed)
    assert "Decompression bomb" in str(exc.value)


def test_decompression_bomb_high_ratio_small():
    """Verify that decompression fails fast when compression ratio exceeds 100x on small payload."""
    import zlib
    # 150KB of repeating characters compresses extremely well (yielding ~1000x ratio)
    raw_data = b"X" * 150000
    compressed = zlib.compress(raw_data)
    
    with pytest.raises(ValueError) as exc:
        ZlibCompression().decompress(compressed)
    assert "Decompression bomb" in str(exc.value)


def test_decompression_bomb_truncated_frame():
    """Verify that corrupted/invalid zlib frames are handled cleanly raising proper errors."""
    import zlib
    # b"\xde\xad\xbe\xef" has an invalid zlib magic number — always raises zlib.error
    with pytest.raises((ValueError, zlib.error)):
        ZlibCompression().decompress(b"\xde\xad\xbe\xef")


def test_json_payload_safety_checks(temp_db, temp_keys):
    """Verify nesting depth, max keys, max elements, and UTF-8 limits are enforced strictly."""
    store = EvidenceStore(db_path=temp_db, key_provider=temp_keys)
    
    # 1. Nesting Depth Violation (>15 levels)
    nested = {}
    curr = nested
    for _ in range(20):
        curr["child"] = {}
        curr = curr["child"]
        
    with pytest.raises(ValueError) as exc:
        store.store_evidence("scan-123", "nest", nested, "AI_SAFE")
    assert "nesting depth" in str(exc.value)
    
    # 2. Key Count Violation (>500 keys)
    large_keys = {f"key_{i}": i for i in range(600)}
    with pytest.raises(ValueError) as exc:
        store.store_evidence("scan-123", "keys", large_keys, "AI_SAFE")
    assert "key count" in str(exc.value)
    
    # 3. Array Element Count Violation (>5000 elements)
    large_array = {"array": list(range(6000))}
    with pytest.raises(ValueError) as exc:
        store.store_evidence("scan-123", "arr", large_array, "AI_SAFE")
    assert "Array element count" in str(exc.value)
    
    # 4. UTF-8 surrogate / invalid string strictness
    bad_surrogate = {"msg": "hello \ud800 world"}
    with pytest.raises(ValueError) as exc:
        store.store_evidence("scan-123", "utf8", bad_surrogate, "AI_SAFE")
    
    store.close()
