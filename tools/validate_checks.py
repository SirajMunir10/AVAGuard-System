#!/usr/bin/env python
"""
AVAGuard Declarative Check & Benchmark Manifest Validator
Validates check JSON schemas, selectors, logical consistency, severity normalization,
manifest hash alignments, and semantic versions. Blocks CI on any failure.
"""

import os
import sys
import json
import re
import hashlib
import hmac
from pathlib import Path
from typing import Dict, List, Set, Any, Tuple

# Supported operators from DeclarativeCheck engine
SUPPORTED_OPERATORS = {"equals", "not_equals", "contains", "in", "greater_than", "regex"}
VALID_SEVERITIES = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
SEMVER_REGEX = re.compile(r"^\d+\.\d+\.\d+$")


class DeclarativeCheckValidator:
    """Performs strict validation of JSON control specifications and manifest consistency."""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.benchmark_root = repo_root / "avaguard-core" / "avaguard_core" / "benchmarks"
        self.errors: List[str] = []
        self.control_ids: Set[str] = set()

    def add_error(self, message: str):
        self.errors.append(message)
        print(f"[FAIL] {message}")

    def validate_semantic_version(self, file_path: str, version: str):
        if not isinstance(version, str) or not SEMVER_REGEX.match(version):
            self.add_error(f"File {file_path}: 'version' '{version}' does not match semantic versioning format X.Y.Z")

    def validate_schema(self, file_path: str, data: Dict[str, Any]):
        required_fields = ["control_id", "title", "version", "scan_query", "evaluation_rules", "remediation_metadata"]
        for field in required_fields:
            if field not in data:
                self.add_error(f"File {file_path}: Missing mandatory schema field '{field}'")
                return

        # Check subfields
        if not isinstance(data["scan_query"], dict) or "resource_type" not in data["scan_query"]:
            self.add_error(f"File {file_path}: 'scan_query' must be a dictionary containing 'resource_type'")
        
        if not isinstance(data["evaluation_rules"], list):
            self.add_error(f"File {file_path}: 'evaluation_rules' must be a list of assertion rules")
        
        if not isinstance(data["remediation_metadata"], dict) or "severity" not in data["remediation_metadata"]:
            self.add_error(f"File {file_path}: 'remediation_metadata' must contain 'severity'")

    def validate_rules(self, file_path: str, data: Dict[str, Any]):
        if "evaluation_rules" not in data or not isinstance(data["evaluation_rules"], list):
            return
            
        rules = data["evaluation_rules"]
        fields_equals: Dict[str, Any] = {}
        fields_not_equals: Dict[str, Set[Any]] = {}
        
        for idx, rule in enumerate(rules):
            rule_loc = f"rule[{idx}] in file {file_path}"
            
            # Validate fields presence
            if not all(k in rule for k in ("field", "operator", "expected")):
                self.add_error(f"{rule_loc}: Must contain 'field', 'operator', and 'expected'")
                continue
                
            field = rule["field"]
            operator = str(rule["operator"]).strip().lower()
            expected = rule["expected"]
            
            # 1. Unsupported operator check
            if operator not in SUPPORTED_OPERATORS:
                self.add_error(f"{rule_loc}: Unsupported operator '{operator}'. Valid operators are: {list(SUPPORTED_OPERATORS)}")
            
            # 2. Impossible/contradictory condition checking
            if operator == "equals":
                if field in fields_equals and fields_equals[field] != expected:
                    self.add_error(
                        f"File {file_path}: Impossible logical condition on field '{field}' "
                        f"(claims it equals '{fields_equals[field]}' AND '{expected}' simultaneously)"
                    )
                fields_equals[field] = expected
                
                # Check conflict with not_equals
                if field in fields_not_equals and expected in fields_not_equals[field]:
                    self.add_error(
                        f"File {file_path}: Impossible logical condition on field '{field}' "
                        f"(claims it equals '{expected}' AND not_equals '{expected}')"
                    )
                    
            elif operator == "not_equals":
                if field not in fields_not_equals:
                    fields_not_equals[field] = set()
                fields_not_equals[field].add(expected)
                
                # Check conflict with equals
                if field in fields_equals and fields_equals[field] == expected:
                    self.add_error(
                        f"File {file_path}: Impossible logical condition on field '{field}' "
                        f"(claims it equals '{expected}' AND not_equals '{expected}')"
                    )

    def validate_severity(self, file_path: str, data: Dict[str, Any]):
        if "remediation_metadata" not in data:
            return
        sev = data["remediation_metadata"].get("severity")
        if not isinstance(sev, str) or sev.upper() not in VALID_SEVERITIES:
            self.add_error(f"File {file_path}: Severity '{sev}' must be normalized to one of: {list(VALID_SEVERITIES)}")

    def validate_control_id_uniqueness(self, file_path: str, control_id: str):
        if control_id in self.control_ids:
            self.add_error(f"File {file_path}: Duplicate control ID '{control_id}' found!")
        else:
            self.control_ids.add(control_id)

    def validate_manifests(self):
        """Checks manifest.sha256 consistency timing-safely in all benchmark provider subfolders."""
        # Find directories inside benchmarks root
        if not self.benchmark_root.exists():
            self.add_error(f"Benchmarks root directory '{self.benchmark_root}' does not exist!")
            return
            
        provider_dirs = [d for d in self.benchmark_root.iterdir() if d.is_dir() and d.name != "__pycache__"]
        
        for pdir in provider_dirs:
            manifest_file = pdir / "manifest.sha256"
            if not manifest_file.exists():
                self.add_error(f"Benchmark provider directory '{pdir.name}' is missing mandatory 'manifest.sha256'")
                continue
                
            # Parse manifest file
            manifest_entries: Dict[str, str] = {}
            try:
                with open(manifest_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        parts = line.split(maxsplit=1)
                        if len(parts) == 2:
                            sha_hash, filename = parts
                            manifest_entries[filename] = sha_hash
            except Exception as e:
                self.add_error(f"Failed to read manifest file '{manifest_file}': {e}")
                continue

            # Verify actual files listed in pdir
            json_files = [f for f in pdir.iterdir() if f.is_file() and f.suffix == ".json"]
            
            # Check for files on disk but missing from manifest, or mismatched hash
            for jfile in json_files:
                fname = jfile.name
                
                # Check hash
                try:
                    with open(jfile, "rb") as f:
                        file_bytes = f.read()
                    computed_hash = hashlib.sha256(file_bytes).hexdigest()
                except Exception as e:
                    self.add_error(f"Failed to compute SHA256 of file '{fname}': {e}")
                    continue
                
                if fname not in manifest_entries:
                    self.add_error(f"Provider '{pdir.name}': File '{fname}' is present on disk but not declared in manifest.sha256")
                else:
                    declared_hash = manifest_entries[fname]
                    # Secure timing-safe compare digest verification
                    if not hmac.compare_digest(computed_hash, declared_hash):
                        self.add_error(
                            f"Provider '{pdir.name}': Cryptographic mismatch for file '{fname}' in manifest.sha256!\n"
                            f"  Declared: '{declared_hash}'\n"
                            f"  Computed: '{computed_hash}'"
                        )
            
            # Check for files declared in manifest but missing on disk
            for fname in manifest_entries.keys():
                jpath = pdir / fname
                if not jpath.exists():
                    self.add_error(f"Provider '{pdir.name}': Manifest declares file '{fname}' which is missing on disk!")

    def validate_all_checks(self) -> bool:
        """Walks the benchmarks directory, runs check validations, and checks manifests."""
        print("=" * 80)
        print("           [AVAGUARD DECLARATIVE CHECKS & MANIFEST VALIDATION]")
        print("=" * 80)
        
        if not self.benchmark_root.exists():
            self.add_error("Benchmarks root directory not found.")
            return False

        json_files = []
        for root, _, files in os.walk(self.benchmark_root):
            for file in files:
                if file.endswith(".json"):
                    json_files.append(Path(root) / file)

        print(f"Discovered {len(json_files)} declarative control check JSON files.")
        
        for file_path in json_files:
            rel_str = str(file_path.relative_to(self.repo_root)).replace("\\", "/")
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                self.add_error(f"File {rel_str}: Failed parsing JSON data: {e}")
                continue

            self.validate_schema(rel_str, data)
            self.validate_rules(rel_str, data)
            self.validate_severity(rel_str, data)
            
            if "version" in data:
                self.validate_semantic_version(rel_str, data["version"])
            if "control_id" in data:
                self.validate_control_id_uniqueness(rel_str, data["control_id"])

        # Check cryptographic manifests
        self.validate_manifests()
        
        print("-" * 80)
        if self.errors:
            print(f"[FAIL] Check validation FAILED with {len(self.errors)} errors.")
            print("=" * 80)
            return False
        else:
            print("[SUCCESS] All declarative controls and manifests are 100% valid and verified.")
            print("=" * 80)
            return True


def main():
    repo_root = Path(__file__).resolve().parent.parent
    validator = DeclarativeCheckValidator(repo_root)
    success = validator.validate_all_checks()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
