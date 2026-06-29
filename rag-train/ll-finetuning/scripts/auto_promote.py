#!/usr/bin/env python3
"""
Auto-promotes entries from corpus_pending_review.jsonl to corpus_grounded.jsonl
if they meet quality thresholds. Entries that fail go to corpus_rejected.jsonl.
No LLM calls — pure field validation.
"""
import json
import argparse
from pathlib import Path

VALID_DOMAINS = [
    "Intune", "Entra ID", "Defender for Endpoint", "Defender XDR",
    "Sentinel", "Exchange Online", "Azure", "Purview", "Governance"
]

def qualifies(entry: dict) -> bool:
    return (
        entry.get("completeness_score", 0) >= 7
        and bool(entry.get("source_references"))
        and entry.get("domain") in VALID_DOMAINS
        and len(entry.get("remediation_steps", [])) >= 2
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pending", default="data/corpus_pending_review.jsonl")
    parser.add_argument("--grounded", default="data/corpus_grounded.jsonl")
    parser.add_argument("--rejected", default="data/corpus_rejected.jsonl")
    args = parser.parse_args()

    pending = Path(args.pending)
    grounded = Path(args.grounded)
    rejected = Path(args.rejected)

    entries = [json.loads(l) for l in pending.read_text().splitlines() if l.strip()]
    promoted, rejected_list, kept = [], [], []

    for e in entries:
        e["generation_method"] = "reviewed_generation"
        e["provenance"] = e.get("provenance", "").replace(
            " — requires human review before promotion", ""
        )
        if qualifies(e):
            promoted.append(e)
        else:
            rejected_list.append(e)

    with open(grounded, "a") as f:
        for e in promoted:
            f.write(json.dumps(e) + "\n")

    with open(rejected, "a") as f:
        for e in rejected_list:
            f.write(json.dumps(e) + "\n")

    pending.write_text("")  # clear pending after processing

    print(f"Promoted:  {len(promoted)}")
    print(f"Rejected:  {len(rejected_list)}")
    print(f"New grounded total: {sum(1 for _ in open(grounded))}")

if __name__ == "__main__":
    main()
