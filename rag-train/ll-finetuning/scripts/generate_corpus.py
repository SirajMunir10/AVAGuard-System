#!/usr/bin/env python3
"""
AVAGuard AI Corpus Generator

Reads topics.csv and generates technical knowledge articles using the DeepSeek API
(or other configured LLMs) via the MultiLLMClient.

Modes:
    articles (default): reads topics.csv, generates .txt knowledge articles for RAG
    jsonl-gap-fill:     reads gap_report.json, generates structured JSONL entries for
                        the fine-tuning corpus, writing to corpus_pending_review.jsonl
                        ONLY — never touches corpus_grounded.jsonl automatically.

Usage:
    python generate_corpus.py --dry-run
    python generate_corpus.py --provider deepseek
    python generate_corpus.py --domain azure_security --delay-ms 1000
    python generate_corpus.py --mode jsonl-gap-fill --gap-report data/gap_report.json
    python generate_corpus.py --mode jsonl-gap-fill --max-entries-per-gap 5 --dry-run
"""

import json
import os
import sys
import csv
import time
import re
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add parent directory to path to import synthetic_data_generator
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
sys.path.append(str(PARENT_DIR))

from synthetic_data_generator.api_clients import MultiLLMClient

# Setup basic logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("corpus_gen")

# Pricing at $0.14 per 1M input, $0.28 per 1M output for DeepSeek
DEEPSEEK_INPUT_COST = 0.14 / 1_000_000
DEEPSEEK_OUTPUT_COST = 0.28 / 1_000_000

# Defaults
DEFAULT_TOPICS = PARENT_DIR / "config" / "topics.csv"
DEFAULT_OUTPUT_DIR = PARENT_DIR / "rag" / "corpus"
DEFAULT_LOG_FILE = PARENT_DIR / "scripts" / "corpus_generation_log.csv"
DEFAULT_ERR_FILE = PARENT_DIR / "scripts" / "corpus_generation_errors.log"

# Gap-fill mode defaults
DEFAULT_GAP_REPORT  = PARENT_DIR / "data" / "gap_report.json"
# Gap-fill entries ALWAYS go to pending review — never to corpus_grounded.jsonl
PENDING_OUTPUT = PARENT_DIR / "data" / "corpus_pending_review.jsonl"

# ── Gap-Fill Prompt ────────────────────────────────────────────────────────────
# The LLM MUST populate the citation field with a specific Microsoft Learn page
# or CIS control number. Entries without a citation are discarded. This is the
# core quality gate that prevents the gap-fill mode from producing hallucinated,
# untraceable content — the same failure mode the original pipeline had.
# temperature=0.4: slightly higher than extraction (0.1) because we are generating
# a scenario in a domain that has a gap, but still low enough to stay grounded.
GAP_FILL_PROMPT = """You are a senior Microsoft cloud security architect filling coverage gaps in a training corpus.

Generate exactly ONE structured training scenario for the following gap:
  Domain:        {domain}
  Incident Type: {incident_type}

MANDATORY CITATION REQUIREMENT:
  You MUST state which specific Microsoft documentation page or CIS Benchmark control
  this scenario is drawn from. If you cannot name a real, specific source, output:
  {{"skip": true, "reason": "no reliable citation available"}}
  and nothing else.

  Do NOT generate a scenario if you are unsure of the source.
  Do NOT cite a generic URL like 'learn.microsoft.com' — you must cite the specific page.

STRICT RULES:
  - Include specific PowerShell/CLI commands only if they appear in official documentation
  - Include exact error codes only if they are documented by Microsoft or CIS
  - Do NOT invent error codes, symptoms, or remediation steps
  - All remediation_steps must reflect documented Microsoft guidance

Output ONLY a valid JSON object (not an array). No preamble, no markdown fences.

Schema:
{{
  "id": "",
  "domain": "{domain}",
  "subdomain": "",
  "incident_type": "{incident_type}",
  "query": "[scenario as a natural language question or problem statement]",
  "environment_context": {{"tenant_type": "", "relevant_config": ""}},
  "symptoms": [],
  "error_codes": [],
  "root_causes": [],
  "remediation_steps": [],
  "validation": "",
  "rollback": "",
  "citation": "[REQUIRED: exact Microsoft Learn page title and URL, or CIS control number]",
  "source_references": [],
  "provenance": "LLM-generated — requires human review before promotion",
  "completeness_score": 0,
  "generation_method": "llm_gap_fill"
}}
"""

GAP_FILL_SYSTEM_PROMPT = (
    "You are a senior Microsoft cloud security architect. "
    "You generate training scenarios grounded in official Microsoft documentation. "
    "You never invent technical details. "
    "If you cannot cite a specific real source, you output a skip signal."
)


SINGLE_FILE_PROMPT = """Write a 700-900 word technical knowledge article about: {topic}

Requirements:
- Factual and technically accurate for a security and compliance audience
- Structure: definition -> key components -> real-world application -> security relevance
- Use clear headings and bullet points where appropriate
- End with exactly 3 key takeaways under the heading "Key Takeaways"
- No marketing language, no filler sentences
- Every sentence must be directly useful to a security engineer

Output plain text only. Do not wrap the output in markdown code fences.
"""

SPLIT_PROMPT = """Write a 700-900 word technical knowledge article about this specific subtopic: {subtopic}
(Part of the broader topic: {topic})

Requirements:
- Factual and technically accurate for a security and compliance audience
- Structure: definition -> key components -> real-world application -> security relevance
- Use clear headings and bullet points where appropriate
- End with exactly 3 key takeaways under the heading "Key Takeaways"
- No marketing language, no filler sentences
- Every sentence must be directly useful to a security engineer
- Do not include any title or filename headers. Start directly with the content.

Output plain text only. Do not wrap the output in markdown code fences.
"""

# ── Gap-fill helper functions ─────────────────────────────────────────────────

def _score_entry_gap_fill(entry: Dict) -> int:
    """
    Score a gap-fill entry 0–10. Mirror of corpus_audit.py:score_entry().
    Duplicated here to avoid circular imports.
    """
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
    if entry.get("symptoms") and isinstance(entry["symptoms"], list) and len(entry["symptoms"]) > 0:
        score += 1
    ctx = entry.get("environment_context")
    if ctx and isinstance(ctx, dict) and any(v for v in ctx.values() if v):
        score += 1
    if isinstance(entry.get("validation"), str) and entry["validation"].strip():
        score += 1
    if isinstance(entry.get("rollback"), str) and entry["rollback"].strip():
        score += 1
    return score


def load_gap_report(path: Path) -> List[Dict]:
    """
    Read gap_report.json and return the gaps list sorted by count ascending
    so the most underrepresented domain × incident_type cells are filled first.

    Returns:
        List of gap dicts: [{"domain": str, "incident_type": str, "count": int}]
    """
    if not path.exists():
        logger.error(f"Gap report not found: {path}. Run corpus_audit.py first.")
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        gaps = data.get("gaps", [])
        # Sort by count ascending — fill the emptiest cells first
        gaps.sort(key=lambda g: g.get("count", 0))
        return gaps
    except (json.JSONDecodeError, KeyError) as exc:
        logger.error(f"Failed to parse gap report {path}: {exc}")
        return []


def generate_gap_entry(
    client: MultiLLMClient,
    domain: str,
    incident_type: str,
    provider: str,
    entry_index: int,
) -> Optional[Dict]:
    """
    Generate a single structured JSONL entry for a domain × incident_type gap.

    The LLM must populate the 'citation' field with a specific Microsoft Learn page
    or CIS control number. If citation is empty or the LLM signals skip, the entry
    is discarded with a logged warning — this is the quality gate that prevents
    hallucinated, untraceable content from entering the pending review file.

    temperature=0.4: lower than creative writing (0.7) to stay grounded in real
    Microsoft guidance, but higher than extraction (0.1) since we are generating
    a scenario rather than directly quoting a source.

    Returns:
        Validated entry dict, or None if citation absent / LLM signals skip.
    """
    prompt = GAP_FILL_PROMPT.format(domain=domain, incident_type=incident_type)
    response: Optional[str] = None

    # 3 retries with exponential backoff: 1s, 2s, 4s
    for attempt in range(3):
        try:
            response = client.call(
                provider,
                prompt,
                system_prompt=GAP_FILL_SYSTEM_PROMPT,
                temperature=0.4,
                max_tokens=2000,
            )
            if response:
                break
        except Exception as exc:
            wait = 2 ** attempt
            logger.warning(f"  LLM attempt {attempt + 1}/3 failed: {exc}. Retrying in {wait}s…")
            time.sleep(wait)

    if not response:
        logger.warning(f"  LLM returned no response for {domain} / {incident_type}")
        return None

    # Strip markdown fences
    response = response.strip()
    response = re.sub(r"^```(?:json)?\s*", "", response)
    response = re.sub(r"\s*```$", "", response)

    try:
        entry = json.loads(response)
    except json.JSONDecodeError as exc:
        logger.warning(f"  Malformed JSON from LLM ({domain}/{incident_type}): {exc}")
        return None

    # Check for LLM skip signal
    if entry.get("skip"):
        reason = entry.get("reason", "unspecified")
        logger.warning(f"  LLM signalled skip ({domain}/{incident_type}): {reason}")
        return None

    # MANDATORY: citation must be non-empty — discard otherwise
    citation = entry.get("citation", "").strip()
    if not citation:
        logger.warning(
            f"  Entry discarded — empty citation field for {domain}/{incident_type}. "
            f"LLM must cite a specific Microsoft doc page or CIS control."
        )
        return None

    # Populate source_references from citation if not already set
    if not entry.get("source_references"):
        entry["source_references"] = [citation]

    # Ensure required fields are present with correct types
    entry.setdefault("id", f"{re.sub(r'[^a-z0-9]+', '-', domain.lower())}-{re.sub(r'[^a-z0-9]+', '-', incident_type.lower())}-{entry_index:03d}")
    entry.setdefault("symptoms", [])
    entry.setdefault("error_codes", [])
    entry.setdefault("root_causes", [])
    entry.setdefault("remediation_steps", [])
    entry.setdefault("environment_context", {})
    entry.setdefault("validation", "")
    entry.setdefault("rollback", "")
    entry["generation_method"] = "llm_gap_fill"
    entry["provenance"] = "LLM-generated — requires human review before promotion"
    entry["completeness_score"] = _score_entry_gap_fill(entry)

    if not entry.get("query", "").strip():
        logger.warning(f"  Entry discarded — empty query field ({domain}/{incident_type})")
        return None

    return entry


def _append_jsonl(path: Path, entries: List[Dict]) -> None:
    """Append entries to a JSONL file; creates parent directories if needed."""
    if not entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def run_gap_fill_mode(args: Any, client: MultiLLMClient) -> None:
    """
    Gap-fill pipeline:
    1. Load gap_report.json, iterate gaps sorted by count ascending.
    2. For each gap cell, generate up to --max-entries-per-gap entries.
    3. Entries with valid citations → corpus_pending_review.jsonl.
    4. Entries without citations, or where LLM signals skip → discarded + logged.
    5. corpus_grounded.jsonl is NEVER touched by this function.

    All gap-fill entries carry:
      generation_method = "llm_gap_fill"
      provenance = "LLM-generated — requires human review before promotion"
    """
    gaps = load_gap_report(args.gap_report)
    if not gaps:
        logger.error("No gaps found in gap report. Exiting gap-fill mode.")
        return

    logger.info(f"Gap-fill mode: {len(gaps)} gap(s) to fill, max {args.max_entries_per_gap} entries each")
    logger.info(f"Output: {PENDING_OUTPUT} (pending review only — never grounded automatically)")

    total_generated = total_skipped = total_discarded = 0

    for gap in gaps:
        domain = gap["domain"]
        incident_type = gap["incident_type"]
        current_count = gap["count"]
        needed = max(0, 5 - current_count)  # 5 is GAP_THRESHOLD — fill to minimum
        to_generate = min(args.max_entries_per_gap, needed + 2)  # +2 buffer for discards

        logger.info(f"\n  Gap: {domain} / {incident_type} (current: {current_count}, generating: {to_generate})")

        gap_entries: List[Dict] = []
        for i in range(to_generate):
            if args.dry_run:
                logger.info(f"    [DRY RUN] Would generate entry {i + 1}/{to_generate} for {domain}/{incident_type}")
                continue

            entry = generate_gap_entry(client, domain, incident_type, args.provider, i + 1)
            if entry:
                gap_entries.append(entry)
                logger.info(f"    ✓ Entry {i + 1}: score={entry['completeness_score']}, citation={entry.get('citation', '')[:60]}")
            else:
                total_discarded += 1

        if not args.dry_run and gap_entries:
            _append_jsonl(PENDING_OUTPUT, gap_entries)
            total_generated += len(gap_entries)
            logger.info(f"  → Wrote {len(gap_entries)} entries to pending review")

    logger.info("\n" + "=" * 50)
    logger.info("GAP-FILL COMPLETE")
    logger.info("=" * 50)
    logger.info(f"  Generated → pending review:  {total_generated}")
    logger.info(f"  Discarded (no citation):     {total_discarded}")
    if not args.dry_run:
        logger.info(f"  Output file: {PENDING_OUTPUT}")
        logger.info("  Next step: run promote_reviewed.py to review and promote entries")


# ── Original article-mode helpers (unchanged) ──────────────────────────────────

def slugify_filename(text: str) -> str:
    """Ensure filename is safe and ends with .txt"""
    # Remove markdown code fences if present by accident
    text = text.replace("`", "")
    if not text.endswith(".txt"):
        text += ".txt"
    # Basic sanitize
    text = re.sub(r'[^a-zA-Z0-9_\-\.]', '', text)
    if len(text) > 60:
        text = text[:56] + ".txt"
    return text.lower()

def count_words(text: str) -> int:
    return len(text.split())

def validate_content(text: str, filename: str) -> bool:
    """Validate word count and structure."""
    words = count_words(text)
    if words < 600 or words > 1200:
        return False
    if "Key Takeaways" not in text:
        return False
    return True

def save_file(output_dir: Path, domain: str, filename: str, content: str, overwrite: bool) -> tuple[bool, str]:
    """Save the file, returning (success, final_path)."""
    domain_dir = output_dir / domain
    domain_dir.mkdir(parents=True, exist_ok=True)
    
    filepath = domain_dir / filename
    if filepath.exists() and not overwrite:
        return False, str(filepath)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    
    return True, str(filepath)

def log_result(log_path: Path, filename: str, wc: int, tokens: int, status: str):
    """Append a row to the generation log."""
    write_header = not log_path.exists()
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "filename", "word_count", "tokens_used", "status"])
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), filename, wc, tokens, status])

def log_error(err_path: Path, message: str):
    with open(err_path, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def process_single(client: MultiLLMClient, row: dict, args, provider: str) -> None:
    """Handle generation of a single file."""
    prompt = SINGLE_FILE_PROMPT.format(topic=row['topic'])
    
    if args.dry_run:
        logger.info(f"  [DRY RUN] Would generate single file for '{row['topic']}'")
        return

    logger.info(f"  Generating: {row['topic']}...")
    # System prompt forces strict factual tone
    sys_prompt = "You are a senior cybersecurity engineer writing internal documentation."
    response = client.call(provider, prompt, system_prompt=sys_prompt, temperature=0.3, max_tokens=2500)
    
    if not response:
        logger.error(f"  Failed to generate response for {row['topic']}")
        log_error(args.err_file, f"API Failure: {row['topic']}")
        return
        
    filename = slugify_filename(f"{row['output_filename_prefix']}.txt")
    wc = count_words(response)
    
    # Validation
    is_valid = validate_content(response, filename)
    if not is_valid:
        filename = filename.replace(".txt", "_NEEDS_REVIEW.txt")
        status = f"WARNING_WC_{wc}"
        logger.warning(f"  Warning: Output for {row['topic']} failed validation (Words: {wc}). Saved as NEEDS_REVIEW.")
    else:
        status = "SUCCESS"
        logger.info(f"  Success: {filename} ({wc} words)")

    saved, path = save_file(args.output_dir, row['domain'], filename, response, args.overwrite)
    
    # Retrieve tokens from client
    tokens_used = 0
    if hasattr(client, 'last_usage'):
        tokens_used = client.last_usage.get('completion_tokens', 0)
        args.total_prompt_tokens += client.last_usage.get('prompt_tokens', 0)
        args.total_completion_tokens += client.last_usage.get('completion_tokens', 0)
        
    if saved:
        log_result(args.log_file, filename, wc, tokens_used, status)
    else:
        logger.info(f"  Skipped (already exists): {filename}")

def process_split(client: MultiLLMClient, row: dict, args, provider: str) -> None:
    """Handle generation of multiple files by iterating through subtopics."""
    n = int(row['split_into_n_files'])
    subtopics = [s.strip() for s in row['subtopics'].split(',')]
    
    if args.dry_run:
        logger.info(f"  [DRY RUN] Would generate {len(subtopics)} files for '{row['topic']}'")
        return

    logger.info(f"  Generating {len(subtopics)} separate files for: {row['topic']}...")
    sys_prompt = "You are a senior cybersecurity engineer writing internal documentation."
    
    success_count = 0
    for idx, subtopic in enumerate(subtopics, 1):
        if not subtopic: continue
        
        prompt = SPLIT_PROMPT.format(
            topic=row['topic'],
            subtopic=subtopic
        )
            
        short_sub = slugify_filename(subtopic.replace(' ', '_'))
        short_sub = short_sub.replace('.txt', '')
        filename = slugify_filename(f"{row['output_filename_prefix']}_{short_sub}.txt")
        
        # Checkpoint: Skip if already in log and we are not overwriting
        if not args.overwrite and filename in args.logged_files:
            logger.info(f"      Skipped (found in log): {filename}")
            continue
            
        logger.info(f"    -> Subtopic {idx}/{len(subtopics)}: {subtopic}")
        response = client.call(provider, prompt, system_prompt=sys_prompt, temperature=0.3, max_tokens=2500)
        
        if not response:
            logger.error(f"      Failed to generate response for {subtopic}")
            log_error(args.err_file, f"API Failure: {row['topic']} -> {subtopic}")
            
            # MultiLLMClient returns None if auth/quota fails or all retries exhaust.
            # We skip the row but don't crash.
            continue
            
        content = response.strip()
        wc = count_words(content)
        
        is_valid = validate_content(content, filename)
        if not is_valid:
            filename = filename.replace(".txt", "_NEEDS_REVIEW.txt")
            status = f"WARNING_WC_{wc}"
        else:
            status = "SUCCESS"
            
        saved, path = save_file(args.output_dir, row['domain'], filename, content, args.overwrite)
        
        # Track tokens
        tokens_used = 0
        if hasattr(client, 'last_usage'):
            tokens_used = client.last_usage.get('completion_tokens', 0)
            args.total_prompt_tokens += client.last_usage.get('prompt_tokens', 0)
            args.total_completion_tokens += client.last_usage.get('completion_tokens', 0)
            
        if saved:
            log_result(args.log_file, filename, wc, tokens_used, status)
            # Update cache so we skip it later if needed
            args.logged_files.add(filename)
            success_count += 1
            if is_valid:
                logger.info(f"      Saved: {filename} ({wc} words, {tokens_used} tokens)")
            else:
                logger.warning(f"      Saved (Review needed): {filename} ({wc} words, {tokens_used} tokens)")
        else:
            logger.info(f"      Skipped (already exists): {filename}")
            
        time.sleep(args.delay_ms / 1000.0)

    if success_count < n:
        logger.warning(f"  Expected {n} files, but generated {success_count}.")

def main():
    parser = argparse.ArgumentParser(
        description="Generate corpus files using LLM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  articles (default)  Read topics.csv and generate .txt knowledge articles for RAG
  jsonl-gap-fill      Read gap_report.json and generate structured JSONL entries
                      for the fine-tuning corpus (pending review only)
"""
    )
    parser.add_argument("--topics", type=Path, default=DEFAULT_TOPICS, help="Path to topics.csv")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Output directory")
    parser.add_argument("--log-file", type=Path, default=DEFAULT_LOG_FILE, help="Log CSV file")
    parser.add_argument("--err-file", type=Path, default=DEFAULT_ERR_FILE, help="Error log file")
    parser.add_argument("--provider", type=str, default="deepseek", help="API provider to use (e.g., deepseek, gemini)")
    parser.add_argument("--domain", type=str, help="Only process this specific domain")
    parser.add_argument("--max-files", type=int, default=0, help="Maximum number of files to generate (0 for unlimited)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without generating")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--delay-ms", type=int, default=200, help="Delay between API calls in ms")
    # ── Gap-fill mode arguments ────────────────────────────────────────────────
    parser.add_argument(
        "--mode", type=str, default="articles",
        choices=["articles", "jsonl-gap-fill"],
        help="Generation mode (default: articles)",
    )
    parser.add_argument(
        "--gap-report", type=Path, default=DEFAULT_GAP_REPORT,
        help=f"Gap report JSON from corpus_audit.py (default: {DEFAULT_GAP_REPORT})",
    )
    parser.add_argument(
        "--max-entries-per-gap", type=int, default=10,
        help="Maximum entries to generate per gap cell in jsonl-gap-fill mode (default: 10)",
    )
    
    args = parser.parse_args()

    args.total_prompt_tokens = 0
    args.total_completion_tokens = 0
    args.logged_files = set()

    # Load existing log to skip completed files
    if args.log_file.exists():
        with open(args.log_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('status') == 'SUCCESS' or row.get('status', '').startswith('WARNING'):
                    args.logged_files.add(row.get('filename'))

    if not args.topics.exists():
        logger.error(f"Topics file not found: {args.topics}")
        sys.exit(1)

    logger.info("Initializing MultiLLMClient...")
    client = MultiLLMClient()
    available = client.get_initialized_providers()

    if not args.dry_run and not available:
        logger.error("No API providers successfully initialized. Check your .env file.")
        sys.exit(1)

    if not args.dry_run and args.provider not in available:
        logger.warning(f"Requested provider '{args.provider}' not initialized. Will attempt fallback to available providers: {available}")

    # ── Route to gap-fill mode if requested ───────────────────────────────────
    if args.mode == "jsonl-gap-fill":
        run_gap_fill_mode(args, client)
        return

    # ── Default: articles mode (original behaviour unchanged below) ───────────
    rows_to_process = []
    with open(args.topics, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if args.domain and row['domain'] != args.domain:
                continue
            rows_to_process.append(row)

    logger.info(f"Found {len(rows_to_process)} rows to process.")
    
    # Check current generated count
    def get_generated_count():
        if not args.log_file.exists(): return 0
        with open(args.log_file, 'r', encoding='utf-8') as f:
            return sum(1 for line in f) - 1 # minus header

    start_count = get_generated_count()
    
    for idx, row in enumerate(rows_to_process, 1):
        if args.max_files > 0 and (get_generated_count() - start_count) >= args.max_files:
            logger.info(f"\nReached max files limit ({args.max_files}). Stopping generation.")
            break
            
        logger.info(f"\n[{idx}/{len(rows_to_process)}] Processing domain: {row['domain']} | Topic: {row['topic']}")
        
        split_n = int(row.get('split_into_n_files', 1))
        
        if split_n <= 1:
            process_single(client, row, args, args.provider)
        else:
            process_split(client, row, args, args.provider)
            
        if not args.dry_run and idx < len(rows_to_process):
            time.sleep(args.delay_ms / 1000.0)

    logger.info("\n" + "="*50)
    logger.info("GENERATION RUN COMPLETE")
    logger.info("="*50)
    
    if not args.dry_run and (args.total_prompt_tokens > 0 or args.total_completion_tokens > 0):
        input_cost = args.total_prompt_tokens * DEEPSEEK_INPUT_COST
        output_cost = args.total_completion_tokens * DEEPSEEK_OUTPUT_COST
        total_cost = input_cost + output_cost
        
        logger.info(f"Tokens Used this run:")
        logger.info(f"  Prompt tokens:     {args.total_prompt_tokens:,}")
        logger.info(f"  Completion tokens: {args.total_completion_tokens:,}")
        logger.info(f"  Estimated Cost:    ${total_cost:.4f}")
        
        # Rough estimate for full run (assuming 10,000 files)
        # Average cost per file based on this run
        if get_generated_count() - start_count > 0:
            files_gen = get_generated_count() - start_count
            avg_cost = total_cost / files_gen
            proj_10k = avg_cost * 10000
            logger.info(f"\nProjection:")
            logger.info(f"  Average cost per file: ~${avg_cost:.4f}")
            logger.info(f"  Projected cost for 10,000 files: ~${proj_10k:.2f}")

if __name__ == "__main__":
    main()
