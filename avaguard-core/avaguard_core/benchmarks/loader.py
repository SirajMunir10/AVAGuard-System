"""
AVAGuard Core — Benchmark Loader

Handles loading, schema validation, differential updates, and overrides
for declarative JSON benchmarks. Supports dynamic patches and versioned loading.
"""

import os
import json
import logging
from typing import Dict, Optional, List, Any
from avaguard_core.benchmarks.models import BenchmarkVersion, ControlDefinition
from avaguard_core.errors import BenchmarkValidationError

logger = logging.getLogger(__name__)


class BenchmarkLoader:
    """
    Orchestrates loading, parsing, and updating versioned declarative benchmarks.
    Supports organization overrides and differential updates out of the box.
    """

    def __init__(self, title: str, version: str, provider: str):
        self.benchmark = BenchmarkVersion(
            title=title,
            version=version,
            provider=provider
        )

    def load_control_from_json_string(self, json_content: str) -> ControlDefinition:
        """
        Validate and load a single control definition from a JSON string.

        Args:
            json_content: Raw JSON string representing a ControlDefinition.

        Returns:
            Validated ControlDefinition instance.

        Raises:
            BenchmarkValidationError: If content violates Pydantic schema constraints.
        """
        try:
            data = json.loads(json_content)
            control = ControlDefinition(**data)
            return control
        except Exception as e:
            logger.error(f"Schema validation failed for control: {e}")
            raise BenchmarkValidationError(f"Invalid control schema definition: {e}")

    def load_control_from_file(self, filepath: str) -> ControlDefinition:
        """
        Validate and load a single control definition from a file path.
        Includes SHA-256 manifest integrity verification.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Control file not found: {filepath}")

        # Compute SHA-256 hash of the file (normalized to LF to prevent cross-platform CRLF issues)
        import hashlib
        with open(filepath, 'rb') as f:
            file_bytes = f.read()
        computed_hash = hashlib.sha256(file_bytes.replace(b'\r\n', b'\n')).hexdigest()

        # Check for manifest.sha256 in the same directory
        dir_path = os.path.dirname(os.path.abspath(filepath))
        manifest_path = os.path.join(dir_path, "manifest.sha256")
        
        if os.path.exists(manifest_path):
            filename = os.path.basename(filepath)
            expected_hash = None
            
            with open(manifest_path, 'r', encoding='utf-8') as mf:
                for line in mf:
                    parts = line.strip().split()
                    if len(parts) >= 2 and parts[1] == filename:
                        expected_hash = parts[0]
                        break
            
            if not expected_hash:
                raise BenchmarkValidationError(
                    f"Integrity check failed: control '{filename}' is not listed in 'manifest.sha256'."
                )
            if computed_hash != expected_hash:
                raise BenchmarkValidationError(
                    f"Integrity check failed: control '{filename}' hash mismatch.\n"
                    f"  Expected: {expected_hash}\n"
                    f"  Actual:   {computed_hash}"
                )
            logger.info(f"Verified integrity for control '{filename}' successfully.")

        content = file_bytes.decode('utf-8')
        control = self.load_control_from_json_string(content)
        self.update_control(control)
        return control

    def load_directory(self, dir_path: str) -> int:
        """
        Recursively scan and load all JSON control definitions in a directory.

        Args:
            dir_path: Absolute directory path containing control JSONs.

        Returns:
            Number of successfully loaded controls.
        """
        if not os.path.isdir(dir_path):
            raise NotADirectoryError(f"Benchmark path is not a directory: {dir_path}")

        loaded_count = 0
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.lower().endswith('.json'):
                    filepath = os.path.join(root, file)
                    try:
                        self.load_control_from_file(filepath)
                        loaded_count += 1
                    except Exception as e:
                        logger.warning(f"Skipping malformed control file '{file}': {e}")
        
        logger.info(f"Loaded {loaded_count} controls into benchmark '{self.benchmark.title}' (v{self.benchmark.version})")
        return loaded_count

    def update_control(self, control: ControlDefinition) -> None:
        """
        Perform a differential update. Adds or patches a control in memory.
        Enables dynamically modifying specific controls without reloading everything.
        """
        self.benchmark.controls[control.control_id] = control
        logger.debug(f"Applied differential control patch: {control.control_id} (v{control.version})")

    def deprecate_control(self, control_id: str) -> None:
        """Flag a specific control as deprecated/superseded."""
        if control_id in self.benchmark.controls:
            self.benchmark.controls[control_id].deprecated = True
            logger.info(f"Flagged control as deprecated: {control_id}")
        else:
            logger.warning(f"Unable to deprecate control - ID not found: {control_id}")

    def apply_overrides(self, overrides_dict: Dict[str, Any]) -> None:
        """
        Apply organization-specific custom controls or severity overrides.

        Format:
        {
          "controls": {
            "1.1": {
              "reremediation_metadata": {
                "severity": "CRITICAL"
              }
            }
          }
        }
        """
        control_overrides = overrides_dict.get("controls", {})
        for cid, overrides in control_overrides.items():
            if cid in self.benchmark.controls:
                control = self.benchmark.controls[cid]
                # Merge logic (e.g., severity)
                metadata_overrides = overrides.get("reremediation_metadata", {}) or overrides.get("remediation_metadata", {})
                if "severity" in metadata_overrides:
                    control.remediation_metadata.severity = metadata_overrides["severity"]
                if "impact_statement" in metadata_overrides:
                    control.remediation_metadata.impact_statement = metadata_overrides["impact_statement"]
                
                logger.info(f"Applied organizational override patch to control: {cid}")

    def export_yaml(self, filepath: str) -> None:
        """
        Export current benchmark catalog to human-readable YAML for ease of auditing.
        Requires pyyaml library if invoked.
        """
        try:
            import yaml
            data = self.benchmark.dict()
            with open(filepath, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Successfully exported benchmark YAML catalog to: {filepath}")
        except ImportError:
            logger.error("Failed to export YAML: 'pyyaml' package is not installed.")
            raise ImportError("Exporting to YAML requires the 'pyyaml' package.")
