import os
import json
import re
from pathlib import Path
from collections import Counter

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
CATALOG_PATH = PARENT_DIR / "config" / "scenario_catalog.json"
ARTIFACT_DIR = Path("C:/Users/AhmedMujtaba/.gemini/antigravity-ide/brain/9aa500bc-2581-425d-a3c1-367ab06132c5")
REPORT_PATH = ARTIFACT_DIR / "catalog_quality_report.md"

# Known templates from the previous generator
KNOWN_TEMPLATE_PHRASES = [
    "Deploying", "to establish secure baseline controls",
    "Configuring", "integrations in a hybrid enterprise environment",
    "Establishing secure deployment architecture for",
    "Remediation: Hardening", "settings to mitigate",
    "Security Baseline: Restricting", "access and disabling insecure default protocols",
    "Applying security hardening guidelines to secure",
    "sync failures and resolving",
    "Diagnosing deployment bottlenecks and resolving connection timeouts in",
    "Resolving access denied errors and sync loops during",
    "Configuring diagnostic logging and forwarding rules for",
    "Setting up security alert rules and health monitoring profiles for",
    "Creating custom telemetry dashboards and logging pipelines for",
    "Incident playbook: Containing and remediating active",
    "Response runbook: Remediating unauthorized access and compromised keys in",
    "Triage and containment guide for",
    "Governance rules: Auditing role assignments and boundary controls for",
    "Enforcing resource tagging policies and subscription lifecycle rules for",
    "Reviewing access permissions and configuring role boundaries for",
    "CIS Audit: Validating", "settings against CIS benchmark controls",
    "CIS Validation: Testing and verifying",
    "CIS Remediation: Enforcing baseline controls for",
    "CIS Troubleshooting: Resolving configuration conflicts during",
    "PowerShell runbook: Automating", "status audits and reporting",
    "CLI runbook: Automating backups and rotation routines for",
    "Operational checklist: Scheduled health and security audits for",
    "Best practices guide: Secure configuration and maintenance of",
    "Security checklist: Operational recommendations for hardening",
    "Architecture guide: Design patterns for deploying high-availability",
    "Upgrade plan: Deploying features and updates for",
    "Rollback runbook: Troubleshooting upgrade failures in",
    "Validation checklist: Post-upgrade verification steps for",
    "Migration roadmap: Transitioning legacy controls to",
    "Cutover plan: Secure resource migration to",
    "Verification runbook: Post-migration data integrity checks for",
    "Administration guide: Managing tenant-wide settings for",
    "Operations guide: Configuring resource allocation and user settings for",
    "Operator manual: Managing active sessions and provisioning roles in"
]

def analyze_catalog():
    if not CATALOG_PATH.exists():
        print(f"Catalog not found at {CATALOG_PATH}")
        return
        
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    total_scenarios = 0
    template_matches = 0
    domains = {}
    categories = Counter()
    all_titles = []
    
    for domain, subdomains in catalog.items():
        domains[domain] = {"total": 0, "subdomains": {}}
        for sub, scenarios in subdomains.items():
            domains[domain]["subdomains"][sub] = len(scenarios)
            domains[domain]["total"] += len(scenarios)
            for s in scenarios:
                total_scenarios += 1
                categories[s["scenario_category"]] += 1
                title = s["scenario_title"]
                all_titles.append(title)
                
                # Check if title matches known templates
                matched = False
                for phrase in KNOWN_TEMPLATE_PHRASES:
                    if phrase.lower() in title.lower():
                        matched = True
                        break
                if matched:
                    template_matches += 1
                    
    # Duplicates analysis
    title_counts = Counter(all_titles)
    exact_duplicates = {t: c for t, c in title_counts.items() if c > 1}
    
    # Write report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# Catalog Quality Audit Report (Current State)\n\n")
        
        f.write("## Executive Summary\n")
        f.write(f"- **Total Scenarios Analyzed:** {total_scenarios}\n")
        f.write(f"- **Template-Driven Scenarios:** {template_matches} ({(template_matches/total_scenarios)*100:.1f}%)\n")
        f.write(f"- **Exact Title Duplicates:** {sum(c-1 for c in exact_duplicates.values())} duplicated scenarios.\n\n")
        
        f.write("> [!WARNING]\n")
        f.write("> The current catalog is heavily reliant on sentence formatting templates, which creates a lack of true technical diversity. As seen above, a large percentage of generated titles reuse identical phrasings instead of focusing on specific operational realities.\n\n")
        
        f.write("## Category Diversity\n")
        f.write("| Category | Count | % of Total |\n")
        f.write("| --- | --- | --- |\n")
        for cat, count in categories.most_common():
            f.write(f"| {cat} | {count} | {(count/total_scenarios)*100:.1f}% |\n")
            
        f.write("\n## Subdomain Coverage Snapshot\n")
        for d, data in domains.items():
            f.write(f"### {d.replace('_', ' ').title()} ({data['total']} scenarios)\n")
            for sub, count in data["subdomains"].items():
                f.write(f"- {sub}: {count}\n")
            f.write("\n")
            
    print(f"Generated {REPORT_PATH}")

if __name__ == "__main__":
    analyze_catalog()
