#!/usr/bin/env python3
"""
AVAGuard Rejected Corpus Enrichment Tool
Reads data/corpus_rejected.jsonl, identifies entries with completeness_score of 5 or 6,
calls DeepSeek to enrich them with validation and rollback steps, re-scores them,
and promotes successful ones to corpus_grounded.jsonl and exports them to RAG.
"""

import json
import os
import sys
import re
import argparse
import time
from pathlib import Path
from typing import Dict, List, Tuple

# Setup paths relative to script location
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
sys.path.append(str(PARENT_DIR))

from synthetic_data_generator.api_clients import MultiLLMClient

REJECTED_INPUT = PARENT_DIR / "data" / "corpus_rejected.jsonl"
GROUNDED_OUTPUT = PARENT_DIR / "data" / "corpus_grounded.jsonl"
CORPUS_DIR = PARENT_DIR / "rag" / "corpus"

DOMAIN_TO_FOLDER = {
    "Intune":                 "intune",
    "Entra ID":               "entra_id",
    "Defender for Endpoint":  "defender_endpoint",
    "Defender XDR":           "defender_xdr",
    "Sentinel":               "sentinel",
    "Exchange Online":        "exchange_online",
    "Azure":                  "azure_security",
    "Purview":                "purview",
    "Governance":             "governance",
}

ENRICHMENT_SYSTEM_PROMPT = (
    "You are a senior Microsoft cloud security architect. "
    "You generate realistic validation and rollback steps grounded in official Microsoft documentation. "
    "You never invent technical details. You output only valid JSON."
)

ENRICHMENT_PROMPT_TEMPLATE = """Given this Microsoft cloud operations scenario, generate realistic validation steps and rollback steps based on the source documentation.
Do not invent technical details not present in the context provided.
Return ONLY a JSON object with two fields:
{{
  "validation": "detailed verification actions or commands to run to confirm remediation succeeded",
  "rollback": "detailed recovery actions or commands to run if the remediation fails or causes issues"
}}

Scenario details:
Domain: {domain}
Subdomain: {subdomain}
Incident Type: {incident_type}
Query: {query}
Environment Context: {env_context}
Symptoms: {symptoms}
Error Codes: {error_codes}
Root Causes: {root_causes}
Remediation Steps: {remediation_steps}
Source References: {references}
"""

def score_entry(entry: Dict) -> int:
    """Calculate completeness score 0-10 based on standard pipeline rules."""
    score = 0
    refs = entry.get("source_references")
    if refs and isinstance(refs, list) and any(str(r).strip() for r in refs):
        score += 2
    codes = entry.get("error_codes")
    if codes and isinstance(codes, list) and len(codes) > 0:
        score += 2
    steps = entry.get("remediation_steps")
    if steps and isinstance(steps, list) and len(steps) >= 2:
        score += 2
    symptoms = entry.get("symptoms")
    if symptoms and isinstance(symptoms, list) and len(symptoms) > 0:
        score += 1
    ctx = entry.get("environment_context")
    if ctx and isinstance(ctx, dict) and any(v for v in ctx.values() if v):
        score += 1
    if isinstance(entry.get("validation"), str) and entry["validation"].strip():
        score += 1
    if isinstance(entry.get("rollback"), str) and entry["rollback"].strip():
        score += 1
    return score

def format_list(items, numbered=False, force_code=False, is_url=False):
    """Format a list of strings into Markdown list representation."""
    if not items:
        return "N/A"
    if isinstance(items, str):
        items = [items]
    if not isinstance(items, list):
        return str(items)
    
    items = [str(item).strip() for item in items if str(item).strip()]
    if not items:
        return "N/A"
    
    lines = []
    for idx, item in enumerate(items, 1):
        if force_code:
            if not (item.startswith('`') and item.endswith('`')):
                item = f"`{item}`"
        if is_url:
            if item.startswith('http') and not (item.startswith('<') and item.endswith('>')):
                item = f"<{item}>"
        
        prefix = f"{idx}. " if numbered else "- "
        lines.append(f"{prefix}{item}")
    return "\n".join(lines)

def export_entry_to_md(entry: dict, file_id: str):
    """Export the promoted entry as a markdown file in the appropriate directory."""
    domain = entry.get("domain", "General")
    subfolder_name = DOMAIN_TO_FOLDER.get(domain)
    
    if not subfolder_name:
        subfolder_name = re.sub(r"[^a-z0-9]+", "_", domain.lower()).strip("_")
    
    dest_dir = CORPUS_DIR / subfolder_name
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    dest_file = dest_dir / f"{file_id}.md"
    
    # Title format: "IncidentType: Subdomain (Error Code)"
    title = f"{entry.get('incident_type', 'Scenario')}: {entry.get('subdomain', 'General Configuration')}"
    error_codes = entry.get("error_codes")
    if error_codes and isinstance(error_codes, list) and len(error_codes) > 0:
        clean_code = str(error_codes[0]).strip()
        if clean_code:
            title += f" ({clean_code})"
    title = re.sub(r"\s+", " ", title).strip()
    
    content = f"""# {title}

**Domain:** {domain}
**Subdomain:** {entry.get('subdomain', 'N/A')}
**Incident Type:** {entry.get('incident_type', 'N/A')}

## Scenario / Query
{entry.get('query', 'N/A')}

## Environment Context
- **Tenant Type:** {entry.get('environment_context', {}).get('tenant_type', 'N/A') or 'N/A'}
- **Configuration:** {entry.get('environment_context', {}).get('relevant_config', 'N/A') or 'N/A'}

## Symptoms
{format_list(entry.get('symptoms'))}

## Error Codes
{format_list(entry.get('error_codes'), force_code=True)}

## Root Causes
{format_list(entry.get('root_causes'), numbered=True)}

## Remediation Steps
{format_list(entry.get('remediation_steps'), numbered=True)}

## Validation
{entry.get('validation') or 'N/A'}

## Rollback
{entry.get('rollback') or 'N/A'}

## References
{format_list(entry.get('source_references'), is_url=True)}
"""
    
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(content)

def clean_json_response(text: str) -> str:
    """Strips markdown fences or preamble from response text."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def main():
    parser = argparse.ArgumentParser(description="Enrich rejected corpus entries with validation and rollback steps")
    parser.add_argument("--max-entries", type=int, default=0, help="Maximum entries to enrich (0 = all)")
    parser.add_argument("--provider", type=str, default="deepseek", help="LLM provider to use")
    args = parser.parse_args()

    if not REJECTED_INPUT.exists():
        print(f"Error: Rejected input file {REJECTED_INPUT} does not exist.")
        sys.exit(1)

    print("Initializing MultiLLMClient...")
    client = MultiLLMClient()
    available = client.get_initialized_providers()
    if args.provider not in available:
        print(f"Warning: Requested provider '{args.provider}' not initialized. Fallbacks available: {available}")

    # Load existing grounded IDs to avoid duplication and help in seen counts
    grounded_ids = set()
    if GROUNDED_OUTPUT.exists():
        with open(GROUNDED_OUTPUT, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        g_entry = json.loads(line)
                        g_id = g_entry.get("id")
                        if g_id:
                            grounded_ids.add(g_id.lower())
                    except Exception:
                        pass

    # Read all rejected entries
    print(f"Reading rejected entries from {REJECTED_INPUT}...")
    all_rejected = []
    with open(REJECTED_INPUT, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    all_rejected.append(json.loads(line))
                except Exception as e:
                    print(f"Skipping malformed line: {e}")

    target_entries = []
    other_entries = []
    already_grounded_in_rejected = []

    for entry in all_rejected:
        eid = entry.get("id", "unnamed-entry")
        eid_lower = eid.lower()
        score = entry.get("completeness_score", 0)
        
        if eid_lower in grounded_ids:
            continue
            
        if score >= 7:
            already_grounded_in_rejected.append(entry)
        elif score in (5, 6):
            target_entries.append(entry)
        else:
            other_entries.append(entry)

    print(f"Found {len(already_grounded_in_rejected)} entries with score >= 7 in rejected. Promoting immediately...")
    if already_grounded_in_rejected:
        with open(GROUNDED_OUTPUT, "a", encoding="utf-8") as f:
            for entry in already_grounded_in_rejected:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        seen_ids = {}
        for entry in already_grounded_in_rejected:
            eid = entry.get("id", "unnamed-entry")
            eid_lower = eid.lower()
            if eid_lower in grounded_ids:
                seen_ids[eid_lower] = seen_ids.get(eid_lower, 0) + 1
                file_id = f"{eid_lower}-promoted-{int(time.time())}-{seen_ids[eid_lower]}"
            else:
                file_id = eid_lower
                grounded_ids.add(eid_lower)
            export_entry_to_md(entry, file_id)
        print(f"  [OK] Promoted {len(already_grounded_in_rejected)} already-good entries.")

    print(f"Found {len(target_entries)} entries with completeness_score of 5 or 6 to process.")
    
    if args.max_entries > 0:
        print(f"Limiting enrichment run to first {args.max_entries} target entries.")
        target_to_process = target_entries[:args.max_entries]
        target_remaining = target_entries[args.max_entries:]
    else:
        target_to_process = target_entries
        target_remaining = []

    still_rejected = list(other_entries) + list(target_remaining)
    total_processed = len(target_to_process)
    promoted_count = 0
    failed_count = 0
    seen_ids = {}

    print(f"Enriching {total_processed} entries using LLM provider '{args.provider}'...")
    
    for idx, entry in enumerate(target_to_process, 1):
        eid = entry.get("id", "unnamed-entry")
        eid_lower = eid.lower()
        
        if eid_lower in grounded_ids:
            print(f"[{idx}/{total_processed}] Skipping entry {eid} (already in grounded)...")
            promoted_count += 1
            continue
            
        print(f"[{idx}/{total_processed}] Enriching entry {eid} (Current Score: {entry.get('completeness_score')})...")
        
        prompt = ENRICHMENT_PROMPT_TEMPLATE.format(
            domain=entry.get("domain", "N/A"),
            subdomain=entry.get("subdomain", "N/A"),
            incident_type=entry.get("incident_type", "N/A"),
            query=entry.get("query", "N/A"),
            env_context=json.dumps(entry.get("environment_context", {})),
            symptoms=json.dumps(entry.get("symptoms", [])),
            error_codes=json.dumps(entry.get("error_codes", [])),
            root_causes=json.dumps(entry.get("root_causes", [])),
            remediation_steps=json.dumps(entry.get("remediation_steps", [])),
            references=json.dumps(entry.get("source_references", []))
        )

        response = None
        for attempt in range(3):
            try:
                response = client.call(
                    args.provider,
                    prompt,
                    system_prompt=ENRICHMENT_SYSTEM_PROMPT,
                    temperature=0.2,
                    max_tokens=1000
                )
                if response:
                    break
            except Exception as e:
                wait = 2 ** attempt
                print(f"  Attempt {attempt+1}/3 failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)

        if not response:
            print("  Failed to get response from LLM. Leaving in rejected.")
            still_rejected.append(entry)
            failed_count += 1
            continue

        clean_resp = clean_json_response(response)
        try:
            res_json = json.loads(clean_resp)
            validation = res_json.get("validation", "").strip()
            rollback = res_json.get("rollback", "").strip()
            
            if not validation and not rollback:
                print("  LLM returned empty validation and rollback fields. Leaving in rejected.")
                still_rejected.append(entry)
                failed_count += 1
                continue

            entry["validation"] = validation
            entry["rollback"] = rollback
            new_score = score_entry(entry)
            entry["completeness_score"] = new_score
            
            print(f"  Enriched successfully! New Score: {new_score}")
            
            if new_score >= 7:
                with open(GROUNDED_OUTPUT, "a", encoding="utf-8") as f:
                    f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                
                if eid_lower in grounded_ids:
                    seen_ids[eid_lower] = seen_ids.get(eid_lower, 0) + 1
                    file_id = f"{eid_lower}-promoted-{int(time.time())}-{seen_ids[eid_lower]}"
                else:
                    file_id = eid_lower
                    grounded_ids.add(eid_lower)
                
                export_entry_to_md(entry, file_id)
                promoted_count += 1
                print(f"  [OK] PROMOTED to grounded (Score: {new_score})")
            else:
                still_rejected.append(entry)
                failed_count += 1
                print(f"  [FAIL] Score {new_score} < 7. Remaining in rejected.")
                
        except Exception as e:
            print(f"  Failed to parse or process LLM response: {e}. Raw response: {response[:150]}")
            still_rejected.append(entry)
            failed_count += 1

        time.sleep(0.5)

    # Overwrite rejected file with remaining entries
    print(f"Rewriting {REJECTED_INPUT} with {len(still_rejected)} remaining entries...")
    with open(REJECTED_INPUT, "w", encoding="utf-8") as f:
        for entry in still_rejected:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print("\n" + "="*50)
    print("ENRICHMENT RUN SUMMARY")
    print("="*50)
    print(f"Total target entries processed: {total_processed}")
    print(f"Successfully promoted:         {promoted_count} ({promoted_count/total_processed*100:.1f}%)" if total_processed > 0 else "Total processed: 0")
    print(f"Failed to promote:             {failed_count}")
    print(f"Remaining in rejected:         {len(still_rejected)}")

if __name__ == "__main__":
    main()
