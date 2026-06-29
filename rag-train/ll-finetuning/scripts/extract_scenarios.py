#!/usr/bin/env python3
"""
AVAGuard Evidence Extraction Pipeline

Fetches authoritative Microsoft documentation and CIS benchmark content,
then uses an LLM (in extraction — not generation — mode) to produce structured
JSONL training scenarios with full provenance.

Pipeline: URL → fetch → chunk → extract → score → deduplicate → JSONL corpus

Usage:
    python extract_scenarios.py --dry-run --max-urls 2
    python extract_scenarios.py --seed-urls config/urls.txt
    python extract_scenarios.py --provider gemini --max-urls 20
"""

import json
import time
import re
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

# ── Path bootstrap ─────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PARENT_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(PARENT_DIR))

from synthetic_data_generator.api_clients import MultiLLMClient  # noqa: E402

# ── Output paths ───────────────────────────────────────────────────────────────
GROUNDED_OUTPUT = PARENT_DIR / "data" / "corpus_grounded.jsonl"
PENDING_OUTPUT  = PARENT_DIR / "data" / "corpus_pending_review.jsonl"
CHECKPOINT_FILE = PARENT_DIR / "data" / "extraction_checkpoint.json"

# ── Quality thresholds ─────────────────────────────────────────────────────────
# ≥7: complete entry — written directly to grounded corpus
# 5–6: partial content — routed to pending review for auto_promote gate
# 3–4: some content but requires human review before training use
# <3: stub / nav content — discard silently
GROUNDED_MIN_SCORE = 7
PENDING_MIN_SCORE  = 3

# Jaccard deduplication threshold.
# 0.80: lower → duplicates survive across similar troubleshooting pages on the
# same product. Higher → paraphrased near-duplicates from different doc versions
# slip through. 0.80 balances both failure modes empirically.
SIMILARITY_THRESHOLD = 0.80

# Max characters per LLM chunk.
# 3000 chars ≈ 700–800 tokens; fits standard context windows while providing
# enough content per call to extract meaningful scenarios.
CHUNK_MAX_CHARS = 3000

# Min chars for a chunk to be worth sending to the LLM.
# 100 chars: avoids sending navigation link stubs and single-heading fragments.
CHUNK_MIN_CHARS = 100

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

# ── Default seed URL list ──────────────────────────────────────────────────────
DEFAULT_SEED_URLS: List[str] = [
    # Intune — Enrollment
    "https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors",
    "https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune",
    # Intune — Autopilot
    "https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe",
    "https://learn.microsoft.com/en-us/autopilot/troubleshoot-autopilot-device-preparation",
    # Entra ID
    "https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access",
    "https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors",
    "https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-troubleshoot",
    "https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr",
    # Defender for Endpoint
    "https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding",
    "https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus",
    "https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-asr",
    # Sentinel
    "https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-common-issues",
    "https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources",
    # Exchange Online
    "https://learn.microsoft.com/en-us/exchange/troubleshoot/outlook-connectivity/outlook-connection-issues",
    "https://learn.microsoft.com/en-us/exchange/troubleshoot/move-mailboxes/troubleshoot-migration-issues-in-exchange-server-hybrid-environment",
    # Azure
    "https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues",
]

# ── LLM extraction prompt (verbatim — do not modify wording) ──────────────────
EXTRACTION_PROMPT = """You are a senior cloud security architect extracting training scenarios from official Microsoft documentation and CIS benchmark guides.

Given the following documentation excerpt, extract any troubleshooting workflows, implementation procedures, hardening steps, or remediation procedures as structured training scenarios.

STRICT RULES:
- Include exact error codes, event IDs, or log entries ONLY if they appear verbatim in the source text
- Include specific PowerShell commands or CLI steps ONLY if present word-for-word in the source
- Do NOT invent, infer, or assume any technical details not explicitly stated
- Do NOT add error codes you believe should be there — only what the source says
- If a field cannot be populated from the source, leave it as an empty array or empty string
- Set provenance to the exact source URL
- Prioritize: Azure/Entra ID context, PowerShell remediation steps, exact error codes, CIS control mappings

Output ONLY a valid JSON array. No preamble, no explanation, no markdown fences.

Schema for each object:
{{
  "id": "source-slug-NNN",
  "domain": "one of: Intune, Entra ID, Defender, Sentinel, Exchange Online, Azure, Purview, Governance",
  "subdomain": "specific product area",
  "incident_type": "one of: Troubleshooting, Implementation, Hardening, Incident Response, Governance, Optimization",
  "query": "the scenario as a natural language question or problem statement",
  "environment_context": {{"tenant_type": "", "relevant_config": ""}},
  "symptoms": [],
  "error_codes": [],
  "root_causes": [],
  "remediation_steps": [],
  "validation": "",
  "rollback": "",
  "source_references": ["{url}"],
  "provenance": "Extracted from: {url}",
  "completeness_score": 0,
  "generation_method": "extracted"
}}

Source URL: {url}
Documentation excerpt:
{chunk}"""

EXTRACTION_SYSTEM_PROMPT = (
    "You are a senior Microsoft cloud security architect. "
    "You extract structured training scenarios from official documentation. "
    "You never invent technical details. You output only valid JSON arrays."
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("extractor")


# ── Entry scoring (mirrors corpus_audit.py — kept in sync manually) ────────────
def score_entry(entry: Dict) -> int:
    """
    Score 0–10. See corpus_audit.py:score_entry() for full weight rationale.
    Duplicated here to avoid circular imports between scripts.
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


# ── Jaccard similarity ─────────────────────────────────────────────────────────
def jaccard_similarity(text1: str, text2: str) -> float:
    """
    Compute Jaccard similarity on whitespace-tokenized text.
    Used to detect near-duplicate entries across similar doc pages.
    Returns 0.0 if either string is empty or produces an empty token set.
    """
    if not text1 or not text2:
        return 0.0
    t1 = set(text1.lower().split())
    t2 = set(text2.lower().split())
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)


def is_duplicate(entry: Dict, existing_queries: List[str]) -> bool:
    """
    Return True if any existing query has Jaccard ≥ SIMILARITY_THRESHOLD
    with this entry's query. Checks both the existing corpus and within-URL
    entries accumulated during the current run.
    """
    query = entry.get("query", "")
    if not query:
        return False
    return any(jaccard_similarity(query, q) >= SIMILARITY_THRESHOLD for q in existing_queries)


# ── Robots.txt compliance ──────────────────────────────────────────────────────
_robots_cache: Dict[str, RobotFileParser] = {}


def can_fetch(url: str) -> bool:
    """
    Check robots.txt before fetching. Cached per domain to avoid redundant
    requests. Returns True if robots.txt is unreachable (benefit of the doubt).
    """
    try:
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        if base not in _robots_cache:
            rp = RobotFileParser()
            rp.set_url(f"{base}/robots.txt")
            rp.read()
            _robots_cache[base] = rp
        return _robots_cache[base].can_fetch("*", url)
    except Exception:
        return True  # unreachable robots.txt → proceed


# ── URL fetching ───────────────────────────────────────────────────────────────
def fetch_url(url: str) -> Optional[str]:
    """
    Fetch URL with robots.txt compliance and exponential backoff retries.

    Retry schedule: attempt 0 → 1s, attempt 1 → 2s, attempt 2 → 4s.
    Returns raw HTML string, or None if all retries fail.
    """
    try:
        import requests
    except ImportError:
        logger.error("'requests' not installed. Run: pip install requests")
        return None

    if not can_fetch(url):
        logger.warning(f"robots.txt disallows: {url}")
        return None

    headers = {
        "User-Agent": (
            "AVAGuard-CorpusBuilder/1.0 "
            "(evidence extraction for Microsoft cloud AI training; respects robots.txt)"
        ),
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }

    for attempt in range(3):
        try:
            import requests as req
            resp = req.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            wait = 2 ** attempt  # 1s, 2s, 4s
            if attempt < 2:
                logger.warning(f"Fetch attempt {attempt + 1}/3 failed ({url}): {e}. Retrying in {wait}s…")
                time.sleep(wait)
            else:
                logger.error(f"All fetch attempts failed: {url} — {e}")

    return None


# ── Content chunking ───────────────────────────────────────────────────────────
def chunk_content(html: str, url: str) -> List[str]:
    """
    Split HTML into text chunks suitable for LLM extraction.

    Strategy:
    1. Parse with BeautifulSoup (lxml primary, html5lib fallback).
    2. Strip boilerplate: nav, header, footer, script, style, aside.
    3. Locate main content area (<main> or <article>).
    4. Walk descendants; split into sections at <h2>/<h3> boundaries.
    5. Sections exceeding CHUNK_MAX_CHARS split at sentence boundaries ('. ').
    6. Drop chunks shorter than CHUNK_MIN_CHARS (navigation stubs).

    Returns:
        List of text chunk strings ready for EXTRACTION_PROMPT.
    """
    soup = None
    for parser in ("lxml", "html5lib"):
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, parser)
            break
        except Exception as exc:
            logger.warning(f"HTML parser '{parser}' failed for {url}: {exc}")

    if soup is None:
        logger.error(f"All HTML parsers failed for {url} — skipping")
        return []

    # Strip boilerplate that adds noise without documentation content
    for tag in soup(["nav", "header", "footer", "script", "style", "aside"]):
        tag.decompose()
    for cls in [".breadcrumb", ".feedback", ".ms-docsnotification", ".doc-outline"]:
        for el in soup.select(cls):
            el.decompose()

    main = soup.find("main") or soup.find("article") or soup.body or soup

    # Walk descendants, splitting into sections at heading boundaries
    sections: List[str] = []
    current_parts: List[str] = []

    def _flush():
        if current_parts:
            sections.append(" ".join(current_parts).strip())
            current_parts.clear()

    if main:
        for element in main.descendants:
            if not hasattr(element, "name") or element.name is None:
                continue
            if element.name in ("h2", "h3"):
                _flush()
                heading = element.get_text(separator=" ", strip=True)
                if heading:
                    current_parts.append(heading)
            elif element.name in ("p", "li", "code", "pre", "td", "dd"):
                text = element.get_text(separator=" ", strip=True)
                if text and len(text) > 10:  # skip single words / nav links
                    current_parts.append(text)
    _flush()

    # Split any section that exceeds CHUNK_MAX_CHARS at sentence boundaries.
    # Splitting on '. ' avoids mid-sentence truncation; not perfect for all
    # abbreviations but adequate for technical documentation prose.
    chunks: List[str] = []
    for section in sections:
        if not section.strip():
            continue
        if len(section) <= CHUNK_MAX_CHARS:
            chunks.append(section)
        else:
            sentences = re.split(r"(?<=[.!?])\s+", section)
            current_chunk: List[str] = []
            current_len = 0
            for sentence in sentences:
                if current_len + len(sentence) > CHUNK_MAX_CHARS and current_chunk:
                    chunks.append(" ".join(current_chunk))
                    current_chunk = [sentence]
                    current_len = len(sentence)
                else:
                    current_chunk.append(sentence)
                    current_len += len(sentence) + 1
            if current_chunk:
                chunks.append(" ".join(current_chunk))

    # Filter chunks too short to contain extractable scenarios
    return [c for c in chunks if len(c) >= CHUNK_MIN_CHARS]


# ── Entry ID generation ────────────────────────────────────────────────────────
def generate_entry_id(url: str, index: int) -> str:
    """
    Generate a stable, human-readable entry ID from the URL path and chunk index.
    Uses the last 40 chars of the URL path slug (most specific part).
    """
    slug = re.sub(r"[^a-z0-9]+", "-", urlparse(url).path.lower()).strip("-")
    slug = slug[-40:] if len(slug) > 40 else slug
    return f"{slug}-{index:03d}"


# ── LLM extraction ─────────────────────────────────────────────────────────────
def extract_from_chunk(
    client: MultiLLMClient,
    chunk: str,
    url: str,
    provider: str,
    chunk_index: int,
) -> List[Dict]:
    """
    Send one documentation chunk to the LLM for structured extraction.

    Uses the verbatim EXTRACTION_PROMPT. Temperature = 0.1: very low because
    this is extraction from a source, not creative generation — we want the
    model to stay as close to the source text as possible.

    Retries: 3 attempts with 1s, 2s, 4s backoff.
    Strips markdown code fences from response (some models add them despite instructions).
    Validates JSON structure; skips entries with empty query fields.

    Returns:
        List of scored, validated entry dicts.
    """
    prompt = EXTRACTION_PROMPT.format(url=url, chunk=chunk)
    response: Optional[str] = None

    for attempt in range(3):
        try:
            response = client.call(
                provider,
                prompt,
                system_prompt=EXTRACTION_SYSTEM_PROMPT,
                temperature=0.1,   # extraction, not generation — minimise creativity
                max_tokens=4000,
            )
            if response:
                break
        except Exception as exc:
            wait = 2 ** attempt
            logger.warning(f"LLM attempt {attempt + 1}/3 failed (chunk {chunk_index}): {exc}. Retrying in {wait}s…")
            time.sleep(wait)

    if not response:
        logger.warning(f"LLM extraction failed for chunk {chunk_index} from {url}")
        return []

    # Strip markdown fences in case the model wraps output despite instructions
    response = response.strip()
    response = re.sub(r"^```(?:json)?\s*", "", response)
    response = re.sub(r"\s*```$", "", response)

    try:
        entries = json.loads(response)
        if isinstance(entries, dict):
            entries = [entries]
        if not isinstance(entries, list):
            logger.warning(f"Unexpected LLM output type {type(entries)} for chunk {chunk_index}")
            return []
    except json.JSONDecodeError as exc:
        logger.warning(f"Malformed JSON from LLM (chunk {chunk_index}, {url}): {exc}")
        return []

    validated: List[Dict] = []
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue

        # Normalize domain
        raw_domain = entry.get("domain", "")
        if raw_domain in DOMAIN_ALIASES:
            entry["domain"] = DOMAIN_ALIASES[raw_domain]

        # Ensure required fields exist with correct default types
        entry.setdefault("source_references", [url])
        entry.setdefault("provenance", f"Extracted from: {url}")
        entry.setdefault("generation_method", "extracted")
        entry.setdefault("symptoms", [])
        entry.setdefault("error_codes", [])
        entry.setdefault("root_causes", [])
        entry.setdefault("remediation_steps", [])
        entry.setdefault("environment_context", {})
        entry.setdefault("validation", "")
        entry.setdefault("rollback", "")
        entry.setdefault("query", "")

        # Generate stable ID (always overwrite what LLM provides to ensure uniqueness)
        entry["id"] = generate_entry_id(url, chunk_index * 100 + i)

        # Score the entry for downstream routing
        entry["completeness_score"] = score_entry(entry)

        # Discard entries with no query — unusable for retrieval at inference time
        if not entry.get("query", "").strip():
            continue

        validated.append(entry)

    return validated


# ── Checkpoint management ──────────────────────────────────────────────────────
def load_checkpoint(path: Path) -> Set[str]:
    """Load the set of already-processed URLs from checkpoint file."""
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return set(data.get("processed_urls", []))
        except Exception:
            return set()
    return set()


def save_checkpoint(path: Path, processed_urls: Set[str]) -> None:
    """Persist the set of processed URLs so restarts skip completed work."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"processed_urls": sorted(processed_urls)}, indent=2),
        encoding="utf-8",
    )


# ── Existing query loading ─────────────────────────────────────────────────────
def load_existing_queries(output_path: Path) -> List[str]:
    """Load all query strings from existing grounded corpus for deduplication."""
    if not output_path.exists():
        return []
    queries: List[str] = []
    for line in output_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            q = entry.get("query", "")
            if q:
                queries.append(q)
        except json.JSONDecodeError:
            pass
    return queries


def append_entries(path: Path, entries: List[Dict]) -> None:
    """Append entries to a JSONL file; creates parent directories if needed."""
    if not entries:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── Single-URL pipeline ────────────────────────────────────────────────────────
def process_url(
    url: str,
    client: MultiLLMClient,
    provider: str,
    existing_queries: List[str],
    dry_run: bool = False,
) -> Tuple[List[Dict], List[Dict]]:
    """
    Full pipeline for one URL: fetch → chunk → extract → score → deduplicate.

    Maintains a local copy of existing_queries so within-URL deduplication
    also applies (prevents two near-identical entries from the same page).

    Args:
        url: Documentation URL to process
        client: Initialized MultiLLMClient
        provider: Primary LLM provider name
        existing_queries: All existing query strings for deduplication
        dry_run: If True, print decisions but write nothing

    Returns:
        (grounded_entries, pending_entries) — both lists contain non-duplicates only
    """
    logger.info(f"Fetching: {url}")
    html = fetch_url(url)
    if not html:
        return [], []

    chunks = chunk_content(html, url)
    logger.info(f"  → {len(chunks)} chunk(s) to process")

    grounded: List[Dict] = []
    pending: List[Dict] = []
    # Local copy to track deduplication within this URL's chunks too
    local_queries = list(existing_queries)

    for i, chunk in enumerate(chunks, 1):
        logger.info(f"  Chunk {i}/{len(chunks)} ({len(chunk)} chars)…")
        try:
            entries = extract_from_chunk(client, chunk, url, provider, i)
        except Exception as exc:
            logger.error(f"  Chunk {i} extraction error: {exc} — skipping")
            continue

        for entry in entries:
            score = entry.get("completeness_score", 0)
            query = entry.get("query", "")

            if is_duplicate(entry, local_queries):
                logger.debug(f"  Duplicate skipped: {query[:60]}…")
                continue

            if dry_run:
                if score >= GROUNDED_MIN_SCORE:
                    label = "GROUNDED"
                elif score >= PENDING_MIN_SCORE:
                    label = "PENDING"
                else:
                    label = "DISCARD"
                print(f"  [{label} score={score}] {query[:80]}")
                if score >= PENDING_MIN_SCORE:
                    local_queries.append(query)
                continue

            if score >= GROUNDED_MIN_SCORE:
                grounded.append(entry)
                local_queries.append(query)
            elif score >= PENDING_MIN_SCORE:
                pending.append(entry)
                local_queries.append(query)
            else:
                logger.debug(f"  Score {score} < {PENDING_MIN_SCORE} — discarding")

    logger.info(f"  → Grounded: {len(grounded)}, Pending: {len(pending)}")
    return grounded, pending


# ── Main ───────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract structured training scenarios from authoritative Microsoft documentation"
    )
    parser.add_argument(
        "--seed-urls", type=Path,
        help="Text file with one URL per line. Uses built-in seed list if not provided.",
    )
    parser.add_argument(
        "--output", type=Path, default=GROUNDED_OUTPUT,
        help=f"Output path for grounded corpus (default: {GROUNDED_OUTPUT})",
    )
    parser.add_argument(
        "--pending", type=Path, default=PENDING_OUTPUT,
        help=f"Output path for pending review corpus (default: {PENDING_OUTPUT})",
    )
    parser.add_argument(
        "--provider", type=str, default="deepseek",
        help="Primary LLM provider (default: deepseek). MultiLLMClient handles fallback.",
    )
    parser.add_argument(
        "--max-urls", type=int, default=0,
        help="Maximum URLs to process (0 = all)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Fetch and parse without writing any files. Prints decisions to stdout.",
    )
    parser.add_argument(
        "--checkpoint", type=Path, default=CHECKPOINT_FILE,
        help=f"Checkpoint file (default: {CHECKPOINT_FILE})",
    )
    args = parser.parse_args()

    # Load URL list
    if args.seed_urls and args.seed_urls.exists():
        urls = [
            l.strip()
            for l in args.seed_urls.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")
        ]
        logger.info(f"Loaded {len(urls)} URLs from {args.seed_urls}")
    else:
        urls = DEFAULT_SEED_URLS
        logger.info(f"Using built-in seed list ({len(urls)} URLs)")

    if args.max_urls > 0:
        urls = urls[: args.max_urls]
        logger.info(f"Limiting to {args.max_urls} URL(s)")

    logger.info(f"Provider: {args.provider} | Dry-run: {args.dry_run}")

    # Initialise LLM client
    client = MultiLLMClient()
    available = client.get_initialized_providers()
    if not args.dry_run and not available:
        logger.error("No LLM providers initialised. Check your config/.env file.")
        sys.exit(1)

    # Load resume state
    processed_urls = load_checkpoint(args.checkpoint)
    existing_queries = load_existing_queries(args.output)
    logger.info(f"Checkpoint: {len(processed_urls)} URLs already processed")
    logger.info(f"Existing corpus: {len(existing_queries)} queries loaded for dedup")

    total_grounded = total_pending = 0

    for url in urls:
        if url in processed_urls:
            logger.info(f"Skipping (checkpointed): {url}")
            continue

        try:
            grounded, pending = process_url(
                url, client, args.provider, existing_queries, args.dry_run
            )

            if not args.dry_run:
                append_entries(args.output, grounded)
                append_entries(args.pending, pending)
                processed_urls.add(url)
                save_checkpoint(args.checkpoint, processed_urls)
                # Extend dedup list with newly written queries
                existing_queries.extend(e.get("query", "") for e in grounded + pending if e.get("query"))

            total_grounded += len(grounded)
            total_pending += len(pending)

        except Exception as exc:
            # Never crash the pipeline — log and continue to next URL
            logger.error(f"Unexpected error processing {url}: {exc}")

        # Mandatory delay between URL fetches to be polite to origin servers
        time.sleep(1)

    logger.info("=" * 60)
    logger.info(f"Run complete — Grounded: {total_grounded} | Pending: {total_pending}")
    if args.dry_run:
        logger.info("DRY RUN — no files written.")
    else:
        logger.info(f"Grounded corpus: {args.output}")
        logger.info(f"Pending review:  {args.pending}")


if __name__ == "__main__":
    main()
