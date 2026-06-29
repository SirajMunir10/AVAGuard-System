#!/usr/bin/env python
"""
AVAGuard - SQLite Operational Safety Diagnostics
Performs database diagnostics including WAL growth, fragmentation, indexes, pragmas, and integrity check.
"""

import os
import sys
import sqlite3
import argparse
from typing import Dict, Any, List
from pathlib import Path

class DatabaseDiagnostics:
    """SQLite diagnostic report engine."""
    def __init__(self, db_path: str):
        self.db_path = Path(db_path).expanduser().resolve()
        
    def generate_report(self) -> Dict[str, Any]:
        """
        Gathers:
        - WAL file size and growth delta
        - Freelist page count and fragmentation estimates
        - Database index utilization
        - active PRAGMA states (journal_mode, synchronous, cache_size, mmap_size)
        - SQLite structural integrity check (PRAGMA integrity_check)
        - VACUUM and rebuild recommendations
        """
        report = {
            "database_path": str(self.db_path),
            "exists": self.db_path.exists(),
            "file_size_bytes": 0,
            "wal_file_size_bytes": 0,
            "shm_file_size_bytes": 0,
            "integrity_check": "FAILED",
            "freelist_count": 0,
            "page_count": 0,
            "page_size": 0,
            "fragmentation_pct": 0.0,
            "pragmas": {},
            "indexes": [],
            "vacuum_recommended": False,
            "warnings": []
        }

        if not self.db_path.exists():
            report["warnings"].append(f"Database file does not exist at: {self.db_path}")
            return report

        report["file_size_bytes"] = self.db_path.stat().st_size
        
        # Check WAL and SHM sizes
        wal_path = self.db_path.with_name(self.db_path.name + "-wal")
        if wal_path.exists():
            report["wal_file_size_bytes"] = wal_path.stat().st_size
            
        shm_path = self.db_path.with_name(self.db_path.name + "-shm")
        if shm_path.exists():
            report["shm_file_size_bytes"] = shm_path.stat().st_size

        try:
            conn = sqlite3.connect(str(self.db_path))
            cursor = conn.cursor()

            # 1. Structural Integrity Check
            cursor.execute("PRAGMA integrity_check")
            integrity_res = cursor.fetchone()
            report["integrity_check"] = integrity_res[0] if integrity_res else "unknown"

            # 2. General File Pragmas
            cursor.execute("PRAGMA page_count")
            report["page_count"] = cursor.fetchone()[0]

            cursor.execute("PRAGMA page_size")
            report["page_size"] = cursor.fetchone()[0]

            cursor.execute("PRAGMA freelist_count")
            report["freelist_count"] = cursor.fetchone()[0]

            # Estimate fragmentation based on freelist pages
            if report["page_count"] > 0:
                report["fragmentation_pct"] = (report["freelist_count"] / report["page_count"]) * 100.0
            
            if report["fragmentation_pct"] > 15.0 or report["freelist_count"] > 1000:
                report["vacuum_recommended"] = True

            # 3. Active PRAGMA state verification
            pragmas_to_check = [
                "journal_mode", "synchronous", "cache_size", "mmap_size", 
                "temp_store", "journal_size_limit", "auto_vacuum"
            ]
            for pragma in pragmas_to_check:
                try:
                    cursor.execute(f"PRAGMA {pragma}")
                    res = cursor.fetchone()
                    report["pragmas"][pragma] = res[0] if res else "unknown"
                except Exception as pe:
                    report["pragmas"][pragma] = f"error: {pe}"

            # 4. Check for WAL runaway growth and checkpoint starvation
            if report["wal_file_size_bytes"] > 1024 * 1024 * 50: # > 50MB WAL
                report["warnings"].append(f"WAL file is large ({report['wal_file_size_bytes'] / (1024 * 1024):.2f} MB), checkpoint starvation likely.")
                
            # Verify WAL journal mode is properly set
            if report["pragmas"].get("journal_mode") != "wal":
                report["warnings"].append("Database is not operating in WAL mode. Concurrency is limited.")

            # 5. Index utilization
            cursor.execute("SELECT name, tbl_name FROM sqlite_master WHERE type='index'")
            indexes_list = cursor.fetchall()
            for idx_name, tbl_name in indexes_list:
                # Get columns in index
                try:
                    cursor.execute(f"PRAGMA index_info({idx_name})")
                    columns = [row[2] for row in cursor.fetchall()]
                    report["indexes"].append({
                        "name": idx_name,
                        "table": tbl_name,
                        "columns": columns
                    })
                except Exception:
                    pass

            conn.close()
        except Exception as e:
            report["warnings"].append(f"Error querying database: {e}")
            report["integrity_check"] = f"CRITICAL ERROR: {e}"

        return report

    def display_report(self):
        """Prints a beautifully formatted operational report to stdout."""
        report = self.generate_report()
        
        print("=" * 60)
        print("           [AVAGUARD SQLITE DIAGNOSTICS REPORT]")
        print("=" * 60)
        print(f"Database Path : {report['database_path']}")
        print(f"File Size     : {report['file_size_bytes'] / (1024 * 1024):.3f} MB")
        print(f"WAL Size      : {report['wal_file_size_bytes'] / (1024 * 1024):.3f} MB")
        print(f"SHM Size      : {report['shm_file_size_bytes'] / 1024:.2f} KB")
        print("-" * 60)
        print(f"Integrity Check: {report['integrity_check'].upper()}")
        print(f"Total Pages    : {report['page_count']}")
        print(f"Page Size      : {report['page_size']} bytes")
        print(f"Freelist Pages : {report['freelist_count']} ({report['fragmentation_pct']:.2f}% fragmentation)")
        print(f"VACUUM Advised : {'YES' if report['vacuum_recommended'] else 'NO'}")
        print("-" * 60)
        print("ACTIVE PRAGMA TUNINGS:")
        for pragma, val in report["pragmas"].items():
            print(f"  * {pragma:<20}: {val}")
        print("-" * 60)
        print(f"INDEXES DETECTED ({len(report['indexes'])}):")
        for idx in report["indexes"]:
            cols = ", ".join(idx["columns"])
            print(f"  * {idx['name']} ON {idx['table']} ({cols})")
        
        if report["warnings"]:
            print("-" * 60)
            print("SYSTEM WARNINGS & RECOVERY ACTIONS:")
            for warn in report["warnings"]:
                # Print cleanly without crashing
                try:
                    print(f"  [WARN] {warn}")
                except UnicodeEncodeError:
                    print(f"  [WARN] {warn.encode('ascii', 'ignore').decode('ascii')}")
        
        print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="AVAGuard SQLite Diagnostics Engine")
    parser.add_argument("--db", type=str, help="Absolute path to the SQLite database")
    args = parser.parse_args()

    db_path = args.db
    if not db_path:
        # Resolve standard location
        repo_root = Path(__file__).resolve().parent.parent
        db_path = str(repo_root / "avaguard_enterprise.db")

    diag = DatabaseDiagnostics(db_path)
    diag.display_report()

if __name__ == "__main__":
    main()
