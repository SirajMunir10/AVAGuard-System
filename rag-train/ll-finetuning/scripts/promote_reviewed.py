#!/usr/bin/env python3
"""
AVAGuard Reviewed Entry Promoter

Interactive CLI that walks a reviewer through corpus_pending_review.jsonl.
Each entry is presented with key fields; the reviewer accepts, skips, or rejects.

  [a]ccept  → strip llm_gap_fill flag, promote to corpus_grounded.jsonl
  [r]eject  → move to corpus_rejected.jsonl
  [s]kip    → remains in corpus_pending_review.jsonl
  [q]uit    → save progress and stop (remaining entries stay in pending)

Prints a tally at the end of each session.

Usage:
    python promote_reviewed.py
    python promote_reviewed.py --pending data/corpus_pending_review.jsonl
    python promote_reviewed.py --grounded data/corpus_grounded.jsonl
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent

DEFAULT_PENDING  = PARENT_DIR / "data" / "corpus_pending_review.jsonl"
DEFAULT_GROUNDED = PARENT_DIR / "data" / "corpus_grounded.jsonl"
DEFAULT_REJECTED = PARENT_DIR / "data" / "corpus_rejected.jsonl"


# ── JSONL helpers ──────────────────────────────────────────────────────────────
def load_jsonl(path: Path) -> List[Dict]:
    """Load all entries from a JSONL file; skips malformed lines silently."""
    if not path.exists():
        return []
    entries: List[Dict] = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict):
                entries.append(obj)
        except json.JSONDecodeError:
            pass
    return entries


def write_jsonl(path: Path, entries: List[Dict]) -> None:
    """Overwrite a JSONL file with the given entries (used to rewrite pending)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def append_jsonl(path: Path, entries: List[Dict]) -> None:
    """Append entries to an existing JSONL file; creates it if absent."""
    if not entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── Entry display ──────────────────────────────────────────────────────────────
def show_entry_summary(entry: Dict, index: int, total: int) -> None:
    """
    Print the key fields of a corpus entry to assist the reviewer's decision.
    Displays enough context to evaluate operational depth without scrolling.
    """
    print("\n" + "=" * 72)
    print(f"  Entry {index} / {total}")
    print("=" * 72)
    print(f"  ID:            {entry.get('id', 'N/A')}")
    print(f"  Domain:        {entry.get('domain', 'N/A')}")
    print(f"  Subdomain:     {entry.get('subdomain', 'N/A')}")
    print(f"  Incident type: {entry.get('incident_type', 'N/A')}")
    print(f"  Score:         {entry.get('completeness_score', 'N/A')} / 10")
    print(f"  Generation:    {entry.get('generation_method', 'N/A')}")
    print(f"  Provenance:    {entry.get('provenance', 'N/A')}")
    print(f"\n  QUERY:\n    {entry.get('query', 'N/A')}")

    symptoms = entry.get("symptoms") or []
    if symptoms:
        print(f"\n  SYMPTOMS ({len(symptoms)}):")
        for s in symptoms[:3]:
            print(f"    • {str(s)[:100]}")
        if len(symptoms) > 3:
            print(f"    … ({len(symptoms) - 3} more)")

    error_codes = entry.get("error_codes") or []
    if error_codes:
        print(f"\n  ERROR CODES: {', '.join(str(c) for c in error_codes)}")

    steps = entry.get("remediation_steps") or []
    if steps:
        print(f"\n  REMEDIATION ({len(steps)} steps):")
        for i, s in enumerate(steps[:2], 1):
            print(f"    {i}. {str(s)[:100]}")
        if len(steps) > 2:
            print(f"    … ({len(steps) - 2} more steps)")

    refs = entry.get("source_references") or []
    if refs:
        print(f"\n  SOURCE: {refs[0]}")

    citation = entry.get("citation", "")
    if citation:
        print(f"  CITATION: {citation}")


# ── Review loop ────────────────────────────────────────────────────────────────
def promote_entries(
    pending_path: Path,
    grounded_path: Path,
    rejected_path: Path,
) -> None:
    """
    Interactive review loop over all pending entries.

    State machine per entry:
      [a] → promote:  set generation_method=reviewed_generation,
                      remove "requires human review" clause from provenance,
                      append to grounded corpus.
      [r] → reject:   append to corpus_rejected.jsonl as-is.
      [s] → skip:     entry remains in corpus_pending_review.jsonl.
      [q] / Ctrl+C:   save progress, add remaining entries to skipped, stop loop.

    Rewrites corpus_pending_review.jsonl with only the skipped entries at the end.
    """
    pending = load_jsonl(pending_path)
    if not pending:
        print(f"No pending entries found in: {pending_path}")
        return

    print(f"\n{'=' * 72}")
    print("  AVAGuard Corpus Review Tool")
    print(f"  Pending entries to review: {len(pending)}")
    print(f"  Grounded corpus:  {grounded_path}")
    print(f"  Rejected file:    {rejected_path}")
    print(f"{'=' * 72}")
    print("  Commands: [a]ccept | [s]kip | [r]eject | [q]uit\n")

    accepted: List[Dict] = []
    rejected: List[Dict] = []
    skipped:  List[Dict] = []
    quit_early = False

    for i, entry in enumerate(pending, 1):
        show_entry_summary(entry, i, len(pending))
        print()

        while True:
            try:
                choice = input("  Decision [a/s/r/q]: ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print("\n  Interrupted — saving progress…")
                skipped.append(entry)
                quit_early = True
                break

            if choice == "a":
                promoted = dict(entry)
                # Strip the llm_gap_fill marker — entry is now human-reviewed
                promoted["generation_method"] = "reviewed_generation"
                # Clean up the provenance note added by the gap-fill pipeline
                prov = promoted.get("provenance", "")
                promoted["provenance"] = prov.replace(
                    " — requires human review before promotion", ""
                ).strip()
                accepted.append(promoted)
                print("  ✓ Accepted → will be promoted to grounded corpus")
                break

            elif choice == "s":
                skipped.append(entry)
                print("  → Skipped (stays in pending review)")
                break

            elif choice == "r":
                rejected.append(entry)
                print("  ✗ Rejected → will be moved to corpus_rejected.jsonl")
                break

            elif choice == "q":
                print("  Quitting — saving progress…")
                skipped.append(entry)
                quit_early = True
                break

            else:
                print("  Invalid input. Enter a, s, r, or q.")

        if quit_early:
            # All unreviewed entries are automatically skipped (stay in pending)
            remaining_start = i  # i is 1-indexed; pending[i:] gives the rest
            skipped.extend(pending[remaining_start:])
            break

    # Persist results
    if accepted:
        append_jsonl(grounded_path, accepted)
    if rejected:
        append_jsonl(rejected_path, rejected)
    write_jsonl(pending_path, skipped)  # rewrite pending with only skipped entries

    # Session summary
    print(f"\n{'=' * 50}")
    print("  REVIEW SESSION COMPLETE")
    print(f"{'=' * 50}")
    print(f"  Accepted → corpus_grounded.jsonl:       {len(accepted)}")
    print(f"  Rejected → corpus_rejected.jsonl:       {len(rejected)}")
    print(f"  Skipped  → corpus_pending_review.jsonl: {len(skipped)}")
    print()
    if accepted:
        print(f"  Grounded corpus: {grounded_path}")
    if rejected:
        print(f"  Rejected file:   {rejected_path}")
    if skipped:
        print(f"  Pending file:    {pending_path} ({len(skipped)} entries remaining)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Interactively review pending corpus entries and promote approved ones"
    )
    parser.add_argument(
        "--pending", type=Path, default=DEFAULT_PENDING,
        help=f"Pending review file (default: {DEFAULT_PENDING})",
    )
    parser.add_argument(
        "--grounded", type=Path, default=DEFAULT_GROUNDED,
        help=f"Grounded corpus file (default: {DEFAULT_GROUNDED})",
    )
    parser.add_argument(
        "--rejected", type=Path, default=DEFAULT_REJECTED,
        help=f"Rejected entries file (default: {DEFAULT_REJECTED})",
    )
    args = parser.parse_args()

    promote_entries(args.pending, args.grounded, args.rejected)


if __name__ == "__main__":
    main()
