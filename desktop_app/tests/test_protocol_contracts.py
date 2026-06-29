"""
AVAGuard Protocol Contract Verification Test Suite
Verifies that concrete subsystem implementations satisfy runtime protocol guarantees.
"""

import pytest
import os
import tempfile
from typing import get_type_hints

from desktop_app.core.interfaces.protocols import (
    CompressionStrategyProtocol,
    EncryptionStrategyProtocol,
    EvidenceStoreProtocol,
    TelemetryProtocol,
    QueueManagerProtocol,
    ProviderProtocol
)
from desktop_app.models.evidence_store import (
    ZlibCompression,
    ZstdCompression,
    Lz4Compression,
    NoCompression,
    EvidenceStore,
    LocalKeyProvider
)
from desktop_app.workers.telemetry import PerformanceProfiler
from desktop_app.workers.scan_queue import ScanQueueManager


def test_compression_strategy_protocols():
    """Verify that all pluggable compression implementations satisfy the CompressionStrategyProtocol contract."""
    strategies = [
        ZlibCompression(),
        ZstdCompression(),
        Lz4Compression(),
        NoCompression()
    ]
    
    for strategy in strategies:
        # Runtime-checkable protocol assertions
        assert isinstance(strategy, CompressionStrategyProtocol), f"{strategy.__class__.__name__} fails CompressionStrategyProtocol"
        
        # Method verification
        assert hasattr(strategy, "compress")
        assert hasattr(strategy, "decompress")
        assert hasattr(strategy, "algorithm_id")
        assert isinstance(strategy.algorithm_id(), str)


def test_evidence_store_protocol():
    """Verify that EvidenceStore satisfies the EvidenceStoreProtocol contract."""
    # Create temp database to avoid collision
    fd, temp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    
    try:
        store = EvidenceStore(db_path=temp_db_path)
        assert isinstance(store, EvidenceStoreProtocol), "EvidenceStore fails EvidenceStoreProtocol"
        
        # Method verification
        assert hasattr(store, "store_evidence")
        assert hasattr(store, "retrieve_evidence")
        assert hasattr(store, "prune_expired")
        assert hasattr(store, "rotate_keys")
        assert hasattr(store, "close")
        
        store.close()
    finally:
        if os.path.exists(temp_db_path):
            os.remove(temp_db_path)


def test_telemetry_protocol():
    """Verify that PerformanceProfiler satisfies the TelemetryProtocol contract."""
    profiler = PerformanceProfiler.get_instance()
    assert isinstance(profiler, TelemetryProtocol), "PerformanceProfiler fails TelemetryProtocol"
    
    # Method verification
    assert hasattr(profiler, "context")
    assert hasattr(profiler, "record_event")
    assert hasattr(profiler, "set_gauge")
    assert hasattr(profiler, "record_histogram")


def test_scan_queue_protocol():
    """Verify that ScanQueueManager satisfies the QueueManagerProtocol contract."""
    manager = ScanQueueManager()
    assert isinstance(manager, QueueManagerProtocol), "ScanQueueManager fails QueueManagerProtocol"
    
    # Method verification
    assert hasattr(manager, "enqueue")
    assert hasattr(manager, "dequeue")
    assert hasattr(manager, "record_success")
    assert hasattr(manager, "record_throttle")
    assert hasattr(manager, "record_error")
    assert hasattr(manager, "size")
    assert hasattr(manager, "clear")
    assert hasattr(manager, "save_state")
    assert hasattr(manager, "load_state")
