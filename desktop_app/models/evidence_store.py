"""
AVAGuard Desktop - High-Performance Encrypted Evidence Store
Implements core schema, WAL, cryptographic integrity checks, adaptive compression, and bloom filter deduplication.
"""

import os
import sys
import json
import time
import hashlib
import sqlite3
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Protocol
from pathlib import Path
from dataclasses import dataclass

# Try imports for advanced compression
try:
    import pyzstd
except ImportError:
    pyzstd = None

try:
    import lz4.block as lz4_block
except ImportError:
    lz4_block = None

from cryptography.fernet import Fernet
from workers.telemetry import PerformanceProfiler

logger = logging.getLogger(__name__)


# ── KEY PROVIDER ─────────────────────────────────────────────────────────────

class KeyProvider(Protocol):
    """Protocol for secure keyring key operations."""
    def get_key(self, version: str) -> bytes: ...
    def get_active_version(self) -> str: ...


class LocalKeyProvider:
    """
    Standard secure key provider.
    Saves keys securely in user home directory, falling back to OS-derived keys.
    """
    def __init__(self, key_dir: Optional[Path] = None):
        if key_dir:
            self.key_dir = key_dir
        else:
            self.key_dir = Path.home() / ".avaguard" / "keys"
        self.key_dir.mkdir(parents=True, exist_ok=True)
        
        # Load or generate active key version 'v1'
        self._keys: Dict[str, bytes] = {}
        self._active_version = "v1"
        self._load_keys()

    def _load_keys(self):
        # We try loading key files, otherwise write v1 key
        key_path = self.key_dir / "v1.key"
        if key_path.exists():
            try:
                with open(key_path, "rb") as f:
                    self._keys["v1"] = f.read().strip()
            except Exception as e:
                logger.error(f"Failed to read v1 key file: {e}")
                self._keys["v1"] = Fernet.generate_key()
        else:
            v1_key = Fernet.generate_key()
            self._keys["v1"] = v1_key
            try:
                with open(key_path, "wb") as f:
                    f.write(v1_key)
            except Exception as e:
                logger.warning(f"Could not save v1 key to file: {e}")

    def get_key(self, version: str) -> bytes:
        if version in self._keys:
            return self._keys[version]
        # Check on disk
        key_path = self.key_dir / f"{version}.key"
        if key_path.exists():
            try:
                with open(key_path, "rb") as f:
                    key_val = f.read().strip()
                    self._keys[version] = key_val
                    return key_val
            except Exception as e:
                logger.error(f"Failed to load key version {version}: {e}")
        
        # Fallback/default key to prevent complete execution crash
        logger.warning(f"Key version {version} not found. Generating a transient fallback key.")
        transient_key = Fernet.generate_key()
        self._keys[version] = transient_key
        return transient_key

    def get_active_version(self) -> str:
        return self._active_version

    def register_key(self, version: str, key_bytes: bytes):
        """Registers a new key for rotations."""
        self._keys[version] = key_bytes
        key_path = self.key_dir / f"{version}.key"
        try:
            with open(key_path, "wb") as f:
                f.write(key_bytes)
            logger.info(f"Registered new key version {version} to file system.")
        except Exception as e:
            logger.error(f"Failed to persist registered key {version}: {e}")

    def set_active_version(self, version: str):
        self._active_version = version


# ── COMPRESSION STRATEGY ──────────────────────────────────────────────────────

class CompressionStrategy(Protocol):
    def compress(self, data: bytes) -> bytes: ...
    def decompress(self, data: bytes) -> bytes: ...
    def algorithm_id(self) -> str: ...


class ZlibCompression:
    def compress(self, data: bytes) -> bytes:
        import zlib
        return zlib.compress(data, level=6)
    def decompress(self, data: bytes) -> bytes:
        import zlib
        compressed_len = len(data)
        if compressed_len == 0:
            return b""
        
        max_size = 10 * 1024 * 1024  # 10MB limit
        decompressor = zlib.decompressobj()
        uncompressed = bytearray()
        
        chunk_size = 65536  # 64KB chunks
        for i in range(0, compressed_len, chunk_size):
            chunk = data[i:i+chunk_size]
            decompressed_chunk = decompressor.decompress(chunk)
            uncompressed.extend(decompressed_chunk)
            
            uncompressed_len = len(uncompressed)
            ratio = uncompressed_len / max(1, compressed_len)
            
            if uncompressed_len > max_size or (uncompressed_len > 1024 and ratio > 100):
                raise ValueError(
                    f"Decompression bomb detected: uncompressed size ({uncompressed_len} B) "
                    f"exceeds 10MB absolute expansion or compression ratio ({ratio:.1f}x) exceeds 100x limit."
                )
        
        try:
            uncompressed.extend(decompressor.flush())
        except Exception:
            pass
            
        uncompressed_len = len(uncompressed)
        ratio = uncompressed_len / max(1, compressed_len)
        if uncompressed_len > max_size or (uncompressed_len > 1024 and ratio > 100):
            raise ValueError(
                f"Decompression bomb detected: uncompressed size ({uncompressed_len} B) "
                f"exceeds 10MB absolute expansion or compression ratio ({ratio:.1f}x) exceeds 100x limit."
            )
            
        return bytes(uncompressed)
    def algorithm_id(self) -> str:
        return "zlib"


class ZstdCompression:
    def compress(self, data: bytes) -> bytes:
        if pyzstd:
            return pyzstd.compress(data, level=3)
        return zlib_fallback_compress(data)
    def decompress(self, data: bytes) -> bytes:
        if pyzstd:
            try:
                frame_info = pyzstd.get_frame_info(data)
                uncompressed_size = getattr(frame_info, 'uncompressed_size', None)
                if uncompressed_size is not None and uncompressed_size > 0:
                    ratio = uncompressed_size / max(1, len(data))
                    if uncompressed_size > 10 * 1024 * 1024 or (uncompressed_size > 1024 and ratio > 100):
                        raise ValueError(
                            f"Decompression bomb detected (pre-scan): uncompressed size ({uncompressed_size} B) "
                            f"exceeds 10MB or ratio ({ratio:.1f}x) exceeds 100x limit."
                        )
            except Exception as e:
                if isinstance(e, ValueError) and "Decompression bomb" in str(e):
                    raise
            
            try:
                decompressed = pyzstd.decompress(data)
                uncompressed_len = len(decompressed)
                ratio = uncompressed_len / max(1, len(data))
                if uncompressed_len > 10 * 1024 * 1024 or (uncompressed_len > 1024 and ratio > 100):
                    raise ValueError(
                        f"Decompression bomb detected: uncompressed size ({uncompressed_len} B) "
                        f"exceeds 10MB or ratio ({ratio:.1f}x) exceeds 100x limit."
                    )
                return decompressed
            except Exception as e:
                if isinstance(e, ValueError) and "Decompression bomb" in str(e):
                    raise
                raise
        return zlib_fallback_decompress(data)
    def algorithm_id(self) -> str:
        return "zstd" if pyzstd else "zlib"


class Lz4Compression:
    def compress(self, data: bytes) -> bytes:
        if lz4_block:
            return lz4_block.compress(data)
        return zlib_fallback_compress(data)
    def decompress(self, data: bytes) -> bytes:
        if lz4_block:
            try:
                decompressed = lz4_block.decompress(data)
                uncompressed_len = len(decompressed)
                ratio = uncompressed_len / max(1, len(data))
                if uncompressed_len > 10 * 1024 * 1024 or (uncompressed_len > 1024 and ratio > 100):
                    raise ValueError(
                        f"Decompression bomb detected: uncompressed size ({uncompressed_len} B) "
                        f"exceeds 10MB or ratio ({ratio:.1f}x) exceeds 100x limit."
                    )
                return decompressed
            except Exception as e:
                if isinstance(e, ValueError) and "Decompression bomb" in str(e):
                    raise
                raise
        return zlib_fallback_decompress(data)
    def algorithm_id(self) -> str:
        return "lz4" if lz4_block else "zlib"


class NoCompression:
    def compress(self, data: bytes) -> bytes:
        return data
    def decompress(self, data: bytes) -> bytes:
        return data
    def algorithm_id(self) -> str:
        return "none"


def zlib_fallback_compress(data: bytes) -> bytes:
    import zlib
    return zlib.compress(data, level=6)

def zlib_fallback_decompress(data: bytes) -> bytes:
    return ZlibCompression().decompress(data)


class AdaptiveCompressor:
    """Selects compression algorithm per-payload size and system guidelines."""
    def select_strategy(self, data_size: int, tier: str) -> CompressionStrategy:
        if data_size < 1024:
            return NoCompression()
            
        # Hot tier prefers lz4 if available for rapid decompress
        if tier == "hot" and lz4_block:
            return Lz4Compression()
            
        # Large archive tier payloads prefer zstd
        if tier == "archive" and pyzstd and data_size > 102400:
            return ZstdCompression()
            
        # Default zlib baseline
        return ZlibCompression()

    def get_strategy_by_id(self, alg_id: str) -> CompressionStrategy:
        if alg_id == "zlib":
            return ZlibCompression()
        elif alg_id == "zstd" and pyzstd:
            return ZstdCompression()
        elif alg_id == "lz4" and lz4_block:
            return Lz4Compression()
        elif alg_id == "none":
            return NoCompression()
        else:
            logger.warning(f"Decompression algorithm '{alg_id}' unavailable, falling back to zlib.")
            return ZlibCompression()


# ── DEDUPLICATION BLOOM FILTER ────────────────────────────────────────────────

class BloomFilter:
    """
    Pure Python Bloom Filter.
    Acts strictly as a fast negative lookup accelerator.
    """
    def __init__(self, expected_items: int = 100000, fp_rate: float = 0.001):
        self.expected_items = expected_items
        self.fp_rate = fp_rate
        self.size = self._get_size(expected_items, fp_rate)
        self.hash_count = self._get_hash_count(self.size, expected_items)
        self.bit_array = [0] * self.size
        self.count = 0
        self.false_positive_assertions = 0

    def _get_size(self, n: int, p: float) -> int:
        import math
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _get_hash_count(self, m: int, n: int) -> int:
        import math
        k = (m / n) * math.log(2)
        return max(1, int(k))

    def _hashes(self, item: str) -> List[int]:
        # Generate hash indexes using salt values in hashlib MD5 and SHA-256
        res = []
        item_bytes = item.encode("utf-8")
        h1 = int(hashlib.md5(item_bytes).hexdigest(), 16)
        h2 = int(hashlib.sha256(item_bytes).hexdigest(), 16)
        
        for i in range(self.hash_count):
            # Double hashing scheme (Kirsch-Mitzenmacher optimization)
            idx = (h1 + i * h2) % self.size
            res.append(idx)
        return res

    def add(self, item: str):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1
        self.count += 1

    def contains(self, item: str) -> bool:
        """
        Check if item might be present.
        False represents a GUARANTEED negative lookup (absolutely does not exist).
        """
        for idx in self._hashes(item):
            if self.bit_array[idx] == 0:
                return False
        return True


def validate_payload_safety(data, depth=0):
    """
    Enforces strict JSON and payload safety checks:
    - Maximum nesting depth of 15 levels
    - Maximum key count of 500 keys per dictionary
    - Maximum array element count of 5000 elements per list
    - Strict UTF-8 decoding and verification on all strings/keys
    """
    if depth > 15:
        raise ValueError("JSON nesting depth exceeds maximum limit of 15 levels.")
        
    if isinstance(data, dict):
        if len(data) > 500:
            raise ValueError(f"Object key count ({len(data)}) exceeds maximum limit of 500.")
        for k, v in data.items():
            if not isinstance(k, str):
                k = str(k)
            try:
                k.encode('utf-8', errors='strict').decode('utf-8', errors='strict')
            except Exception:
                raise ValueError("Payload contains invalid non-UTF-8 keys.")
            validate_payload_safety(v, depth + 1)
            
    elif isinstance(data, list):
        if len(data) > 5000:
            raise ValueError(f"Array element count ({len(data)}) exceeds maximum limit of 5000.")
        for item in data:
            validate_payload_safety(item, depth + 1)
            
    elif isinstance(data, str):
        try:
            data.encode('utf-8', errors='strict').decode('utf-8', errors='strict')
        except Exception:
            raise ValueError("Payload contains invalid non-UTF-8 string content.")


# ── EVIDENCE STORE ENGINE ─────────────────────────────────────────────────────

class EvidenceStore:
    """
    High-performance, crash-safe local evidence store.
    Handles cryptographic envelope verification, adaptive compression, bloom deduplication,
    retention tier pruning, and transactional key rotations.
    """
    def __init__(self, db_path: str, key_provider: Optional[KeyProvider] = None):
        self.db_path = db_path
        self.key_provider = key_provider or LocalKeyProvider()
        self.compressor = AdaptiveCompressor()
        self.profiler = PerformanceProfiler.get_instance()
        self.degraded_mode = False
        
        # Initialize connection and apply WAL pragmas
        self._conn = sqlite3.connect(db_path, check_same_thread=False)
        self._apply_pragmas()
        
        # In-memory Bloom Filter
        self.bloom = BloomFilter(expected_items=100000, fp_rate=0.001)
        self.rebuild_bloom()
        
        # Validate initial database health
        self.check_database_health()

    def _apply_pragmas(self):
        """Applies database-engine-grade performance & reliability settings."""
        try:
            cursor = self._conn.cursor()
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=NORMAL")
            cursor.execute("PRAGMA cache_size=-65536")      # 64MB cache
            cursor.execute("PRAGMA mmap_size=268435456")    # 256MB mmap
            cursor.execute("PRAGMA page_size=4096")
            cursor.execute("PRAGMA temp_store=MEMORY")
            self._conn.commit()
            logger.info("Tuned SQLite WAL pragmas applied successfully.")
        except Exception as e:
            logger.error(f"Failed to apply SQLite pragmas: {e}")

    def check_database_health(self) -> bool:
        """
        Runs a quick integrity check on the database.
        If corruption is detected, enters degraded read-only mode,
        recommends backups, and logs critical recovery events.
        """
        try:
            cursor = self._conn.cursor()
            cursor.execute("PRAGMA quick_check")
            res = cursor.fetchone()
            if res and res[0] != "ok":
                self.trigger_degraded_mode(f"Integrity check failed: {res[0]}")
                return False
            return True
        except Exception as e:
            self.trigger_degraded_mode(f"Health check execution raised exception: {e}")
            return False

    def trigger_degraded_mode(self, reason: str):
        """Activates safe degraded read-only mode and logs recovery guidance."""
        self.degraded_mode = True
        self.profiler.metrics_updated.emit({
            "context": "evidence.corruption.recovery",
            "value": 1,
            "timestamp": datetime.now().isoformat()
        })
        logger.critical(
            f"⚠️ CRITICAL: Database corruption or health failure detected! Reason: {reason}\n"
            f"⚠️ RECOVERABILITY ACTION: EvidenceStore has entered SAFE DEGRADED READ-ONLY MODE.\n"
            f"⚠️ ACTION REQUIRED: Backup the database file '{self.db_path}' immediately before attempting repairs!"
        )

    def checkpoint_wal(self):
        """
        Executes an explicit WAL checkpoint and records performance observability metrics.
        Tracks WAL file size, checkpoint duration, and stall frequencies.
        """
        wal_path = Path(self.db_path + "-wal")
        wal_size_before = 0
        if wal_path.exists():
            try:
                wal_size_before = wal_path.stat().st_size
            except Exception:
                pass
                
        start_time = time.perf_counter()
        try:
            cursor = self._conn.cursor()
            cursor.execute("PRAGMA wal_checkpoint(TRUNCATE)")
            cursor.fetchone()
            
            duration_ms = (time.perf_counter() - start_time) * 1000.0
            
            # Observability metrics
            self.profiler.metrics_updated.emit({
                "context": "evidence.wal.checkpoint_duration_ms",
                "value": duration_ms,
                "timestamp": datetime.now().isoformat()
            })
            
            self.profiler.metrics_updated.emit({
                "context": "evidence.wal.size_bytes",
                "value": wal_size_before,
                "timestamp": datetime.now().isoformat()
            })
            
            is_stall = 1 if duration_ms > 150.0 else 0
            self.profiler.metrics_updated.emit({
                "context": "evidence.wal.stall_frequency",
                "value": is_stall,
                "timestamp": datetime.now().isoformat()
            })
            
            logger.info(f"WAL checkpoint executed in {duration_ms:.2f}ms. Size before: {wal_size_before} B. Stall: {bool(is_stall)}")
            
        except Exception as e:
            logger.error(f"WAL checkpoint failed: {e}")

    def rebuild_bloom(self):
        """Rebuilds Bloom Filter from stored evidence content hashes on startup."""
        start_time = time.perf_counter()
        try:
            cursor = self._conn.cursor()
            cursor.execute("SELECT content_hash FROM evidence_snapshots")
            rows = cursor.fetchall()
            
            # Reset Bloom filter
            self.bloom = BloomFilter(expected_items=max(100000, len(rows) * 2), fp_rate=0.001)
            for row in rows:
                self.bloom.add(row[0])
                
            elapsed_ms = (time.perf_counter() - start_time) * 1000.0
            logger.info(f"Rebuilt Bloom Filter in {elapsed_ms:.2f}ms with {len(rows)} entries.")
        except Exception as e:
            logger.error(f"Bloom Filter rebuild failed: {e}. Falling back to clean filter.")
            self.bloom = BloomFilter()

    def store_evidence(self, scan_id: str, check_id: str, payload: Dict[str, Any], 
                       classification: str, retention_days: int = 90) -> str:
        """
        Compresses, encrypts, validates integrity, and persists evidence payload
        observing strict crash-safe database constraints.
        """
        if self.degraded_mode:
            raise sqlite3.DatabaseError("Database is in degraded read-only mode. Write operations are strictly locked.")
            
        start_time = time.perf_counter()
        
        # Standardized metrics variables
        latency_name = "evidence.store.latency_ms"
        encrypt_name = "evidence.encrypt.latency_ms"
        compress_ratio_name = "evidence.compress.ratio"
        dedup_name = "evidence.dedup.hit_rate"
        
        with self.profiler.context("evidence/store"):
            # Enforce strict safety and payload constraints
            validate_payload_safety(payload)
            
            try:
                # 1. Serialization
                serialized = json.dumps(payload, default=str).encode("utf-8")
                raw_size = len(serialized)
                
                # 2. Compute canonical hash for deduplication
                content_hash = hashlib.sha256(serialized).hexdigest()
                
                # 3. Bloom filter fast negative lookup
                bloom_hit = self.bloom.contains(content_hash)
                
                # Double-check canonical database for safety if bloom hits (authority validation)
                if bloom_hit:
                    cursor = self._conn.cursor()
                    cursor.execute("SELECT id, scan_id FROM evidence_snapshots WHERE content_hash = ?", (content_hash,))
                    db_row = cursor.fetchone()
                    if db_row:
                        # Duplicate hit verified, return existing entry reference
                        logger.debug(f"Deduplication HIT for hash {content_hash[:8]}. Skipping store.")
                        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                        
                        # Record metrics
                        self.profiler.metrics_updated.emit({
                            "context": dedup_name,
                            "hit": 1,
                            "timestamp": datetime.now().isoformat()
                        })
                        return f"dup_ref_{db_row[0]}"
                    else:
                        # Bloom False Positive detected!
                        self.bloom.false_positive_assertions += 1
                        logger.debug("Bloom Filter False Positive detected.")

                # 4. Select Compression Strategy
                tier = "archive" if retention_days > 180 else "hot" if retention_days <= 30 else "warm"
                strategy = self.compressor.select_strategy(raw_size, tier)
                compressed = strategy.compress(serialized)
                comp_size = len(compressed)
                ratio = float(raw_size) / comp_size if comp_size > 0 else 1.0
                
                # 5. Encryption stage
                encrypt_start = time.perf_counter()
                active_key_version = self.key_provider.get_active_version()
                key = self.key_provider.get_key(active_key_version)
                fernet = Fernet(key)
                
                encrypted_blob = fernet.encrypt(compressed)
                encrypt_latency = (time.perf_counter() - encrypt_start) * 1000.0
                
                # 6. Compute Cryptographic Integrity Hash of final envelope payload
                integrity_hash = hashlib.sha256(encrypted_blob).hexdigest()
                
                # 7. Persist to DB using transaction
                expires_at = None
                if retention_days is not None and retention_days != 0:
                    expires_at = datetime.fromtimestamp(time.time() + (retention_days * 86400)).isoformat()
                
                cursor = self._conn.cursor()
                cursor.execute('''
                    INSERT INTO evidence_snapshots 
                    (scan_id, check_id, classification, content_hash, integrity_hash, 
                     algorithm_version, key_version, compression_id, encrypted_payload, 
                     expires_at, retention_tier)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    scan_id,
                    check_id,
                    classification,
                    content_hash,
                    integrity_hash,
                    "fernet_v1",
                    active_key_version,
                    strategy.algorithm_id(),
                    encrypted_blob,
                    expires_at,
                    tier
                ))
                
                record_id = cursor.lastrowid
                self._conn.commit()
                
                # 8. Add to Bloom Filter
                self.bloom.add(content_hash)
                
                # 9. Telemetry instrumentation
                elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                
                # Standardized namespaces
                self.profiler.metrics_updated.emit({"context": latency_name, "value": elapsed_ms, "timestamp": datetime.now().isoformat()})
                self.profiler.metrics_updated.emit({"context": encrypt_name, "value": encrypt_latency, "timestamp": datetime.now().isoformat()})
                self.profiler.metrics_updated.emit({"context": compress_ratio_name, "value": ratio, "timestamp": datetime.now().isoformat()})
                
                return str(record_id)
                
            except Exception as e:
                self._conn.rollback()
                logger.error(f"Core storage pipeline failure: {e}")
                raise

    def retrieve_evidence(self, record_id: str) -> Dict[str, Any]:
        """
        Retrieves, checks integrity, decrypts, and decompresses an evidence record.
        Strict verification occurs prior to executing decryption.
        """
        import hmac
        with self.profiler.context("evidence/retrieve"):
            try:
                # Strip duplicate prefix if returned by dedup
                if record_id.startswith("dup_ref_"):
                    actual_id = record_id.replace("dup_ref_", "")
                else:
                    actual_id = record_id
                    
                cursor = self._conn.cursor()
                cursor.execute('''
                    SELECT scan_id, check_id, classification, integrity_hash, algorithm_version, 
                           key_version, compression_id, encrypted_payload 
                    FROM evidence_snapshots 
                    WHERE id = ?
                ''', (actual_id,))
                
                row = cursor.fetchone()
                if not row:
                    raise KeyError(f"Evidence snapshot with ID {record_id} does not exist.")
                    
                (scan_id, check_id, classification, integrity_hash, alg_ver, 
                 key_ver, comp_id, encrypted_payload) = row
                 
                # 1. Database-engine-grade Cryptographic Integrity Verification
                computed_integrity = hashlib.sha256(encrypted_payload).hexdigest()
                if not hmac.compare_digest(computed_integrity, integrity_hash):
                    # Trip integrity alarm
                    self.profiler.metrics_updated.emit({
                        "context": "evidence.integrity.failure",
                        "value": 1,
                        "timestamp": datetime.now().isoformat()
                    })
                    logger.critical(f"INTEGRITY ERROR: Cryptographic verification mismatch on evidence {record_id}!")
                    raise ValueError(f"Integrity check failed. Evidence payload was truncated or corrupted.")

                # 2. Envelope Decryption
                key = self.key_provider.get_key(key_ver)
                fernet = Fernet(key)
                try:
                    compressed_payload = fernet.decrypt(encrypted_payload)
                except Exception as de:
                    # Telemetry counter for decrypt failures
                    self.profiler.metrics_updated.emit({
                        "context": "evidence.decrypt.failure",
                        "value": 1,
                        "timestamp": datetime.now().isoformat()
                    })
                    logger.critical(f"DECRYPT FAILURE: Cryptographic envelope decryption failed: {de}")
                    # Ensure cryptographic failures never expose partial decrypted payloads
                    raise ValueError("Decryption failed. Partial decrypted payload exposure was prevented.")

                # 3. Envelope Decompression
                strategy = self.compressor.get_strategy_by_id(comp_id)
                serialized = strategy.decompress(compressed_payload)
                
                # 4. Deserialization
                return json.loads(serialized.decode("utf-8"))
                
            except Exception as e:
                logger.error(f"Core retrieval pipeline failure for record {record_id}: {e}")
                raise

    def prune_expired(self, batch_size: int = 100) -> int:
        """
        Incremental retention pruning using indexed cursor bounds.
        Deletes in tiny chunks to avoid locking SQLite checkpoints.
        """
        if self.degraded_mode:
            logger.warning("Prune skipped: Database is in degraded read-only mode.")
            return 0
            
        start_time = time.perf_counter()
        pruned_count = 0
        now_str = datetime.fromtimestamp(time.time()).isoformat()
        
        with self.profiler.context("evidence/prune"):
            try:
                cursor = self._conn.cursor()
                while True:
                    # Query batches of expired rows using indexes
                    cursor.execute('''
                        SELECT id FROM evidence_snapshots 
                        WHERE expires_at < ? 
                        LIMIT ?
                    ''', (now_str, batch_size))
                    
                    rows = cursor.fetchall()
                    if not rows:
                        break
                        
                    ids_to_prune = [r[0] for r in rows]
                    
                    # Delete batch in transaction
                    cursor.execute(f'''
                        DELETE FROM evidence_snapshots 
                        WHERE id IN ({",".join("?" * len(ids_to_prune))})
                    ''', ids_to_prune)
                    
                    self._conn.commit()
                    pruned_count += len(ids_to_prune)
                    
                    # Yield slightly between transaction batches
                    time.sleep(0.01)
                    
                # Rebuild bloom filter on prune completion to recover false positive accuracy
                if pruned_count > 0:
                    self.rebuild_bloom()
                    
                elapsed_ms = (time.perf_counter() - start_time) * 1000.0
                self.profiler.metrics_updated.emit({
                    "context": "evidence.prune.duration_ms",
                    "value": elapsed_ms,
                    "timestamp": datetime.now().isoformat()
                })
                
                if pruned_count > 0:
                    logger.info(f"Pruned {pruned_count} expired records in {elapsed_ms:.2f}ms.")
                    
                return pruned_count
                
            except Exception as e:
                self._conn.rollback()
                logger.error(f"Prune execution failed: {e}")
                return 0

    def rotate_keys(self, old_version: str, new_version: str, batch_size: int = 50) -> bool:
        """
        Safe transactional incremental key rotation.
        Drives batches of decryptions/encryptions, rolling back failures safely.
        """
        if self.degraded_mode:
            logger.warning("Key rotation skipped: Database is in degraded read-only mode.")
            return False
            
        import hmac
        start_time = time.perf_counter()
        logger.info(f"Starting transactional key rotation from version {old_version} to {new_version}...")
        
        try:
            old_key = self.key_provider.get_key(old_version)
            new_key = self.key_provider.get_key(new_version)
            
            old_fernet = Fernet(old_key)
            new_fernet = Fernet(new_key)
        except Exception as e:
            logger.error(f"Key provider retrieval failed during rotation check: {e}")
            return False

        cursor = self._conn.cursor()
        
        while True:
            # Query next batch of records encrypted with the old key
            cursor.execute('''
                SELECT id, compression_id, integrity_hash, encrypted_payload FROM evidence_snapshots
                WHERE key_version = ?
                LIMIT ?
            ''', (old_version, batch_size))
            
            rows = cursor.fetchall()
            if not rows:
                break
                
            logger.info(f"Rotating batch of {len(rows)} evidence records...")
            
            try:
                # Process batch transactional envelope modifications
                for row_id, comp_id, integrity_hash, old_encrypted in rows:
                    # 1. Verify integrity of current envelope
                    row_hash = hashlib.sha256(old_encrypted).hexdigest()
                    if not hmac.compare_digest(row_hash, integrity_hash):
                        self.profiler.metrics_updated.emit({
                            "context": "evidence.integrity.failure",
                            "value": 1,
                            "timestamp": datetime.now().isoformat()
                        })
                        raise ValueError(f"Integrity check failed during rotation on record {row_id}")
                    
                    # 2. Decrypt envelope safely
                    try:
                        compressed = old_fernet.decrypt(old_encrypted)
                    except Exception:
                        self.profiler.metrics_updated.emit({
                            "context": "evidence.decrypt.failure",
                            "value": 1,
                            "timestamp": datetime.now().isoformat()
                        })
                        raise
                    
                    # 3. Re-encrypt using new version key
                    new_encrypted = new_fernet.encrypt(compressed)
                    new_integrity = hashlib.sha256(new_encrypted).hexdigest()
                    
                    # 4. Update row values in active transaction
                    cursor.execute('''
                        UPDATE evidence_snapshots
                        SET encrypted_payload = ?, integrity_hash = ?, key_version = ?
                        WHERE id = ?
                    ''', (new_encrypted, new_integrity, new_version, row_id))
                    
                # Commit successful batch
                self._conn.commit()
                
            except Exception as e:
                # Rollback current batch transaction safely, stopping rotation pipeline without corruption
                self._conn.rollback()
                self.profiler.metrics_updated.emit({
                    "context": "evidence.rollback.event",
                    "value": 1,
                    "timestamp": datetime.now().isoformat()
                })
                logger.error(f"FAIL-SAFE ROLLBACK: Incremental key rotation failed during batch processing: {e}")
                return False
                
        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        logger.info(f"Key rotation completed successfully in {elapsed_ms:.2f}ms.")
        return True

    def close(self):
        """Clean shutdown closing connections."""
        try:
            self._conn.close()
        except Exception:
            pass
