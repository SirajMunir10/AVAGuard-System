#!/usr/bin/env python3
"""
CIS JSON -> Corpus File Post-Processor

Reads structured CIS benchmark JSON files (produced by CIS_AutomationV2) and
converts each control into a self-contained .txt corpus file suitable for RAG indexing.

Strategy:
  - Groups controls sharing the same CIS control ID into a single corpus file
  - Each file targets 700-1,000 words; groups are split if they exceed ~1,200
  - Merges grouped controls into a single flowing technical article format
  - Names files: cis_[framework]_[control-id]_[short-topic].txt

Usage:
    python cis_to_corpus.py
    python cis_to_corpus.py --input-dir path/to/json --output-dir path/to/corpus/cis_benchmarks
    python cis_to_corpus.py --dry-run --verbose
"""

import json
import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict


# === Defaults ===
SCRIPT_DIR = Path(__file__).parent
DEFAULT_INPUT_DIR = Path(r"c:\AVA\CIS_AutmationV2\output\json")
DEFAULT_OUTPUT_DIR = Path(r"c:\AVA\rag-train\ll-finetuning\rag\corpus\cis_benchmarks")

# Word count targets
MIN_USEFUL = 50       # Skip controls with fewer words than this
TARGET_MIN = 700      # Ideal minimum
TARGET_MAX = 1000     # Ideal maximum
SPLIT_THRESHOLD = 1200  # Split groups above this


def slugify(text: str, max_length: int = 40) -> str:
    """Convert text to a clean filename slug."""
    text = text.lower()
    # Remove benchmark prefixes
    text = re.sub(r'^(azure\s+databricks|microsoft\s+azure|azure|intune\s+)\s*', '', text)
    text = re.sub(r'\d+\.\d+(\.\d+)*\s*', '', text)
    text = re.sub(r'[^a-z0-9]+', '_', text)
    text = re.sub(r'_+', '_', text)
    text = text.strip('_')
    if len(text) > max_length:
        text = text[:max_length].rsplit('_', 1)[0]
    return text or 'control'


def get_framework_slug(metadata: dict) -> str:
    """Extract framework slug from benchmark metadata."""
    btype = metadata.get('benchmark_type', '').lower()
    title = metadata.get('title', '').lower()
    source = metadata.get('source_file', '').lower()

    if 'intune' in source or 'intune' in title:
        if 'windows_11' in source or 'windows 11' in title or 'win11' in source:
            return 'intune_win11'
        elif 'windows_10' in source or 'windows 10' in title or 'win10' in source:
            return 'intune_win10'
        return 'intune'
    elif 'azure' in btype or 'azure' in title:
        return 'azure'
    elif 'aws' in btype or 'aws' in title:
        return 'aws'
    elif 'windows' in btype or 'windows' in title:
        return 'windows'
    elif 'linux' in btype or 'linux' in title or 'ubuntu' in source:
        return 'linux'
    elif 'kubernetes' in btype or 'kubernetes' in title:
        return 'kubernetes'
    else:
        return slugify(btype or title or 'unknown', 15)


def render_group_text(group: List[dict], benchmark_title: str) -> str:
    """Render a group of controls into a flowing plain-text article."""
    parts = []
    
    cid = group[0].get('control_id', 'Unknown')
    title = group[0].get('title', 'Untitled Control')
    
    if len(group) == 1:
        parts.append(f"{cid}: {title}")
    else:
        parts.append(f"{cid}: {title} (and related controls)")
    parts.append("")
    
    descs = []
    rationales = []
    audits = []
    remediations = []
    takeaway_sources = []
    
    for c in group:
        sub_title = c.get('title', '')
        
        desc = (c.get('description') or '').strip()
        if desc: descs.append(desc)
            
        rat = (c.get('rationale') or '').strip()
        if rat:
            rationales.append(rat)
            takeaway_sources.append(rat)
        elif desc:
            takeaway_sources.append(desc)
            
        aud = (c.get('audit') or c.get('audit_procedure') or '').strip()
        if aud: audits.append(f"For {sub_title}:\n{aud}" if len(group) > 1 else aud)
            
        rem = (c.get('remediation') or c.get('remediation_steps') or '').strip()
        if rem: remediations.append(f"For {sub_title}:\n{rem}" if len(group) > 1 else rem)
        
    if descs:
        parts.append("Overview")
        parts.append("\n\n".join(descs))
        parts.append("")
        
    if rationales:
        parts.append("Why This Matters")
        parts.append("\n\n".join(rationales))
        parts.append("")
        
    if audits:
        parts.append("Audit Steps")
        parts.append("\n\n".join(audits))
        parts.append("")
        
    if remediations:
        parts.append("Remediation")
        parts.append("\n\n".join(remediations))
        parts.append("")
        
    # Extract Key Takeaways
    combined_source = " ".join(takeaway_sources)
    sentences = [s.strip() for s in combined_source.replace('\n', ' ').split('.') if len(s.strip()) > 20]
    
    # Simple deduplication while preserving order
    seen = set()
    unique_sentences = []
    for s in sentences:
        if s not in seen:
            seen.add(s)
            unique_sentences.append(s)
            
    takeaways = []
    if len(unique_sentences) >= 3:
        takeaways = unique_sentences[:3]
    elif len(unique_sentences) > 0:
        takeaways = unique_sentences
    else:
        takeaways = [f"This control mitigates risks associated with {title.lower()}."]
        
    parts.append("Key Takeaways")
    for t in takeaways:
        if not t.endswith('.'): t += '.'
        # Remove common bullet prefix if it happens to have one
        t = t.lstrip('•*- ')
        parts.append(f"- {t}")
    parts.append("")
    
    return "\n".join(parts)


def write_corpus_file(filepath: Path, text: str, dry_run: bool) -> int:
    """Write a corpus file and return word count."""
    if not dry_run:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
    return len(text.split())


def process_json_file(
    json_path: Path,
    output_dir: Path,
    dry_run: bool = False,
    verbose: bool = False
) -> Dict[str, Any]:
    """Process a single CIS JSON file and produce corpus .txt files."""

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    metadata = data.get("metadata", {})
    controls = data.get("controls", [])
    benchmark_title = metadata.get("title", json_path.stem)
    source_file = metadata.get("source_file", json_path.name)
    framework = get_framework_slug(metadata)

    framework_dir = output_dir / framework

    stats = {
        "source": source_file,
        "framework": framework,
        "total_controls": len(controls),
        "files_created": 0,
        "skipped_empty": 0,
        "under_target": 0,
        "in_target": 0,
        "over_target": 0,
        "word_counts": [],
    }

    print(f"\n{'='*60}")
    print(f"Processing: {source_file}")
    print(f"Framework: {framework}")
    print(f"Controls: {len(controls)}")
    print(f"Output: {framework_dir}")
    print(f"{'='*60}")

    # Group controls by CIS control ID
    groups = defaultdict(list)
    for control in controls:
        cid = control.get('control_id', '')
        if not cid:
            continue

        # Count words naively to filter empty ones
        desc = control.get('description', '') or ''
        rat = control.get('rationale', '') or ''
        aud = control.get('audit', '') or control.get('audit_procedure', '') or ''
        rem = control.get('remediation', '') or control.get('remediation_steps', '') or ''
        
        wc = len((desc + rat + aud + rem).split())

        if wc < MIN_USEFUL:
            stats["skipped_empty"] += 1
            if verbose:
                print(f"  SKIP {cid}: Only {wc} words (empty control)")
            continue

        groups[cid].append(control)

    if verbose:
        singles = sum(1 for g in groups.values() if len(g) == 1)
        multis = sum(1 for g in groups.values() if len(g) > 1)
        print(f"  Unique CIS IDs: {len(groups)} (singles: {singles}, groups: {multis})")

    used_filenames = set()

    for cid in sorted(groups.keys(), key=lambda x: [int(p) if p.isdigit() else p for p in x.split('.')]):
        group = groups[cid]
        cid_slug = cid.replace('.', '_')
        topic_slug = slugify(group[0]["title"], 35)

        # Merge into batches targeting 700-1000 words
        batches = _batch_controls(group, TARGET_MIN, TARGET_MAX)
        for i, batch in enumerate(batches, 1):
            batch_text = render_group_text(batch, benchmark_title)
            suffix = f"part{i}" if len(batches) > 1 else ""
            base_name = f"cis_{framework}_{cid_slug}_{topic_slug}"
            if suffix:
                base_name += f"_{suffix}"
            filename = _unique_filename(base_name, used_filenames)
            filepath = framework_dir / filename

            wc = write_corpus_file(filepath, batch_text, dry_run)
            stats["files_created"] += 1
            _categorize(wc, stats)

            if verbose:
                label = _label(wc)
                batch_info = f" (batch {i}/{len(batches)}, {len(batch)} controls)" if len(batches) > 1 else ""
                print(f"  {label} {cid}{batch_info} -> {filename} ({wc} words)")

    return stats


def _batch_controls(group: list, target_min: int, target_max: int) -> List[list]:
    """Split a group of controls into batches targeting word count range."""
    batches = []
    current_batch = []
    current_wc = 80  # header overhead

    for c in group:
        desc = c.get('description', '') or ''
        rat = c.get('rationale', '') or ''
        aud = c.get('audit', '') or c.get('audit_procedure', '') or ''
        rem = c.get('remediation', '') or c.get('remediation_steps', '') or ''
        wc = len((desc + rat + aud + rem).split())

        if current_wc + wc > target_max and current_batch:
            batches.append(current_batch)
            current_batch = [c]
            current_wc = 80 + wc
        else:
            current_batch.append(c)
            current_wc += wc

    if current_batch:
        batches.append(current_batch)

    return batches


def _unique_filename(base: str, used: set) -> str:
    """Generate a unique .txt filename."""
    # Truncate base to 60 chars
    if len(base) > 60:
        base = base[:60].rsplit('_', 1)[0]

    filename = f"{base}.txt"
    if filename not in used:
        used.add(filename)
        return filename

    # Append counter for uniqueness
    for n in range(2, 999):
        filename = f"{base}_{n}.txt"
        if filename not in used:
            used.add(filename)
            return filename

    return f"{base}_999.txt"


def _label(wc: int) -> str:
    """Get ASCII-safe label for word count."""
    if wc < TARGET_MIN:
        return "!! THIN"
    elif wc <= TARGET_MAX:
        return "OK"
    else:
        return "!! OVER"


def _categorize(wc: int, stats: dict):
    """Categorize word count into buckets."""
    stats["word_counts"].append(wc)
    if wc < TARGET_MIN:
        stats["under_target"] += 1
    elif wc <= TARGET_MAX:
        stats["in_target"] += 1
    else:
        stats["over_target"] += 1


def print_summary(all_stats: List[Dict[str, Any]]):
    """Print a summary of all processed files."""
    print(f"\n{'='*60}")
    print("CORPUS GENERATION SUMMARY")
    print(f"{'='*60}")

    total_files = 0
    total_skipped = 0

    for stats in all_stats:
        print(f"\n  {stats['source']} ({stats['framework']})")
        print(f"    Controls: {stats['total_controls']}")
        print(f"    Files created: {stats['files_created']}")
        print(f"    Skipped (empty): {stats['skipped_empty']}")
        print(f"    Word count distribution:")
        print(f"      Under {TARGET_MIN}: {stats['under_target']}")
        print(f"      {TARGET_MIN}-{TARGET_MAX} (target): {stats['in_target']}")
        print(f"      Over {TARGET_MAX}: {stats['over_target']}")
        total_files += stats['files_created']
        total_skipped += stats['skipped_empty']

    print(f"\n  TOTAL FILES CREATED: {total_files}")
    print(f"  TOTAL SKIPPED: {total_skipped}")
    print(f"{'='*60}")

    # Word count stats
    all_wc = []
    for stats in all_stats:
        all_wc.extend(stats['word_counts'])

    if all_wc:
        avg = sum(all_wc) / len(all_wc)
        sorted_wc = sorted(all_wc)
        print(f"\n  Word count stats:")
        print(f"    Min: {min(all_wc)}")
        print(f"    Max: {max(all_wc)}")
        print(f"    Avg: {avg:.0f}")
        print(f"    Median: {sorted_wc[len(sorted_wc)//2]}")
        in_range = sum(1 for w in all_wc if TARGET_MIN <= w <= TARGET_MAX)
        print(f"    In target range ({TARGET_MIN}-{TARGET_MAX}): {in_range}/{len(all_wc)} ({in_range/len(all_wc)*100:.0f}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Convert CIS benchmark JSON files to RAG corpus .txt files"
    )
    parser.add_argument(
        "--input-dir", type=Path, default=DEFAULT_INPUT_DIR,
        help=f"Directory containing CIS JSON files (default: {DEFAULT_INPUT_DIR})"
    )
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to write corpus files (default: {DEFAULT_OUTPUT_DIR})"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview what would be generated without writing files"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show per-control output"
    )
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"Error: No JSON files found in {input_dir}")
        sys.exit(1)

    print(f"Found {len(json_files)} CIS JSON file(s)")
    if args.dry_run:
        print("DRY RUN -- no files will be written\n")

    output_dir = Path(args.output_dir)
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    all_stats = []
    for json_file in json_files:
        stats = process_json_file(json_file, output_dir, args.dry_run, args.verbose)
        all_stats.append(stats)

    print_summary(all_stats)


if __name__ == "__main__":
    main()
