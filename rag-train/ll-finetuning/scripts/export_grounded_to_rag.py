#!/usr/bin/env python3
"""
AVAGuard Grounded Corpus to RAG Exporter
Reads data/corpus_grounded.jsonl and exports each scenario to an individual .md file
in mapped subdirectories under rag/corpus/.
"""

import json
import os
import re
from pathlib import Path

# Setup paths relative to script location
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
GROUNDED_INPUT = PARENT_DIR / "data" / "corpus_grounded.jsonl"
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

def format_list(items, numbered=False, force_code=False, is_url=False):
    """Format a list of strings into Markdown list representation."""
    if not items:
        return "N/A"
    if isinstance(items, str):
        items = [items]
    if not isinstance(items, list):
        return str(items)
    
    # filter empty values
    items = [str(item).strip() for item in items if str(item).strip()]
    if not items:
        return "N/A"
    
    lines = []
    for idx, item in enumerate(items, 1):
        if force_code:
            # wrap in backticks if not already
            if not (item.startswith('`') and item.endswith('`')):
                item = f"`{item}`"
        if is_url:
            if item.startswith('http'):
                # Avoid nesting angle brackets or double wrapping
                if not (item.startswith('<') and item.endswith('>')):
                    item = f"<{item}>"
        
        prefix = f"{idx}. " if numbered else "- "
        lines.append(f"{prefix}{item}")
    return "\n".join(lines)

def export_entry(entry: dict, file_id: str) -> Path:
    """Formats and writes a single JSONL entry to a Markdown file in the mapped directory."""
    domain = entry.get("domain", "General")
    subfolder_name = DOMAIN_TO_FOLDER.get(domain)
    
    if not subfolder_name:
        # Fallback to standard slugified domain name
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
            
    # Clean the title of markdown characters or multiple spaces
    title = re.sub(r"\s+", " ", title).strip()
    
    # Standard template formatting
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
        
    return dest_file

def slugify_topic(incident_type: str, subdomain: str) -> str:
    """Creates a clean, safe filename slug from incident type and subdomain."""
    text = f"{incident_type} {subdomain}"
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    text = text.strip('_')
    if len(text) > 120:
        text = text[:120].strip('_')
    return text

def main():
    if not GROUNDED_INPUT.exists():
        print(f"Error: Grounded input file {GROUNDED_INPUT} does not exist.")
        return
        
    print(f"Exporting entries from {GROUNDED_INPUT} to RAG corpus under {CORPUS_DIR}...")
    
    # Tracked .md files to preserve
    TRACKED_MD_FILES = {
        "azure_security_01_entra_id_conditional_access_policies.md",
        "azure_security_02_entra_id_mfa_setup_enforcement.md",
        "azure_security_03_entra_id_privileged_identity_management.md",
        "azure_security_04_entra_id_identity_protection_risk_polic.md",
        "azure_security_05_entra_id_b2b_b2c_guest_access_NEEDS_REVIEW.md"
    }
    
    # 1. Clean up existing untracked/old .md files in the subfolders of CORPUS_DIR
    print("Cleaning up old untracked .md files in RAG corpus subfolders...")
    for root, dirs, files in os.walk(CORPUS_DIR):
        for file in files:
            if file.endswith(".md") and file not in TRACKED_MD_FILES:
                file_path = Path(root) / file
                try:
                    file_path.unlink()
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

    # 2. First Pass: Read entries and compute topic frequency counts per subfolder
    entries = []
    topic_counts = {} # key: (subfolder, topic_slug) -> count
    
    with open(GROUNDED_INPUT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                domain = entry.get("domain", "General")
                subfolder_name = DOMAIN_TO_FOLDER.get(domain)
                if not subfolder_name:
                    subfolder_name = re.sub(r"[^a-z0-9]+", "_", domain.lower()).strip("_")
                
                incident_type = entry.get("incident_type", "Scenario")
                subdomain = entry.get("subdomain", "General Configuration")
                topic_slug = slugify_topic(incident_type, subdomain)
                
                key = (subfolder_name, topic_slug)
                topic_counts[key] = topic_counts.get(key, 0) + 1
                entries.append((entry, key, topic_slug))
            except Exception as e:
                print(f"Failed to parse line during first pass: {line[:100]}... Error: {e}")

    # 3. Second Pass: Export entries with proper filenames
    count = 0
    folder_counts = {}
    seen_counts = {} # key: (subfolder, topic_slug) -> current_index
    
    for entry, key, topic_slug in entries:
        try:
            total_for_key = topic_counts[key]
            if total_for_key > 1:
                seen_counts[key] = seen_counts.get(key, 0) + 1
                file_id = f"{topic_slug}_part_{seen_counts[key]}"
            else:
                file_id = topic_slug
            
            dest_path = export_entry(entry, file_id)
            folder_name = dest_path.parent.name
            folder_counts[folder_name] = folder_counts.get(folder_name, 0) + 1
            count += 1
        except Exception as e:
            print(f"Failed to export entry {entry.get('id', 'unnamed')}: {e}")
            
    print("\nExport run complete!")
    print(f"Total entries exported: {count}")
    print("\nCreated files per folder:")
    for folder, c in sorted(folder_counts.items()):
        print(f"  - {folder}/: {c} files")

if __name__ == "__main__":
    main()
