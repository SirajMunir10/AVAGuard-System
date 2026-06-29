"""
AVAGuard - Evidence Store Benchmarks Harness
Measures encrypted insert throughput, concurrent reads, compression ratios, Bloom filter deduplication,
and database pruning latencies.
"""

import time
import os
import shutil
import tempfile
import random
import hashlib
import sqlite3
from typing import Dict, Any, List
from pathlib import Path
from models.database import EnhancedDatabaseManager
from models.evidence_store import EvidenceStore, LocalKeyProvider, ZlibCompression, ZstdCompression, Lz4Compression

# Optional imports
try:
    import pyzstd
except ImportError:
    pyzstd = None
try:
    import lz4.block as lz4_block
except ImportError:
    lz4_block = None


def run_benchmarks(num_records: int = 200) -> Dict[str, Any]:
    """
    Stresses the local compliance storage engine to track latency distributions.
    """
    results = {}
    
    # 1. Setup temporary workspace
    temp_dir = tempfile.mkdtemp()
    db_path = str(Path(temp_dir) / "bench_evidence.db")
    
    # Pre-initialize schema using database manager
    db_mgr = EnhancedDatabaseManager(db_path)
    
    key_dir = Path(temp_dir) / "keys"
    
    # Injected key provider in temp folder to avoid cluttering user home keys
    key_provider = LocalKeyProvider(key_dir=key_dir)
    store = EvidenceStore(db_path, key_provider=key_provider)
    
    # Generate mock payloads of mixed sizes: small (<1KB), medium (10KB), large (150KB)
    payload_small = {"compliance_status": "PASS", "resources": [{"id": f"res_{i}"} for i in range(5)]}
    payload_medium = {"compliance_status": "FAIL", "resources": [{"id": f"res_{i}", "details": "Detailed resource compliance properties and configuration metadata describing the exact rules checked."} for i in range(50)]}
    payload_large = {"compliance_status": "FAIL", "resources": [{"id": f"res_{i}", "details": "Detailed resource compliance properties and configuration metadata describing the exact rules checked.", "raw_response": "A very large azure API JSON payload with extensive tenant policies, subscription permissions, active directory role definitions, network security group rules, storage account configurations, virtual machine profiles, key vault metadata, and nested properties repeating over and over to simulate production sizes."} for i in range(250)]}

    # Helper to measure compression ratios
    sample_data = str(payload_large).encode("utf-8")
    comp_ratios = {}
    
    zlib_comp = ZlibCompression()
    zlib_ratio = len(sample_data) / len(zlib_comp.compress(sample_data))
    comp_ratios["zlib"] = zlib_ratio
    
    if pyzstd:
        zstd_comp = ZstdCompression()
        zstd_ratio = len(sample_data) / len(zstd_comp.compress(sample_data))
        comp_ratios["zstd"] = zstd_ratio
        
    if lz4_block:
        lz4_comp = Lz4Compression()
        lz4_ratio = len(sample_data) / len(lz4_comp.compress(sample_data))
        comp_ratios["lz4"] = lz4_ratio
        
    results["compression_ratios"] = {
        "mean_ms": 0.0,
        "p50_ms": 0.0,
        "p95_ms": 0.0,
        "p99_ms": 0.0,
        "zlib_ratio": comp_ratios.get("zlib", 1.0),
        "zstd_ratio": comp_ratios.get("zstd", 0.0),
        "lz4_ratio": comp_ratios.get("lz4", 0.0),
        "description": "Adaptive compression ratios achieved on mixed payloads"
    }

    # 2. Encrypted Insert Throughput Benchmark
    insert_durations = []
    record_ids = []
    
    start_inserts = time.perf_counter()
    for i in range(num_records):
        # Choose mixed sizes
        if i % 10 == 0:
            payload = payload_large
        elif i % 3 == 0:
            payload = payload_medium
        else:
            payload = payload_small
            
        classification = random.choice(["RAW", "AI_SAFE", "AUDIT_SAFE", "NORMALIZED"])
        
        t0 = time.perf_counter()
        rec_id = store.store_evidence(
            scan_id=f"scan_{i // 50}",
            check_id=f"check_{i % 30}",
            payload=payload,
            classification=classification,
            retention_days=30 if i % 4 == 0 else 90
        )
        insert_durations.append((time.perf_counter() - t0) * 1000.0)
        record_ids.append(rec_id)
        
    total_insert_time = time.perf_counter() - start_inserts
    insert_throughput = num_records / total_insert_time if total_insert_time > 0 else 0.0
    
    insert_durations.sort()
    count = len(insert_durations)
    results["encrypted_insert"] = {
        "mean_ms": sum(insert_durations) / count,
        "p50_ms": insert_durations[int(count * 0.5)],
        "p95_ms": insert_durations[int(count * 0.95)],
        "p99_ms": insert_durations[int(count * 0.99)],
        "throughput_ops_sec": insert_throughput,
        "description": "Encrypted evidence batch database insert latency"
    }

    # 3. Retrieval Latency Benchmark (with cryptographic decryption)
    retrieve_durations = []
    for rec_id in record_ids[:100]: # Sample first 100 entries
        t0 = time.perf_counter()
        store.retrieve_evidence(rec_id)
        retrieve_durations.append((time.perf_counter() - t0) * 1000.0)
        
    retrieve_durations.sort()
    count = len(retrieve_durations)
    results["evidence_retrieval"] = {
        "mean_ms": sum(retrieve_durations) / count,
        "p50_ms": retrieve_durations[int(count * 0.5)],
        "p95_ms": retrieve_durations[int(count * 0.95)],
        "p99_ms": retrieve_durations[int(count * 0.99)],
        "description": "Integrity hash verification, decryption, and decompression retrieval latency"
    }

    # 4. Bloom Filter vs DB lookup speed
    bloom_lookups = []
    db_lookups = []
    
    # Generate some random query hashes
    query_hashes = []
    for i in range(200):
        if i % 2 == 0 and record_ids:
            # Query existing hash (fetch hash from DB)
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT content_hash FROM evidence_snapshots LIMIT 1 OFFSET ?", (random.randint(0, len(record_ids)-1),))
            row = cursor.fetchone()
            query_hashes.append(row[0] if row else hashlib.sha256(str(i).encode()).hexdigest())
            conn.close()
        else:
            query_hashes.append(hashlib.sha256(str(i).encode()).hexdigest())

    # Bloom lookups
    for h in query_hashes:
        t0 = time.perf_counter()
        _ = store.bloom.contains(h)
        bloom_lookups.append((time.perf_counter() - t0) * 1000.0)

    # Database lookups
    conn = sqlite3.connect(db_path)
    for h in query_hashes:
        t0 = time.perf_counter()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM evidence_snapshots WHERE content_hash = ?", (h,))
        _ = cursor.fetchone()
        db_lookups.append((time.perf_counter() - t0) * 1000.0)
    conn.close()

    bloom_lookups.sort()
    db_lookups.sort()
    
    results["bloom_lookup_speed"] = {
        "mean_ms": sum(bloom_lookups) / len(bloom_lookups),
        "p50_ms": bloom_lookups[int(len(bloom_lookups) * 0.5)],
        "p95_ms": bloom_lookups[int(len(bloom_lookups) * 0.95)],
        "p99_ms": bloom_lookups[int(len(bloom_lookups) * 0.99)],
        "description": "In-memory Bloom filter membership query latency"
    }
    
    results["db_lookup_speed"] = {
        "mean_ms": sum(db_lookups) / len(db_lookups),
        "p50_ms": db_lookups[int(len(db_lookups) * 0.5)],
        "p95_ms": db_lookups[int(len(db_lookups) * 0.95)],
        "p99_ms": db_lookups[int(len(db_lookups) * 0.99)],
        "description": "SQLite indexed content-hash query lookup latency"
    }

    # 5. Retention Pruning Cost
    # Insert some expired records manually to test pruning
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    past_iso = "2020-01-01T00:00:00"
    for i in range(50):
        cursor.execute('''
            INSERT INTO evidence_snapshots 
            (scan_id, check_id, classification, content_hash, integrity_hash, 
             algorithm_version, key_version, compression_id, encrypted_payload, 
             expires_at, retention_tier)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            "scan_expired", f"check_{i}", "RAW", f"hash_exp_{i}", f"int_exp_{i}",
            "fernet_v1", "v1", "none", b"expired_data", past_iso, "hot"
        ))
    conn.commit()
    conn.close()

    t0 = time.perf_counter()
    pruned = store.prune_expired()
    prune_ms = (time.perf_counter() - t0) * 1000.0
    
    results["retention_pruning"] = {
        "mean_ms": prune_ms,
        "p50_ms": prune_ms,
        "p95_ms": prune_ms,
        "p99_ms": prune_ms,
        "records_pruned": pruned,
        "description": "Indexed database cursor bounding expired records pruning latency"
    }

    # Cleanup
    store.close()
    try:
        shutil.rmtree(temp_dir)
    except OSError:
        pass

    return results
