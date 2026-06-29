#!/usr/bin/env python3
"""
AVAGuard Coverage Matrix

Prints an ASCII table of corpus coverage: domain × incident_type.
Cells below the gap threshold are marked "← GAP".
Rows sorted by total entry count descending — highest coverage first.
Outputs to stdout only — no files written.

Usage:
    python coverage_matrix.py --input data/corpus_grounded.jsonl
    python coverage_matrix.py --input data/
    python coverage_matrix.py --input data/ --gap-threshold 10
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

# Ordered domain list — matches gap_report.json schema and spec
DOMAINS: List[str] = [
    "Intune",
    "Entra ID",
    "Defender for Endpoint",
    "Defender XDR",
    "Sentinel",
    "Exchange Online",
    "Azure",
    "Purview",
    "Governance",
]

# Ordered incident type list — matches gap_report.json schema and spec
INCIDENT_TYPES: List[str] = [
    "Troubleshooting",
    "Implementation",
    "Hardening",
    "Incident Response",
    "Governance",
    "Optimization",
]

# Cells below this count are flagged as gaps.
# 5 chosen as minimum: below this the model has insufficient examples to
# generalise the pattern for that product area × scenario type combination.
GAP_THRESHOLD: int = 5

# Column header abbreviations to keep ASCII table width manageable
INCIDENT_TYPE_ABBREV: Dict[str, str] = {
    "Troubleshooting": "Troublesh.",
    "Implementation":  "Implement.",
    "Hardening":       "Hardening",
    "Incident Response": "IR",
    "Governance":      "Governanc.",
    "Optimization":    "Optimiz.",
}


def load_corpus(paths: List[Path]) -> List[Dict]:
    """
    Load corpus entries from one or more JSONL files.
    Skips malformed lines silently.
    """
    entries: List[Dict] = []
    for path in paths:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return entries


def build_matrix(entries: List[Dict]) -> Tuple[Dict[str, Dict[str, int]], int]:
    """
    Build a domain × incident_type count matrix from corpus entries.

    Entries whose domain or incident_type does not match the canonical lists
    are counted in 'unknown' for transparency but not added to the matrix.

    Returns:
        (matrix, unknown_count)
    """
    matrix = {domain: {it: 0 for it in INCIDENT_TYPES} for domain in DOMAINS}
    unknown = 0

    for entry in entries:
        domain = entry.get("domain", "").strip()
        incident_type = entry.get("incident_type", "").strip()
        if domain in matrix and incident_type in matrix[domain]:
            matrix[domain][incident_type] += 1
        else:
            unknown += 1

    return matrix, unknown


def print_matrix(
    matrix: Dict[str, Dict[str, int]],
    gap_threshold: int,
    total: int,
    unknown: int,
) -> None:
    """
    Print an ASCII coverage matrix to stdout.

    Rows sorted by total entry count descending.
    Cells below gap_threshold marked with "← GAP".
    Followed by a prioritised gap list (max 15, sorted by count ascending).
    """
    # Compute row totals for sort order
    row_totals = {domain: sum(matrix[domain].values()) for domain in DOMAINS}
    sorted_domains = sorted(DOMAINS, key=lambda d: row_totals[d], reverse=True)

    # Build column headers (abbreviated to fit)
    headers = [INCIDENT_TYPE_ABBREV.get(it, it[:10]) for it in INCIDENT_TYPES]
    domain_col_w = max(len(d) for d in DOMAINS) + 2  # left column width
    cell_w = 13                                        # per data column width
    total_col_w = 7

    sep_len = domain_col_w + (cell_w + 3) * len(INCIDENT_TYPES) + total_col_w + 5

    print()
    print("=" * sep_len)
    print("AVAGuard Corpus Coverage Matrix")
    print(f"Total entries: {total}  |  Unknown domain/type: {unknown}  |  Gap threshold: < {gap_threshold}")
    print("=" * sep_len)

    # Header row
    header = f"{'Domain':<{domain_col_w}}"
    for h in headers:
        header += f" | {h:^{cell_w}}"
    header += f" | {'Total':^{total_col_w}}"
    print(header)
    print("-" * sep_len)

    gap_count = 0
    for domain in sorted_domains:
        row = f"{domain:<{domain_col_w}}"
        for it in INCIDENT_TYPES:
            count = matrix[domain][it]
            if count < gap_threshold:
                cell_str = f"{count} ← GAP"
                gap_count += 1
            else:
                cell_str = str(count)
            row += f" | {cell_str:^{cell_w}}"
        row += f" | {row_totals[domain]:^{total_col_w}}"
        print(row)

    print("-" * sep_len)
    total_cells = len(DOMAINS) * len(INCIDENT_TYPES)
    print(f"\nGap cells (< {gap_threshold} entries): {gap_count} / {total_cells}")

    # Prioritised gap list — most critical (lowest count) first
    gap_cells = [
        (matrix[d][it], d, it)
        for d in DOMAINS
        for it in INCIDENT_TYPES
        if matrix[d][it] < gap_threshold
    ]
    gap_cells.sort()

    if gap_cells:
        print(f"\nPriority gaps (most critical first, max 15 shown):")
        print(f"  {'Domain':<28} | {'Incident Type':<22} | Count | Needed")
        print(f"  {'-'*28}-+-{'-'*22}-+-------+-------")
        for count, domain, it in gap_cells[:15]:
            needed = gap_threshold - count
            print(f"  {domain:<28} | {it:<22} | {count:^5} | {needed:^6}")

    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print corpus coverage matrix by domain × incident_type (stdout only)"
    )
    parser.add_argument(
        "--input", type=Path, default=Path("data/corpus_grounded.jsonl"),
        help="Grounded corpus JSONL file or directory of JSONL files (default: data/corpus_grounded.jsonl)",
    )
    parser.add_argument(
        "--gap-threshold", type=int, default=GAP_THRESHOLD,
        help=f"Entries below this count are marked as gaps (default: {GAP_THRESHOLD})",
    )
    args = parser.parse_args()

    # Accept a single file or a directory
    if args.input.is_dir():
        paths = [
            f for f in sorted(args.input.glob("*.jsonl"))
            if "archived" not in str(f).replace("\\", "/")
            and f.name not in ("corpus_pending_review.jsonl", "corpus_rejected.jsonl")
        ]
    else:
        paths = [args.input]

    if not paths:
        print(f"No JSONL files found at: {args.input}")
        sys.exit(1)

    entries = load_corpus(paths)
    if not entries:
        print("No entries found. Run extract_scenarios.py first to populate the grounded corpus.")
        sys.exit(0)

    matrix, unknown = build_matrix(entries)
    print_matrix(matrix, args.gap_threshold, len(entries), unknown)


if __name__ == "__main__":
    main()
