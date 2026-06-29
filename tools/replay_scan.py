#!/usr/bin/env python
"""
AVAGuard Deterministic Replay Engine
Extracts archived encrypted evidence snapshots for a given scan, simulates the execution
environment statically with deterministic resource query overrides, asserts matching compliance outputs,
and computes a unique deterministic replay hash to ensure zero regression or side-effects.
"""

import os
import sys
import json
import hashlib
import sqlite3
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Configure path imports
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "avaguard-core"))
sys.path.insert(0, str(project_root / "avaguard-cli"))

from avaguard_core.benchmarks.loader import BenchmarkLoader
from avaguard_core.benchmarks.models import ControlDefinition
from desktop_app.models.evidence_store import EvidenceStore, LocalKeyProvider
from avaguard_core.providers.registry import ProviderRegistry
from avaguard_core.checks.declarative_check import DeclarativeCheck

import socket
class BlockedNetworkError(IOError):
    pass

class NetworkBlocker:
    """Blocks all outbound socket connections to ensure complete sandboxing during scan replays."""
    def __enter__(self):
        self.orig_socket = socket.socket
        def blocked_socket(*args, **kwargs):
            raise BlockedNetworkError("Outbound network access is strictly blocked during replay execution!")
        socket.socket = blocked_socket
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        socket.socket = self.orig_socket

def load_control(check_id: str) -> Optional[ControlDefinition]:
    """Helper to instantiate loader and read versioned JSON check definition."""
    benchmarks_dir = project_root / "avaguard-core" / "avaguard_core" / "benchmarks" / "azure"
    filepath = benchmarks_dir / f"{check_id}.json"
    if not filepath.exists():
        return None
    
    loader = BenchmarkLoader(title="Azure CIS", version="2.0.0", provider="azure")
    try:
        return loader.load_control_from_file(str(filepath))
    except Exception as e:
        print(f"[WARN] Failed to load control '{check_id}': {e}")
        return None


class MockReplayResponse:
    """Mock structure wrapping replayed resources satisfying query interface expectations."""
    def __init__(self, resources: List[Dict[str, Any]], evidence_snapshot: Optional[Dict] = None):
        self.resources = resources
        self.evidence_snapshot = evidence_snapshot


class MockReplayProvider:
    """Mock provider with query capability overridden to return static replayed resource arrays."""
    def __init__(self, resource_store: Dict[str, List[Dict[str, Any]]]):
        self.resource_store = resource_store

    def query_resources(self, resource_type: str, fields: List[str] = None) -> MockReplayResponse:
        resources = self.resource_store.get(resource_type, [])
        return MockReplayResponse(resources=resources)

    def is_healthy(self) -> bool:
        return True

    def get_capabilities(self) -> Dict:
        return {"replay": True}


def compute_replay_hash(results: List[Dict[str, Any]]) -> str:
    """Generates a mathematical, deterministic SHA-256 signature hash of replayed check outcomes."""
    # Ensure strict sorting of keys and objects to preserve hash uniqueness
    normalized = []
    for r in results:
        normalized.append({
            "check_id": r["check_id"],
            "status": str(r["status"]),
            "compliant_count": r["compliant_count"],
            "non_compliant_count": r["non_compliant_count"],
            "total_count": r["total_count"]
        })
    
    sorted_normalized = sorted(normalized, key=lambda x: x["check_id"])
    serialized = json.dumps(sorted_normalized, sort_keys=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def replay_scan(scan_id: str, db_path: str) -> bool:
    """Runs deterministic replay on the specified scan ID and verifies outcomes."""
    print("=" * 80)
    print(f"           [AVAGUARD DETERMINISTIC SCAN REPLAY ENGINE]")
    print(f"           Target Scan ID: {scan_id}")
    print("=" * 80)
    
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file not found at: {db_path}")
        return False

    # Initialize read-only connection to check original metadata
    # SECURITY: Replay must NEVER mutate source database — enforce immutable read-only WAL mode
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cursor = conn.cursor()

    # Enforce additional read-only pragma guards in case URI flag is silently ignored
    try:
        cursor.execute("PRAGMA query_only = ON;")
    except sqlite3.OperationalError:
        pass  # Older SQLite versions may not support this pragma

    cursor.execute("SELECT overall_score, total_checks, passed_checks, failed_checks FROM scan_history WHERE scan_id = ?", (scan_id,))
    orig_meta = cursor.fetchone()
    if not orig_meta:
        print(f"[ERROR] Original scan ID {scan_id} not found in database scan_history!")
        conn.close()
        return False
        
    orig_score, orig_total, orig_passed, orig_failed = orig_meta
    print("Original Scan Baseline:")
    print(f"  • Score:  {orig_score}%")
    print(f"  • Total:  {orig_total} checks")
    print(f"  • Passed: {orig_passed}")
    print(f"  • Failed: {orig_failed}")
    print("-" * 80)

    # 1. Fetch check results to get target check_ids
    cursor.execute("SELECT check_id, status, compliant_count, non_compliant_count FROM check_results WHERE scan_id = ?", (scan_id,))
    orig_checks = cursor.fetchall()
    orig_check_map = {row[0]: {"status": row[1], "compliant": row[2], "non_compliant": row[3]} for row in orig_checks}

    # 2. Fetch encrypted evidence snapshots
    cursor.execute("SELECT id, check_id, classification, compression_id FROM evidence_snapshots WHERE scan_id = ?", (scan_id,))
    snapshots = cursor.fetchall()
    
    if not snapshots:
        print("[WARN] Zero evidence snapshots found for this scan! (Deterministic replay is only possible for scans with evidence snapshots).")
        cursor.execute("SELECT count(*) FROM evidence_snapshots")
        total_snaps = cursor.fetchone()[0]
        print(f"Total evidence snapshots across all scans: {total_snaps}")
        conn.close()
        return False

    conn.close()

    # 3. Decrypt and decompress evidence snapshots
    print(f"Extracting and decrypting {len(snapshots)} evidence snapshots...")
    store = EvidenceStore(db_path=db_path)
    
    replayed_resources: Dict[str, List[Dict[str, Any]]] = {}
    check_resources_map: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    
    for snap_id, check_id, classification, comp_id in snapshots:
        try:
            # Secure retrieval using hardened cryptographic flow
            decrypted = store.retrieve_evidence(str(snap_id))
            
            # Map evidence resources
            resources = decrypted.get("resources", [])
            if not resources and isinstance(decrypted, list):
                resources = decrypted
            elif not resources and isinstance(decrypted, dict):
                # Try handling other structures or fallback
                resources = [decrypted]
                
            # Locate Control Definition to find resource type
            control_def = load_control(check_id)
            if control_def:
                res_type = control_def.scan_query.resource_type
                if check_id not in check_resources_map:
                    check_resources_map[check_id] = {}
                check_resources_map[check_id][res_type] = resources
                
        except Exception as e:
            print(f"[ERROR] Failed to decrypt evidence snapshot {snap_id} for check {check_id}: {e}")
            store.close()
            return False

    # 4. Perform replay sandbox execution
    # SECURITY: All compliance engine re-execution runs inside NetworkBlocker to guarantee
    # zero outbound network access. Any socket call raises BlockedNetworkError immediately.
    print("Re-running compliance engine assertions over replayed payloads...")
    print("  [SANDBOX] NetworkBlocker active — outbound network I/O is blocked.")
    replay_results: List[Dict[str, Any]] = []
    
    passed_count = 0
    failed_count = 0
    mismatches = 0
    
    with NetworkBlocker():
        for check_id, orig_vals in orig_check_map.items():
            # Load Control JSON
            control_def = load_control(check_id)
            if not control_def:
                print(f"[WARN] Skipping check {check_id}: benchmark JSON control definition unavailable.")
                continue
                
            # Get query resource mapping
            res_map = check_resources_map.get(check_id, {})
            
            # Override Registry with Replay mock provider
            replay_provider = MockReplayProvider(res_map)
            provider_name = control_def.provider_compatibility[0] if control_def.provider_compatibility else "azure"
            ProviderRegistry.register_active_instance(provider_name, replay_provider)
            
            # Run execution within sandbox
            try:
                check_instance = DeclarativeCheck(control_def)
                result = check_instance.execute()
                
                # Compare output logic
                replayed_status = result.status.value
                replayed_comp = result.compliant_count
                replayed_non_comp = result.non_compliant_count
                
                orig_status = orig_vals["status"]
                orig_comp = orig_vals["compliant"]
                orig_non_comp = orig_vals["non_compliant"]
                
                is_match = (
                    replayed_status == orig_status and
                    replayed_comp == orig_comp and
                    replayed_non_comp == orig_non_comp
                )
                
                status_text = "[OK]" if is_match else "[DRIFT]"
                print(f"  • {check_id:10} Compliance Score: {replayed_comp}/{replayed_comp+replayed_non_comp} {status_text}")
                
                if not is_match:
                    print(f"    [MISMATCH DETAIL] Original: {orig_status} (C:{orig_comp}, NC:{orig_non_comp}) | Replayed: {replayed_status} (C:{replayed_comp}, NC:{replayed_non_comp})")
                    mismatches += 1
                    
                if replayed_status == "PASS":
                    passed_count += 1
                else:
                    failed_count += 1
                    
                replay_results.append({
                    "check_id": check_id,
                    "status": replayed_status,
                    "compliant_count": replayed_comp,
                    "non_compliant_count": replayed_non_comp,
                    "total_count": replayed_comp + replayed_non_comp
                })
                
            except BlockedNetworkError as e:
                # Network access during replay is a CRITICAL security violation
                print(f"[CRITICAL] NetworkBlocker triggered during check {check_id} replay — network call attempted: {e}")
                store.close()
                return False
            except Exception as e:
                print(f"[ERROR] Replay execution crash on check {check_id}: {e}")
                store.close()
                return False

    store.close()

    # 5. Compute Replay Cryptographic Hash Signature
    replay_signature = compute_replay_hash(replay_results)
    
    print("-" * 80)
    print("Replay Execution Summary:")
    print(f"  • Total checks replayed: {len(replay_results)}")
    print(f"  • Passed: {passed_count} | Failed: {failed_count}")
    print(f"  • Replay Signature Hash: {replay_signature}")
    print("-" * 80)

    if mismatches > 0:
        print(f"[FAIL] Deterministic Replay FAILED: {mismatches} compliance outcome mismatches/drifts detected!")
        return False
        
    print("[SUCCESS] Deterministic Replay completed with 100% exact compliance matching!")
    print("=" * 80)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AVAGuard Compliance Deterministic Replay Utility")
    parser.add_argument("--scan-id", required=True, help="Scan ID to replay")
    parser.add_argument("--db", default="avaguard_enterprise.db", help="Path to database file")
    
    args = parser.parse_args()
    
    success = replay_scan(args.scan_id, args.db)
    sys.exit(0 if success else 1)
