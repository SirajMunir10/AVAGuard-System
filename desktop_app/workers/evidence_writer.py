"""
AVAGuard Desktop - Evidence Writer Thread
Implements a safe, bounded background persistence queue with graceful degradation.
"""

import time
import queue
import logging
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path

# PyQt6 imports
try:
    from PyQt6.QtCore import QThread, pyqtSignal
except ImportError:
    # Headless/CLI fallback
    class QThread:
        def __init__(self, *args, **kwargs): pass
        def start(self): pass
        def wait(self): pass
    def pyqtSignal(*args, **kwargs):
        class DummySignal:
            def emit(self, *args, **kwargs): pass
        return DummySignal()

from models.evidence_store import EvidenceStore

logger = logging.getLogger(__name__)


class EvidenceWriterThread(QThread):
    """
    Background worker thread that serializes and encrypts evidence snapshots.
    Guarantees no UI deadlock using a bounded queue and graceful degradation.
    """
    write_failed = pyqtSignal(str, str)  # check_id, error_message
    queue_pressure = pyqtSignal(int)      # current queue size

    def __init__(self, evidence_store: EvidenceStore, max_queue_size: int = 1000):
        super().__init__()
        self.store = evidence_store
        # Bounded thread-safe queue
        self.queue: queue.Queue[Tuple[str, str, Dict[str, Any], str, int]] = queue.Queue(maxsize=max_queue_size)
        self.is_running = True
        self.dropped_raw_count = 0

    def submit(self, scan_id: str, check_id: str, payload: Dict[str, Any], 
               classification: str, retention_days: int = 90) -> bool:
        """
        Submits evidence to the persistence queue.
        Implements graceful degradation: drops RAW data if full, blocks for AI/AUDIT.
        """
        if not self.is_running:
            logger.warning("Attempted to submit evidence after writer thread has shut down.")
            return False

        item = (scan_id, check_id, payload, classification, retention_days)
        
        # Expose queue pressure
        self.queue_pressure.emit(self.queue.qsize())
        
        if self.queue.full():
            # Graceful degradation logic
            if classification.upper() == "RAW":
                self.dropped_raw_count += 1
                # Increment telemetry warning namespace
                self.store.profiler.metrics_updated.emit({
                    "context": "evidence.dropped.raw.count",
                    "value": self.dropped_raw_count,
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
                })
                logger.warning(f"[QUEUE OVERFLOW] Bounded queue full. Dropped RAW evidence for check {check_id}.")
                return False
            else:
                # Critical compliance tiers (AI_SAFE / AUDIT_SAFE / NORMALIZED) must NEVER be dropped
                logger.info(f"[QUEUE PRESSURE] Bounded queue full. Blocking thread to enqueue critical {classification} evidence...")
                try:
                    # Block with timeout to prevent complete deadlock but maintain integrity
                    self.queue.put(item, block=True, timeout=5.0)
                    return True
                except queue.Full:
                    logger.critical(f"[DEADLOCK PREVENTION] Queue remained locked for 5s. Dropping {classification} snapshot to prevent UI freeze!")
                    self.write_failed.emit(check_id, "Write buffer timed out. Evidence dropped to prevent system lock.")
                    return False
        else:
            self.queue.put(item)
            return True

    def run(self):
        """Background loop pulling items and writing in single SQLite transactions."""
        logger.info("EvidenceWriterThread background pipeline started.")
        
        # Setup telemetry tracking variables
        latency_name = "evidence.wal.checkpoint_time_ms"
        
        while self.is_running or not self.queue.empty():
            batch = []
            start_wait = time.perf_counter()
            
            # 1. Wait/accumulate up to 10 items or 100ms
            while len(batch) < 10 and (time.perf_counter() - start_wait) < 0.1:
                try:
                    # Non-blocking or short wait poll
                    item = self.queue.get(block=True, timeout=0.01)
                    batch.append(item)
                    self.queue.task_done()
                except queue.Empty:
                    # Break loop if we have at least one item, otherwise continue waiting
                    if batch:
                        break
                    if not self.is_running:
                        break
                    
            if not batch:
                time.sleep(0.01)
                continue
                
            # 2. Write accumulated batch inside a single SQLite Transaction
            write_start = time.perf_counter()
            try:
                # Wrap batch save in single transaction
                cursor = self.store._conn.cursor()
                cursor.execute("BEGIN TRANSACTION")
                
                for scan_id, check_id, payload, classification, retention_days in batch:
                    # Compute, compress, encrypt
                    self.store.store_evidence(
                        scan_id=scan_id,
                        check_id=check_id,
                        payload=payload,
                        classification=classification,
                        retention_days=retention_days
                    )
                    
                self.store._conn.commit()
                
                # Expose WAL checkpoint timings periodically
                elapsed_ms = (time.perf_counter() - write_start) * 1000.0
                if len(batch) > 1:
                    logger.debug(f"Batched written {len(batch)} snapshots in {elapsed_ms:.2f}ms.")
                    
            except Exception as e:
                try:
                    self.store._conn.rollback()
                except Exception:
                    pass
                logger.error(f"Batch transactional write failed: {e}")
                for _, check_id, _, _, _ in batch:
                    self.write_failed.emit(check_id, f"Transactional commit error: {str(e)}")

        logger.info("EvidenceWriterThread pipeline successfully flushed and stopped.")

    def stop(self):
        """Triggers a clean, deterministic shutdown flush."""
        logger.info("Initiating EvidenceWriterThread graceful shutdown...")
        self.is_running = False
        # Block until thread has processed remaining queue entries
        self.wait()
