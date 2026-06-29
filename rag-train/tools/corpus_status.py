#!/usr/bin/env python3
"""
Corpus Status Tracker

Reports on the progress of the RAG corpus generation by comparing
the generated files against the topics.csv manifest.
"""

import csv
import os
from pathlib import Path
from collections import defaultdict

def main():
    script_dir = Path(__file__).resolve().parent
    base_dir = script_dir.parent / "ll-finetuning"
    topics_file = base_dir / "config" / "topics.csv"
    corpus_dir = base_dir / "rag" / "corpus"
    
    if not topics_file.exists():
        print(f"Error: {topics_file} not found.")
        return

    # Count generated files
    domain_counts = defaultdict(int)
    total_files = 0
    generated_prefixes = set()
    
    if corpus_dir.exists():
        for file_path in corpus_dir.rglob("*.txt"):
            domain = file_path.parent.name
            domain_counts[domain] += 1
            total_files += 1
            # Try to extract the topic prefix (e.g. azure_security_01_entra_id)
            # The filenames are like: domain_XX_topic_subtopic.txt
            # Let's just track by exact domain to simplify, or better, we can read the log.
            # But the requirement asks which topic rows are "done".
            # A row is "done" if we see files matching its output_filename_prefix.
            
    # Read log file to get exact matching if available, or just check prefixes
    # We will check if any file starts with the prefix.
    # To be accurate about "done", we should count if all N files are generated.
    # But a simple way is: if prefix exists in any filename, it's at least started.
    generated_filenames = []
    if corpus_dir.exists():
        generated_filenames = [f.name for f in corpus_dir.rglob("*.txt")]

    total_rows = 0
    completed_rows = 0
    pending_rows = 0
    estimated_remaining = 0
    
    row_status = []

    with open(topics_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rows += 1
            prefix = row['output_filename_prefix']
            n = int(row['split_into_n_files'])
            
            # Count how many files start with this prefix
            matched_files = [fn for fn in generated_filenames if fn.startswith(prefix)]
            
            if len(matched_files) >= n:
                status = "Done"
                completed_rows += 1
            elif len(matched_files) > 0:
                status = f"Partial ({len(matched_files)}/{n})"
                estimated_remaining += (n - len(matched_files))
            else:
                status = "Pending"
                pending_rows += 1
                estimated_remaining += n
                
            row_status.append({
                'domain': row['domain'],
                'topic': row['topic'],
                'status': status,
                'expected': n,
                'found': len(matched_files)
            })

    print("=" * 60)
    print("CORPUS GENERATION STATUS")
    print("=" * 60)
    print("\n[ Domain Folders ]")
    if not domain_counts:
        print("  No files generated yet.")
    else:
        for domain, count in sorted(domain_counts.items()):
            print(f"  {domain:<25} : {count} files")
    
    print("-" * 60)
    print(f"Total files generated across all domains: {total_files}")
    
    print("\n[ Topics Progress ]")
    print(f"  Total topic rows in CSV : {total_rows}")
    print(f"  Fully completed rows    : {completed_rows}")
    print(f"  Pending/Partial rows    : {total_rows - completed_rows}")
    print(f"  Est. files remaining    : ~{estimated_remaining}")
    
    print("\n[ Detailed Topic Status ]")
    print(f"  {'Domain':<20} | {'Topic':<25} | {'Status':<15}")
    print("  " + "-"*65)
    for r in row_status:
        # Highlight partial or done
        print(f"  {r['domain']:<20} | {r['topic']:<25} | {r['status']:<15}")
        
    print("=" * 60)

if __name__ == "__main__":
    main()
