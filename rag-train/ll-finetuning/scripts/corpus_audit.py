#!/usr/bin/env python3
"""
AVAGuard Corpus Quality Auditor

Scans existing JSONL corpus files for field completeness, off-topic detection,
and domain × incident_type coverage gaps. Writes gap_report.json to guide
extraction priorities.

Usage:
    python corpus_audit.py --input data/ --output data/gap_report.json
    python corpus_audit.py --input data/ --threshold 5
    python corpus_audit.py --input data/ --include-archived
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any

# ── Off-topic detection keywords ───────────────────────────────────────────────
# These indicate HackTheBox / CTF penetration testing content which is
# categorically unrelated to Microsoft cloud operational training data.
OFF_TOPIC_KEYWORDS: List[str] = [
    "nmap", "reverse shell", "htb", "hackthebox", "evil-winrm", "meterpreter",
    "netcat", "exploit", "payload", "ctf", "flag{", "privilege escalation",
    "shells", "bind shell", "mimikatz", "pass-the-hash", "kerberoasting",
    "sqlmap", "gobuster", "ffuf", "nikto", "burpsuite", "burp suite",
    "hydra", "hashcat", "john the ripper", "metasploit", "nc -lvnp",
    ".htb", "hackthebox.com", "10.10.11.", "10.10.10.",
]

# Supported Microsoft cloud operational domains
DOMAINS: List[str] = [
    "Intune", "Entra ID", "Defender for Endpoint", "Defender XDR",
    "Sentinel", "Exchange Online", "Azure", "Purview", "Governance",
]

# Supported incident types
INCIDENT_TYPES: List[str] = [
    "Troubleshooting", "Implementation", "Hardening",
    "Incident Response", "Governance", "Optimization",
]

# Completeness classification thresholds
# ≥7: Complete — suitable for training corpus as-is
# 4–6: Shallow — usable but needs enrichment or extraction pass
# <4: Skeleton — insufficient operational depth for training
COMPLETE_THRESHOLD: int = 7
SHALLOW_THRESHOLD: int = 4

# Minimum entries per domain × incident_type cell before flagging as a gap.
# 5 chosen: below this, the model has insufficient examples to generalize the
# pattern for that product area and scenario type.
GAP_THRESHOLD: int = 5


def score_entry(entry: Dict) -> int:
    """
    Score a corpus entry 0–10 based on field completeness.

    Scoring weights (explicit):
        source_references (non-empty list): +2   — grounding is the highest-priority
                                                    property; ungrounded entries are
                                                    operationally untrustworthy
        error_codes (non-empty list):       +2   — specific codes distinguish real
                                                    scenarios from invented ones
        remediation_steps (≥2 steps):      +2   — requires ≥2 because a single step
                                                    is almost always a placeholder;
                                                    real runbooks have sequences
        symptoms (non-empty list):          +1   — enables scenario matching at inference
        environment_context (non-empty):   +1   — allows scoping to tenant configs
        validation (non-empty string):      +1   — "how do you confirm it worked"
        rollback (non-empty string):        +1   — production runbooks require this

    Returns:
        int: Score 0–10
    """
    score = 0

    # source_references: 2 pts — non-negotiable for trusted training data
    refs = entry.get("source_references")
    if refs and isinstance(refs, list) and any(str(r).strip() for r in refs):
        score += 2

    # error_codes: 2 pts — operational specificity signal
    codes = entry.get("error_codes")
    if codes and isinstance(codes, list) and len(codes) > 0:
        score += 2

    # remediation_steps: 2 pts — requires ≥2 for actionable guidance
    steps = entry.get("remediation_steps")
    if steps and isinstance(steps, list) and len(steps) >= 2:
        score += 2

    # symptoms: 1 pt — needed to match incident type to scenario at inference
    symptoms = entry.get("symptoms")
    if symptoms and isinstance(symptoms, list) and len(symptoms) > 0:
        score += 1

    # environment_context: 1 pt — scoping to specific tenant/device configs
    ctx = entry.get("environment_context")
    if ctx and isinstance(ctx, dict) and any(v for v in ctx.values() if v):
        score += 1

    # validation: 1 pt — "how do you know it worked" is critical for runbooks
    validation = entry.get("validation", "")
    if isinstance(validation, str) and validation.strip():
        score += 1

    # rollback: 1 pt — production runbooks must include rollback procedures
    rollback = entry.get("rollback", "")
    if isinstance(rollback, str) and rollback.strip():
        score += 1

    return score


def detect_off_topic(entry: Dict, keywords: List[str]) -> bool:
    """
    Detect if an entry contains off-topic content (HackTheBox / CTF material).

    Flattens all string values in the entry recursively into a single lowercase
    string, then checks for presence of any off-topic keyword. Case-insensitive.
    Never raises on unexpected field types.

    Args:
        entry: JSONL corpus entry dict
        keywords: List of off-topic indicator strings

    Returns:
        bool: True if any keyword found in the entry's text content
    """
    text_parts: List[str] = []

    def _extract(obj: Any) -> None:
        if isinstance(obj, str):
            text_parts.append(obj)
        elif isinstance(obj, list):
            for item in obj:
                _extract(item)
        elif isinstance(obj, dict):
            for v in obj.values():
                _extract(v)

    _extract(entry)
    combined = " ".join(text_parts).lower()
    return any(kw.lower() in combined for kw in keywords)


def build_gap_matrix(entries: List[Tuple]) -> Dict:
    """
    Build a coverage matrix: domain × incident_type → entry count.

    Only non-off-topic entries are counted; off-topic entries are tallied
    separately and excluded from the matrix so gaps reflect usable coverage.

    Args:
        entries: List of (entry_dict, score, is_off_topic) tuples

    Returns:
        Dict matching the gap_report.json schema:
        {
          "total_entries", "complete", "shallow", "skeleton", "off_topic",
          "gap_matrix": { domain: { incident_type: count } },
          "gaps": [{ "domain", "incident_type", "count" }]  # asc by count
        }
    """
    gap_matrix: Dict[str, Dict[str, int]] = {
        domain: {it: 0 for it in INCIDENT_TYPES}
        for domain in DOMAINS
    }

    total = len(entries)
    complete = shallow = skeleton = off_topic_count = 0

    for entry, score, is_off_topic in entries:
        if is_off_topic:
            off_topic_count += 1
            continue  # off-topic entries never count toward coverage

        if score >= COMPLETE_THRESHOLD:
            complete += 1
        elif score >= SHALLOW_THRESHOLD:
            shallow += 1
        else:
            skeleton += 1

        domain = entry.get("domain", "").strip()
        incident_type = entry.get("incident_type", "").strip()

        if domain in gap_matrix and incident_type in gap_matrix[domain]:
            gap_matrix[domain][incident_type] += 1

    # Compute gap cells (below GAP_THRESHOLD) sorted by count ascending
    # so the most critical gaps appear first in the list
    gaps = [
        {"domain": domain, "incident_type": it, "count": gap_matrix[domain][it]}
        for domain in DOMAINS
        for it in INCIDENT_TYPES
        if gap_matrix[domain][it] < GAP_THRESHOLD
    ]
    gaps.sort(key=lambda x: x["count"])

    return {
        "total_entries": total,
        "complete": complete,
        "shallow": shallow,
        "skeleton": skeleton,
        "off_topic": off_topic_count,
        "gap_matrix": gap_matrix,
        "gaps": gaps,
    }


def audit_jsonl_file(filepath: Path) -> List[Tuple]:
    """
    Parse a JSONL file and score each entry.

    Handles two formats:
      - JSONL: one JSON object per line (standard)
      - JSON array: entire file is a single [...] array

    Strips trailing commas from malformed JSONL lines before parse.
    Skips lines that are not dict objects with a logged warning.

    Args:
        filepath: Path to .jsonl file

    Returns:
        List of (entry_dict, score, is_off_topic) tuples
    """
    raw = filepath.read_text(encoding="utf-8", errors="ignore")
    lines = [l.strip() for l in raw.splitlines() if l.strip() and l.strip() not in ("[", "]")]

    parsed_entries: List[Dict] = []
    for i, line in enumerate(lines, 1):
        line = line.rstrip(",")
        if not line:
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict):
                parsed_entries.append(obj)
            elif isinstance(obj, list):
                parsed_entries.extend(e for e in obj if isinstance(e, dict))
        except json.JSONDecodeError:
            print(f"  [WARN] {filepath.name} line {i}: malformed JSON — skipping")

    results = []
    for entry in parsed_entries:
        s = score_entry(entry)
        ot = detect_off_topic(entry, OFF_TOPIC_KEYWORDS)
        results.append((entry, s, ot))

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit JSONL corpus files for completeness, off-topic content, and coverage gaps"
    )
    parser.add_argument(
        "--input", type=Path, default=Path("data"),
        help="Directory containing JSONL corpus files (default: data/)"
    )
    parser.add_argument(
        "--output", type=Path, default=Path("data/gap_report.json"),
        help="Output path for gap_report.json (default: data/gap_report.json)"
    )
    parser.add_argument(
        "--include-archived", action="store_true",
        help="Include files in data/archived/ (default: skip archived)"
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input directory not found: {args.input}")
        sys.exit(1)

    # Collect JSONL files, excluding archived and pipeline output files by default
    jsonl_files = []
    for f in sorted(args.input.rglob("*.jsonl")):
        if not args.include_archived and "archived" in str(f).replace("\\", "/"):
            continue
        # Pipeline output files auditing themselves would be circular
        if f.name in ("corpus_pending_review.jsonl", "corpus_rejected.jsonl"):
            continue
        jsonl_files.append(f)

    if not jsonl_files:
        print(f"No .jsonl files found under {args.input}")
        sys.exit(1)

    print(f"Auditing {len(jsonl_files)} JSONL file(s):\n")

    all_entries: List[Tuple] = []
    for f in jsonl_files:
        entries = audit_jsonl_file(f)
        off_ct = sum(1 for _, _, ot in entries if ot)
        print(f"  {f.name}: {len(entries)} entries ({off_ct} off-topic)")
        all_entries.extend(entries)

    report = build_gap_matrix(all_entries)

    print("\n" + "=" * 60)
    print("CORPUS QUALITY SUMMARY")
    print("=" * 60)
    print(f"  Total entries:          {report['total_entries']}")
    print(f"  Complete  (score ≥ {COMPLETE_THRESHOLD}):  {report['complete']}")
    print(f"  Shallow   (score {SHALLOW_THRESHOLD}–{COMPLETE_THRESHOLD - 1}):   {report['shallow']}")
    print(f"  Skeleton  (score < {SHALLOW_THRESHOLD}):   {report['skeleton']}")
    print(f"  Off-topic (HTB/CTF):    {report['off_topic']}")
    print(f"\n  Gap cells (< {GAP_THRESHOLD} entries): {len(report['gaps'])} / {len(DOMAINS) * len(INCIDENT_TYPES)}")

    if report["gaps"]:
        print(f"\n  Top 10 priority gaps (most critical first):")
        for g in report["gaps"][:10]:
            print(f"    {g['domain']:28} | {g['incident_type']:20} | {g['count']} entries")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"\nGap report written → {args.output}")


if __name__ == "__main__":
    main()
