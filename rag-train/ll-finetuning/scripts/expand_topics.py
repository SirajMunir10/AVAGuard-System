#!/usr/bin/env python3
"""
AVAGuard Advanced Corpus Gap Analyzer & Scenario Catalog Generator
Refactored to use a Hierarchical Realistic Scenario Model and advanced coverage matching.
"""

import os
import json
import re
import time
from pathlib import Path
from collections import Counter

# Import the massive realistic scenario registry
from scenario_data import HIERARCHICAL_CATALOG

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
CORPUS_DIR = PARENT_DIR / "rag" / "corpus"
OUTPUT_CATALOG = PARENT_DIR / "config" / "refined_scenario_catalog.json"
OUTPUT_TOP_100 = PARENT_DIR / "config" / "refined_top_100_missing_scenarios.json"

ARTIFACT_DIR = Path("C:/Users/AhmedMujtaba/.gemini/antigravity-ide/brain/9aa500bc-2581-425d-a3c1-367ab06132c5")
TECH_INVENTORY_REPORT = ARTIFACT_DIR / "technology_inventory_report.md"
DIVERSITY_REPORT = ARTIFACT_DIR / "scenario_diversity_report.md"

SCENARIO_CATEGORIES = [
    "Deployment", "Configuration", "Administration", "Troubleshooting",
    "Monitoring", "Security Hardening", "Incident Response", "Governance",
    "Automation", "Integration", "Migration", "Upgrade",
    "Architecture & Design", "Compliance", "Threat Hunting"
]

TARGET_DOMAINS = ["windows", "azure", "intune", "defender", "sentinel"]

def classify_scenario_category(text: str) -> str:
    """Attempts to classify an existing file's text into one of the 15 new categories."""
    text = text.lower()
    if any(k in text for k in ["threat hunt", "hunting", "kql", "ioc", "indicator"]):
        return "Threat Hunting"
    if any(k in text for k in ["architecture", "design", "topology", "planning"]):
        return "Architecture & Design"
    if any(k in text for k in ["automate", "automation", "pipeline", "ci/cd", "script"]):
        return "Automation"
    if any(k in text for k in ["integration", "integrate", "third-party", "api"]):
        return "Integration"
    if any(k in text for k in ["migrate", "migration", "transition", "cutover"]):
        return "Migration"
    if any(k in text for k in ["upgrade", "update", "patching", "in-place"]):
        return "Upgrade"
    if any(k in text for k in ["troubleshoot", "diagnose", "error", "fail", "resolve"]):
        return "Troubleshooting"
    if any(k in text for k in ["incident", "contain", "remediate", "forensic", "breach"]):
        return "Incident Response"
    if any(k in text for k in ["harden", "secure", "restrict", "baseline", "protect"]):
        return "Security Hardening"
    if any(k in text for k in ["monitor", "log", "alert", "telemetry", "dashboard"]):
        return "Monitoring"
    if any(k in text for k in ["govern", "policy", "audit", "role", "lifecycle"]):
        return "Governance"
    if any(k in text for k in ["compliance", "cis ", "nist", "pci", "hipaa", "audit"]):
        return "Compliance"
    if any(k in text for k in ["deploy", "install", "setup", "provision"]):
        return "Deployment"
    if any(k in text for k in ["configure", "setting", "enable", "disable"]):
        return "Configuration"
    return "Administration"

def classify_domain_subdomain(rel_path: str, filename: str, content: str) -> tuple:
    """Simplified heuristic mapping for existing files."""
    path_lower = rel_path.lower().replace("\\", "/")
    content_lower = content.lower()
    
    if "intune" in path_lower or "intune" in content_lower:
        if "enroll" in path_lower or "enroll" in content_lower:
            return "intune", "Enrollment"
        return "intune", "Device Management"
        
    elif "defender" in path_lower or "defender" in content_lower:
        if "endpoint" in path_lower or "mde" in content_lower:
            return "defender", "Defender for Endpoint"
        return "defender", "Other Defender"
        
    elif any(k in path_lower or k in content_lower for k in ["entra", "aad", "mfa", "pim", "conditional access"]):
        if "conditional access" in path_lower or "conditional access" in content_lower:
            return "azure", "Conditional Access"
        return "azure", "Entra ID"
        
    elif "azure" in path_lower or "azure" in content_lower:
        return "azure", "Azure General"
        
    elif "sentinel" in path_lower or "sentinel" in content_lower:
        return "sentinel", "Microsoft Sentinel"
        
    elif any(k in path_lower or k in content_lower for k in ["windows", "win10", "win11", "ad", "active directory", "gpo"]):
        if "active directory" in path_lower or "adds" in content_lower or "domain controller" in content_lower:
            return "windows", "Active Directory"
        return "windows", "Windows General"
        
    return "other", "General"

def analyze_existing_corpus():
    """Scans and parses the existing files."""
    existing_files = []
    extensions = {".txt", ".md"}

    if not CORPUS_DIR.exists():
        print(f"Warning: Corpus directory not found at {CORPUS_DIR}. Assuming 0 existing files.")
        return existing_files

    for path in CORPUS_DIR.rglob("*"):
        if path.is_file() and path.suffix.lower() in extensions:
            rel_path = path.relative_to(CORPUS_DIR)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read(2048)
            except Exception:
                content = ""
                
            domain, subdomain = classify_domain_subdomain(str(rel_path), path.name, content)
            category = classify_scenario_category(content)
            
            existing_files.append({
                "name": path.name,
                "domain": domain,
                "subdomain": subdomain,
                "category": category,
                "content": content
            })
            
    return existing_files

def calculate_match_confidence(scenario: dict, file_meta: dict) -> float:
    """Technology-aware matching algorithm."""
    confidence = 0.0
    
    s_title = scenario["scenario_title"].lower()
    s_tech = scenario["technology"].lower()
    s_sub = scenario["subdomain"].lower()
    s_cat = scenario["scenario_category"].lower()
    
    f_content = file_meta["content"].lower()
    f_name = file_meta["name"].lower()
    f_sub = file_meta["subdomain"].lower()
    f_cat = file_meta["category"].lower()
    
    # 1. Technology Match (35%)
    # Very important: Does the file actually discuss the specific feature?
    if s_tech in f_content or s_tech in f_name.replace("_", " ").replace("-", " "):
        confidence += 35.0
        
    # 2. Subdomain Match (20%)
    if s_sub == f_sub:
        confidence += 20.0
        
    # 3. Category Match (15%)
    if s_cat == f_cat:
        confidence += 15.0
        
    # 4. Keyword Overlap (30%)
    stop_words = {"and", "or", "the", "a", "an", "with", "for", "to", "in", "of", "on", "at", "by", "from", "as", "is", "are"}
    scen_words = set(re.findall(r'\w+', s_title)) - stop_words
    file_words = set(re.findall(r'\w+', f_name.replace("_", " ").replace("-", " "))) - stop_words
    
    if scen_words:
        overlap = scen_words.intersection(file_words)
        ratio = len(overlap) / len(scen_words)
        confidence += (ratio * 30.0)
        
    return min(round(confidence, 1), 100.0)

def generate_priority_score(item: dict) -> float:
    """Calculates priority based on category and domain."""
    cat = item["scenario_category"]
    dom = item["domain"]
    
    # High priority categories
    if cat in ["Threat Hunting", "Incident Response", "Architecture & Design", "Automation"]:
        score = 5.0
    elif cat in ["Troubleshooting", "Security Hardening", "Integration", "Migration"]:
        score = 4.0
    else:
        score = 3.0
        
    if dom in ["azure", "intune", "defender"]:
        score += 0.5
        
    return min(score, 5.0)

def generate_catalog(existing_files):
    catalog_data = []
    
    for domain, subdomains in HIERARCHICAL_CATALOG.items():
        for subdomain, technologies in subdomains.items():
            for tech, scenarios in technologies.items():
                for s in scenarios:
                    item = {
                        "scenario_title": s["title"],
                        "scenario_category": s["category"],
                        "domain": domain,
                        "subdomain": subdomain,
                        "technology": tech,
                        "is_cis": s["is_cis"],
                        "cis_type": s["cis_type"],
                        "priority_score": 0.0,
                        "existing_coverage": "No",
                        "match_confidence": 0.0
                    }
                    item["priority_score"] = generate_priority_score(item)
                    
                    # Coverage check
                    best_conf = 0.0
                    best_file = None
                    for f in existing_files:
                        if f["domain"] == domain:
                            conf = calculate_match_confidence(item, f)
                            if conf > best_conf:
                                best_conf = conf
                                best_file = f["name"]
                                
                    if best_conf >= 60.0:
                        item["existing_coverage"] = "Yes"
                        item["matched_file"] = best_file
                    item["match_confidence"] = best_conf
                    
                    catalog_data.append(item)
                    
    return catalog_data

def write_technology_inventory_report(catalog):
    hierarchy = {}
    for item in catalog:
        d = item["domain"]
        s = item["subdomain"]
        t = item["technology"]
        
        if d not in hierarchy:
            hierarchy[d] = {}
        if s not in hierarchy[d]:
            hierarchy[d][s] = {}
        if t not in hierarchy[d][s]:
            hierarchy[d][s][t] = 0
            
        hierarchy[d][s][t] += 1
        
    TECH_INVENTORY_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with open(TECH_INVENTORY_REPORT, "w", encoding="utf-8") as f:
        f.write("# Technology Inventory Report\n\n")
        f.write("A detailed breakdown of the realistic Microsoft workloads covered in the new scenario catalog.\n\n")
        
        for d, subs in hierarchy.items():
            f.write(f"## Domain: {d.title()}\n")
            for s, techs in subs.items():
                f.write(f"### Subdomain: {s}\n")
                f.write("| Technology / Feature | Scenario Count |\n")
                f.write("| --- | --- |\n")
                for t, count in techs.items():
                    f.write(f"| {t} | {count} |\n")
                f.write("\n")

def write_scenario_diversity_report(catalog):
    total = len(catalog)
    cat_counts = Counter(s["scenario_category"] for s in catalog)
    dom_counts = Counter(s["domain"] for s in catalog)
    tech_counts = Counter(s["technology"] for s in catalog)
    
    titles = [s["scenario_title"] for s in catalog]
    title_counts = Counter(titles)
    duplicates = sum(c - 1 for c in title_counts.values())
    unique_score = ((total - duplicates) / total) * 100 if total > 0 else 0
    
    # Template phrase analysis (checking for old bad habits)
    old_templates = ["Deploying {", "Remediation: Hardening", "Security Baseline: Restricting", "Incident playbook:"]
    template_matches = 0
    for t in titles:
        if any(tmpl.lower() in t.lower() for tmpl in old_templates):
            template_matches += 1
            
    DIVERSITY_REPORT.parent.mkdir(parents=True, exist_ok=True)
    with open(DIVERSITY_REPORT, "w", encoding="utf-8") as f:
        f.write("# Scenario Diversity & Realism Report\n\n")
        
        f.write("## 1. Quality Metrics\n")
        f.write(f"- **Total Scenarios:** {total}\n")
        f.write(f"- **Exact Duplicates:** {duplicates}\n")
        f.write(f"- **Scenario Uniqueness Score:** {unique_score:.1f}%\n")
        f.write(f"- **Template Phrase Usage:** {template_matches} scenarios containing old generic templates (Target: 0)\n\n")
        
        f.write("## 2. Category Distribution\n")
        f.write("| Category | Count | % of Total |\n")
        f.write("| --- | --- | --- |\n")
        for cat in SCENARIO_CATEGORIES:
            count = cat_counts.get(cat, 0)
            f.write(f"| {cat} | {count} | {(count/total)*100:.1f}% |\n")
            
        f.write("\n## 3. Domain Distribution\n")
        for dom, count in dom_counts.items():
            f.write(f"- **{dom.title()}**: {count} scenarios\n")
            
        f.write("\n## 4. Top 10 Technologies by Coverage\n")
        for tech, count in tech_counts.most_common(10):
            f.write(f"- **{tech}**: {count} scenarios\n")

def main():
    print("Scanning existing corpus for advanced coverage matching...")
    existing_files = analyze_existing_corpus()
    print(f"Found {len(existing_files)} existing files.")
    
    print("Generating hierarchical catalog...")
    catalog = generate_catalog(existing_files)
    
    missing = [s for s in catalog if s["existing_coverage"] == "No"]
    missing.sort(key=lambda x: x["priority_score"], reverse=True)
    
    # Save standard outputs
    OUTPUT_CATALOG.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CATALOG, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2)
        
    with open(OUTPUT_TOP_100, "w", encoding="utf-8") as f:
        json.dump(missing[:100], f, indent=2)
        
    print(f"Saved refined_scenario_catalog.json ({len(catalog)} scenarios).")
    print(f"Saved refined_top_100_missing_scenarios.json.")
    
    # Generate requested reports
    write_technology_inventory_report(catalog)
    write_scenario_diversity_report(catalog)
    print("Quality reports successfully generated in artifact directory.")

if __name__ == "__main__":
    main()
