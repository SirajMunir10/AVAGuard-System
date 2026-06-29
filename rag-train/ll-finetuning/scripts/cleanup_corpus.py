#!/usr/bin/env python3
"""
One-shot corpus cleanup:
1. Normalize domain aliases in grounded corpus (fix "Defender" -> "Defender for Endpoint", etc.)
2. Demote entries scoring < 7 from grounded to pending review
3. Report what changed
"""
import json
from pathlib import Path

DOMAIN_ALIASES = {
    "Defender": "Defender for Endpoint",
    "Microsoft Defender": "Defender for Endpoint",
    "MDE": "Defender for Endpoint",
    "Microsoft Sentinel": "Sentinel",
    "Azure Active Directory": "Entra ID",
    "AAD": "Entra ID",
    "Azure AD": "Entra ID",
    "Microsoft Intune": "Intune",
    "Microsoft Purview": "Purview",
}

VALID_DOMAINS = [
    "Intune", "Entra ID", "Defender for Endpoint", "Defender XDR",
    "Sentinel", "Exchange Online", "Azure", "Purview", "Governance"
]

GROUNDED = Path("rag-train/ll-finetuning/data/corpus_grounded.jsonl")
PENDING  = Path("rag-train/ll-finetuning/data/corpus_pending_review.jsonl")

entries = [json.loads(l) for l in GROUNDED.read_text(encoding="utf-8").splitlines() if l.strip()]

kept = []
demoted = []
normalized = 0

for e in entries:
    # Normalize domain alias
    raw = e.get("domain", "")
    if raw in DOMAIN_ALIASES:
        e["domain"] = DOMAIN_ALIASES[raw]
        normalized += 1

    # Demote if score < 7
    if e.get("completeness_score", 0) < 7:
        demoted.append(e)
    else:
        kept.append(e)

# Rewrite grounded with only high-quality entries
GROUNDED.write_text("\n".join(json.dumps(e) for e in kept) + "\n", encoding="utf-8")

# Append demoted to pending review
with open(PENDING, "a", encoding="utf-8") as f:
    for e in demoted:
        f.write(json.dumps(e) + "\n")

print(f"Domain aliases normalized: {normalized}")
print(f"Kept in grounded (score ≥7): {len(kept)}")
print(f"Demoted to pending (score <7): {len(demoted)}")
print(f"New grounded total: {len(kept)}")
