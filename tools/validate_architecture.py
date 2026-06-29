#!/usr/bin/env python
"""
AVAGuard Static Architecture Boundary Validator
Analyzes python file AST structures to enforce dependency rules, detect circular imports,
and generate architectural reports. Blocks CI by returning exit code 1 on violation.
"""

import os
import sys
import ast
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Layer identifiers
UI_LAYER = "UI_LAYER"
WORKERS_LAYER = "WORKERS_LAYER"
PERSISTENCE_LAYER = "PERSISTENCE_LAYER"
CORE_LAYER = "CORE_LAYER"
UNKNOWN_LAYER = "UNKNOWN_LAYER"


class ArchitectureValidator:
    """Statically scans imports and validates architectural layer rules and cycle traces."""
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        # Mapping: relative_module_path -> Set of imported absolute/relative module paths
        self.dependencies: Dict[str, Set[str]] = {}
        # Mapping: relative_module_path -> layer name
        self.file_layers: Dict[str, str] = {}
        # List of provider plugin allowlist (extendable)
        self.provider_allowlist = ["azure", "aws", "gcp", "mock"]
        
        # New violation trackers (Phase 4 refinements)
        self.dynamic_import_violations: List[Tuple[str, str]] = []
        self.symbol_violations: List[Tuple[str, str, str]] = []

    def identify_layer(self, file_path: Path) -> str:
        """Determines architectural layer of a file based on its path."""
        rel_str = str(file_path.relative_to(self.repo_root)).replace("\\", "/")
        
        if "desktop_app/views" in rel_str or "desktop_app/ui" in rel_str:
            return UI_LAYER
        elif "desktop_app/workers" in rel_str:
            return WORKERS_LAYER
        elif "desktop_app/models" in rel_str or "desktop_app/database" in rel_str:
            return PERSISTENCE_LAYER
        elif "avaguard-core" in rel_str or "avaguard_core" in rel_str:
            return CORE_LAYER
        return UNKNOWN_LAYER

    def parse_imports(self) -> Dict[str, Set[str]]:
        """Walks the repository and parses imports from all Python files."""
        python_files = []
        for root, dirs, files in os.walk(self.repo_root):
            # Skip build/venv/legacy directories
            dirs[:] = [d for d in dirs if d not in (".venv", ".git", "build", "dist", "__pycache__", "ll-fintuning-main", "web_portal", "CIS_AutmationV2", "mock_data", "datasets", "data", "output", "rag-train")]
            for file in files:
                if file.endswith(".py") and file != "validate_architecture.py" and not file.startswith("debug_"):
                    python_files.append(Path(root) / file)

        for file_path in python_files:
            rel_path = str(file_path.relative_to(self.repo_root)).replace("\\", "/")
            layer = self.identify_layer(file_path)
            self.file_layers[rel_path] = layer
            self.dependencies[rel_path] = set()

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=str(file_path))
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            self.dependencies[rel_path].add(alias.name)
                            if alias.name == "importlib" or alias.name.startswith("importlib."):
                                self.dynamic_import_violations.append((rel_path, "importlib usage"))
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            # Resolve relative imports cleanly
                            module_name = node.module
                            if node.level > 0:
                                # Simple relative level resolution
                                module_name = "." * node.level + module_name
                            self.dependencies[rel_path].add(module_name)
                            if node.module == "importlib" or node.module.startswith("importlib."):
                                self.dynamic_import_violations.append((rel_path, "importlib usage"))
                    elif isinstance(node, ast.Call):
                        # Dynamic imports detection
                        if isinstance(node.func, ast.Name) and node.func.id == "__import__":
                            self.dynamic_import_violations.append((rel_path, "__import__() call"))
                        elif isinstance(node.func, ast.Attribute) and node.func.attr == "import_module":
                            self.dynamic_import_violations.append((rel_path, "import_module() call"))
                            
                        # Forbidden UI symbols checks
                        if layer == UI_LAYER:
                            if isinstance(node.func, ast.Attribute) and node.func.attr == "connect":
                                if isinstance(node.func.value, ast.Name) and node.func.value.id == "sqlite3":
                                    self.symbol_violations.append((rel_path, "sqlite3.connect", "UI layer is forbidden from connecting directly to sqlite3."))
                            elif isinstance(node.func, ast.Attribute) and node.func.attr == "execute":
                                self.symbol_violations.append((rel_path, "cursor.execute", "UI layer is forbidden from executing direct cursor database queries."))
                            elif isinstance(node.func, ast.Name) and node.func.id == "Fernet":
                                self.symbol_violations.append((rel_path, "Fernet", "UI layer is forbidden from importing/instantiating cryptography.fernet primitives directly."))
                            elif isinstance(node.func, ast.Attribute) and node.func.attr == "compare_digest":
                                self.symbol_violations.append((rel_path, "compare_digest", "UI layer is forbidden from running cryptographic primitives directly."))
                            elif isinstance(node.func, ast.Name) and node.func.id == "open":
                                mode_arg = 'r'
                                if len(node.args) >= 2:
                                    if isinstance(node.args[1], ast.Constant) and isinstance(node.args[1].value, str):
                                        mode_arg = node.args[1].value
                                    elif isinstance(node.args[1], ast.Str):
                                        mode_arg = node.args[1].s
                                for keyword in node.keywords:
                                    if keyword.arg == "mode" and isinstance(keyword.value, (ast.Constant, ast.Str)):
                                        val = keyword.value.value if isinstance(keyword.value, ast.Constant) else keyword.value.s
                                        mode_arg = val
                                if any(c in mode_arg for c in ('w', 'a', 'x')):
                                    self.symbol_violations.append((rel_path, f"open(..., '{mode_arg}')", "UI layer is forbidden from executing direct filesystem writes."))
                            elif isinstance(node.func, ast.Attribute) and node.func.attr in ("write_text", "write_bytes"):
                                self.symbol_violations.append((rel_path, f"Path.{node.func.attr}", "UI layer is forbidden from executing direct filesystem writes."))
            except Exception as e:
                # Log parsing errors but do not crash the script
                print(f"[WARN] Failed parsing AST of {rel_path}: {e}")

        return self.dependencies

    def check_boundary_violations(self) -> List[Tuple[str, str, str, str]]:
        """
        Enforces:
        - UI Layer MUST NEVER directly import sqlite3 or access DB internals (models.database/evidence_store).
        - Core Layer MUST NEVER import desktop_app.
        - Persistence Layer MUST NEVER import PyQt6 or UI Layer.
        - Workers/Orchestration Layer MUST NEVER import UI Layer.
        Returns: list of (file, layer, imported_module, reason)
        """
        violations = []
        for file_path, imports in self.dependencies.items():
            layer = self.file_layers.get(file_path, UNKNOWN_LAYER)
            
            for imp in imports:
                # Rule 1: UI Layer boundary check
                if layer == UI_LAYER:
                    if imp == "sqlite3" or "database" in imp or "evidence_store" in imp:
                        violations.append((
                            file_path, layer, imp,
                            "Direct UI-to-storage/database coupling is strictly forbidden. Go through Orchestrator worker slots."
                        ))
                
                # Rule 2: Persistence Layer decoupling (no PyQt6 framework coupling)
                elif layer == PERSISTENCE_LAYER:
                    if "PyQt6" in imp or "desktop_app/views" in imp or "desktop_app/ui" in imp:
                        violations.append((
                            file_path, layer, imp,
                            "Persistence Layer must remain framework-agnostic. Direct PyQt6 or UI Layer imports are forbidden."
                        ))

                # Rule 3: Workers Layer boundary check (no UI Layer imports)
                elif layer == WORKERS_LAYER:
                    if "desktop_app/views" in imp or "desktop_app/ui" in imp:
                        violations.append((
                            file_path, layer, imp,
                            "Workers Layer must never import UI Layer modules to prevent cycle crossings."
                        ))

                # Rule 4: Core Engine Layer strict separation
                elif layer == CORE_LAYER:
                    if "desktop_app" in imp:
                        violations.append((
                            file_path, layer, imp,
                            "avaguard-core engine must remain fully decoupled and standalone from desktop app packaging wrappers."
                        ))

        return violations

    def module_matches_file(self, imp: str, parsed_file: str) -> bool:
        """Helper to match imported module string to a parsed repository file path."""
        clean_imp = imp.lstrip(".")
        if not clean_imp:
            return False
        imp_parts = clean_imp.replace(".", "/").split("/")
        file_no_ext = parsed_file.replace(".py", "").replace("\\", "/")
        imp_suffix = "/" + "/".join(imp_parts)
        return file_no_ext.endswith(imp_suffix) or file_no_ext == "/".join(imp_parts)

    def check_transitive_violations(self) -> List[Tuple[str, str, List[str]]]:
        """
        Verifies UI layer does not transitively reach persistence layer or forbidden external modules.
        Returns: list of (ui_file, target_forbidden_node, path_trace)
        """
        # 1. Build resolved dependency graph
        graph = {}
        for file_path, imports in self.dependencies.items():
            graph[file_path] = []
            for imp in imports:
                if imp in ("sqlite3", "cryptography", "cryptography.fernet"):
                    graph[file_path].append(imp)
                for parsed_file in self.dependencies.keys():
                    if self.module_matches_file(imp, parsed_file):
                        if parsed_file != file_path:
                            graph[file_path].append(parsed_file)
                        break

        transitive_violations = []

        # 2. Check UI to Persistence Layer reachability using DFS
        for file_path, layer in self.file_layers.items():
            if layer == UI_LAYER:
                visited = set()
                path = []

                def dfs(node):
                    visited.add(node)
                    path.append(node)

                    # Check violation
                    is_forbidden = False
                    if node in ("sqlite3", "cryptography", "cryptography.fernet"):
                        is_forbidden = True
                    elif node in self.file_layers and self.file_layers[node] == PERSISTENCE_LAYER:
                        is_forbidden = True

                    if is_forbidden and len(path) > 1:
                        transitive_violations.append((file_path, node, list(path)))

                    if node in graph:
                        for neighbor in graph[node]:
                            if neighbor not in visited:
                                dfs(neighbor)

                    path.pop()

                dfs(file_path)

        return transitive_violations

    def detect_circular_dependencies(self) -> List[List[str]]:
        """Detects circular dependencies (cycles) using DFS search on the import graph."""
        graph = {}
        
        # Convert imports to files in the repository where possible to find true cycles
        for file_path, imports in self.dependencies.items():
            graph[file_path] = []
            for imp in imports:
                # Find if any parsed file matches the imported module name
                for parsed_file in self.dependencies.keys():
                    if self.module_matches_file(imp, parsed_file):
                        if parsed_file != file_path:
                            graph[file_path].append(parsed_file)
                        break

        cycles = []
        visited = {}  # module -> status (0=unvisited, 1=visiting, 2=visited)
        path = []

        def dfs(node):
            visited[node] = 1
            path.append(node)
            for neighbor in graph.get(node, []):
                if visited.get(neighbor, 0) == 1:
                    # Cycle found!
                    cycle_start_idx = path.index(neighbor)
                    cycles.append(path[cycle_start_idx:] + [neighbor])
                elif visited.get(neighbor, 0) == 0:
                    dfs(neighbor)
            path.pop()
            visited[node] = 2

        for node in graph.keys():
            if visited.get(node, 0) == 0:
                dfs(node)

        return cycles

    def print_validation_report(self) -> bool:
        """Generates comprehensive architectural validation reports and returns success status."""
        self.parse_imports()
        violations = self.check_boundary_violations()
        transitive = self.check_transitive_violations()
        cycles = self.detect_circular_dependencies()

        print("=" * 80)
        print("           [AVAGUARD STATIC ARCHITECTURE BOUNDARY REPORT]")
        print("=" * 80)
        
        # Layer Summary
        layers = {UI_LAYER: 0, WORKERS_LAYER: 0, PERSISTENCE_LAYER: 0, CORE_LAYER: 0, UNKNOWN_LAYER: 0}
        for layer in self.file_layers.values():
            layers[layer] += 1
            
        print("Layer Metrics Summary:")
        print(f"  • UI Layer Files          : {layers[UI_LAYER]}")
        print(f"  • Workers/Scan Queue Files: {layers[WORKERS_LAYER]}")
        print(f"  • Persistence Models Files: {layers[PERSISTENCE_LAYER]}")
        print(f"  • Core Engine Files       : {layers[CORE_LAYER]}")
        print("-" * 80)

        # Boundary Violations Report
        if violations:
            print("[FAIL] Boundary Crossing Violations:")
            for file, layer, imp, reason in violations:
                print(f"  [VIOLATION] File: {file} ({layer})")
                print(f"     Imports: '{imp}'")
                print(f"     Reason: {reason}\n")
        else:
            print("[SUCCESS] All direct layer boundary constraints are strictly satisfied.")

        print("-" * 80)

        # Dynamic Import Violations Report
        if self.dynamic_import_violations:
            print("[FAIL] Dynamic Import Violations (importlib or __import__ usage banned):")
            for file, reason in self.dynamic_import_violations:
                print(f"  [VIOLATION] File: {file} -> {reason}")
        else:
            print("[SUCCESS] Zero dynamic import violations detected.")

        print("-" * 80)

        # Forbidden Symbols Report
        if self.symbol_violations:
            print("[FAIL] Forbidden Symbol-Level Access Violations:")
            for file, symbol, reason in self.symbol_violations:
                print(f"  [VIOLATION] File: {file} -> Forbidden Symbol '{symbol}' accessed.")
                print(f"     Reason: {reason}\n")
        else:
            print("[SUCCESS] Zero forbidden symbol-level access violations detected.")

        print("-" * 80)

        # Transitive Dependency Violations Report
        if transitive:
            print("[FAIL] Transitive Dependency Violations (UI indirectly reaching Persistence/SQL/Crypto):")
            for file, target, path in transitive:
                path_trace = " -> ".join(path)
                print(f"  [VIOLATION] UI File '{file}' reaches forbidden module '{target}' via:")
                print(f"     Path: {path_trace}\n")
        else:
            print("[SUCCESS] Zero transitive layer boundary violations detected.")

        print("-" * 80)

        # Circular Dependencies Report
        if cycles:
            print("[FAIL] Cyclic/Circular Dependencies Detected:")
            for cyc in cycles[:5]: # Show top 5 cycles
                trace = " -> ".join(cyc)
                print(f"  [CYCLE] Cycle: {trace}")
            if len(cycles) > 5:
                print(f"  ... and {len(cycles) - 5} more circular loops detected.")
        else:
            print("[SUCCESS] Zero circular dependency loops detected.")

        print("=" * 80)

        # Provider plugin allowlist check summary
        print(f"Plugin Allowlist Configured: {', '.join(self.provider_allowlist)}")
        
        # Write JSON reports
        import json
        
        arch_report = {
            "layer_files": layers,
            "counts": {
                "direct_violations": len(violations),
                "dynamic_import_violations": len(self.dynamic_import_violations),
                "symbol_violations": len(self.symbol_violations),
                "transitive_violations": len(transitive),
                "circular_dependencies": len(cycles)
            },
            "status": "PASS" if (len(violations) == 0 and len(cycles) == 0 and len(self.dynamic_import_violations) == 0 and len(self.symbol_violations) == 0 and len(transitive) == 0) else "FAIL"
        }
        with open(self.repo_root / "architecture_report.json", "w", encoding="utf-8") as f:
            json.dump(arch_report, f, indent=4)
            
        with open(self.repo_root / "cycle_report.json", "w", encoding="utf-8") as f:
            json.dump({"cycles": cycles}, f, indent=4)
            
        boundary_report = {
            "direct_violations": [
                {"file": f, "layer": l, "import": imp, "reason": r} for f, l, imp, r in violations
            ],
            "dynamic_import_violations": [
                {"file": f, "reason": r} for f, r in self.dynamic_import_violations
            ],
            "symbol_violations": [
                {"file": f, "symbol": s, "reason": r} for f, s, r in self.symbol_violations
            ],
            "transitive_violations": [
                {"file": f, "target": t, "path": p} for f, t, p in transitive
            ]
        }
        with open(self.repo_root / "boundary_violations.json", "w", encoding="utf-8") as f:
            json.dump(boundary_report, f, indent=4)

        # Returns True if no cycles and no violations found anywhere
        success = (
            len(violations) == 0 and
            len(cycles) == 0 and
            len(self.dynamic_import_violations) == 0 and
            len(self.symbol_violations) == 0 and
            len(transitive) == 0
        )
        return success


def main():
    repo_root = Path(__file__).resolve().parent.parent
    validator = ArchitectureValidator(repo_root)
    success = validator.print_validation_report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
