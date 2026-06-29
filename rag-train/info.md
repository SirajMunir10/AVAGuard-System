# RAG-Train Pipeline Updates & Status Summary

This document serves as a comprehensive summary of all architectural changes, file modifications, and new additions made to the `rag-train` project directory. 

Since `rag-train` was imported as a standalone subproject into the main AVA repository, this file documents exactly what was changed so that you can safely synchronize these updates back to the original GitHub repository.

---

## 1. Project Structure: Original vs. New

**Original Structure (Before our changes):**
The original `rag-train` folder was relatively barebones. It contained:
*   A basic `build_index.py` script for creating a FAISS vector database.
*   A basic `query_index.py` script for searching the index.
*   A small `corpus/` folder containing a few dozen loosely formatted text files (mostly penetration testing notes).
*   **Critical Flaw:** The original scripts contained hardcoded absolute paths specific to the original developer's PC (e.g., `C:\Users\UsamaMaqbool\OneDrive...`), making them unusable on other machines.

**New Structure:**
We consolidated all corpus generation, fine-tuning infrastructure, and API tooling into this single canonical pipeline. 
*   **`rag-train/ll-finetuning/`**: We imported the entire `ll-finetuning-main` project into here. It now acts as the engine for generating the massive dataset.
*   **`rag-train/ll-finetuning/rag/corpus/`**: The new canonical, centralized storage location for all generated `.txt` files.
*   **`rag-train/tools/`**: A new directory created for utility scripts.

---

## 2. File Changes & Modifications

Here is the exact list of files that were modified from the original codebase, and new files that were created:

### A. Modifications to Original `rag-train` Codebase
We made minimal but critical changes to the original developer's code to make it production-ready.

**1. `build_index.py`**
*   **Changes:** Removed the hardcoded `C:\Users\UsamaMaqbool\...` paths. Replaced them with relative Python `Path` resolutions (`Path(__file__).parent`).
*   **Purpose:** To make the script portable. Now, anyone pulling the repo can run the indexer regardless of their operating system or username.

**2. `query_index.py`**
*   **Changes:** Fixed the hardcoded paths (same as above). Additionally, modified the script so that it doesn't just return the *filename* of the matching document, but actually reads and returns the *text content* of the document.
*   **Purpose:** A RAG pipeline must feed text to an LLM, not just filenames. This modification makes the retrieval script actually usable for the final AVAGuard RAG architecture.

### B. Additions & Automation Scripts (New Code)

**3. `rag-train/ll-finetuning/scripts/cis_to_corpus.py`**
*   **Changes:** Completely rewritten to parse raw CIS Benchmark JSONs into human-readable `.txt` articles.
*   **Purpose:** To transform structured compliance data into flowing prose (Overview, Audit Steps, Remediation, Key Takeaways) so the RAG model can easily understand and synthesize it.

**4. `rag-train/ll-finetuning/scripts/generate_corpus.py`**
*   **Changes:** We built this from scratch to automate the DeepSeek API. During the latest session, we updated it to:
    *   Output exclusively to `.txt` (to match the CIS corpus).
    *   Iterate through subtopics individually rather than in one massive batch (to prevent DeepSeek token truncation).
    *   Include robust checkpointing (reading `corpus_generation_log.csv`) so that if the script stops, it skips already-generated files on restart.
    *   Track API tokens and project financial costs.
*   **Purpose:** To automatically generate a 10,000+ file RAG corpus covering SOC2, AWS, Azure, etc., in a highly resilient and cost-effective manner.

**5. `rag-train/ll-finetuning/config/topics.csv`**
*   **Changes:** Seeded with 59 technical domains and topics. We appended `bitbucket_security` to this list.
*   **Purpose:** Serves as the master manifest instructing the AI on what corpus files to generate.

**6. `rag-train/tools/corpus_status.py`**
*   **Changes:** Brand new utility script.
*   **Purpose:** Provides a real-time terminal summary of how many files have been generated, how many are pending, and estimated completion status.

---

## 3. Current Status & Next Steps

**Is the project in a working state?**
**Yes.** The corpus generation pipeline is 100% operational, robust, and actively running. The retrieval scripts (`build_index.py` and `query_index.py`) have been debugged and made portable. 

**Additional steps required to run it successfully:**
Right now, the corpus generation is running. Once it completes, the pipeline is ready for **Phase 2 (Indexing)**. 
1.  Run `python rag-train/build_index.py` to ingest the newly generated thousands of `.txt` files into the FAISS vector database.
2.  Test the retrieval using `python rag-train/query_index.py "How do I secure an Azure AD tenant?"`.

---

## 4. Repository Management & GitHub Syncing

**Can I safely copy the `rag-train` folder back to its original location and push it to the original GitHub repository?**
**Absolutely YES.**

Here is why it is safe and highly recommended to push these changes back to your team member's repository:
1.  **No Destructive Changes:** We did not delete the original indexing logic. We only fixed the fatal flaw (hardcoded paths) that prevented the code from running on your machine.
2.  **Massive Value Add:** You are pushing back a fully automated, resilient data-generation pipeline (`ll-finetuning` and `tools`) that the original repository desperately needed to build its corpus.
3.  **Self-Contained:** Because we used relative pathing (e.g., `Path(__file__).parent / "rag" / "corpus"`), your team member can pull your branch, and the scripts will immediately work on their machine without them having to change a single line of code.

**Summary for your GitHub Commit Message:**
> *"Refactored indexing scripts to use relative paths instead of hardcoded absolute paths. Integrated ll-finetuning pipeline to automate generation of a 10,000+ file RAG corpus via DeepSeek. Added progress tracking tools and standardized all corpus data to .txt format."*

---

## 5. Evidence-Driven Corpus Pipeline (Fine-Tuning JSONL)

The fine-tuning corpus is built using an evidence-extraction pipeline rather than free-form LLM generation.
Every entry must be traceable to an authoritative source (Microsoft Learn, CIS Benchmarks).

### Architecture

```
Authoritative URLs / CIS JSON  →  extract_scenarios.py  →  corpus_grounded.jsonl
Gap analysis                   →  generate_corpus.py     →  corpus_pending_review.jsonl
Human review                   →  promote_reviewed.py    →  corpus_grounded.jsonl
```

### Three-Command Workflow

**Step 1 — Audit existing corpus and identify gaps:**
```bash
python ll-finetuning/scripts/corpus_audit.py \
    --input ll-finetuning/data/ \
    --output ll-finetuning/data/gap_report.json
```

**Step 2 — Extract scenarios from authoritative documentation:**
```bash
python ll-finetuning/scripts/extract_scenarios.py \
    --seed-urls ll-finetuning/config/urls.txt \
    --output ll-finetuning/data/corpus_grounded.jsonl
```

**Step 3 — Check coverage matrix (repeat until all cells ≥ 5):**
```bash
python ll-finetuning/scripts/coverage_matrix.py \
    --input ll-finetuning/data/corpus_grounded.jsonl
```

### Additional Commands

**Gap-fill with LLM (generates entries for review — never auto-promoted):**
```bash
python ll-finetuning/scripts/generate_corpus.py \
    --mode jsonl-gap-fill \
    --gap-report ll-finetuning/data/gap_report.json \
    --max-entries-per-gap 10
```

**Review and promote pending entries:**
```bash
python ll-finetuning/scripts/promote_reviewed.py
```

### Data Files

| File | Purpose |
|---|---|
| `data/corpus_grounded.jsonl` | Training-ready entries with provenance. Only human-reviewed or extracted entries. |
| `data/corpus_pending_review.jsonl` | LLM-generated gap-fill entries awaiting human review. |
| `data/corpus_rejected.jsonl` | Rejected entries from promote_reviewed.py. Kept for audit. |
| `data/gap_report.json` | Output of corpus_audit.py. Drives gap-fill prioritisation. |
| `data/extraction_checkpoint.json` | Resume state for extract_scenarios.py. |
| `data/archived/` | Off-topic HTB/CTF data. Not part of the Microsoft cloud corpus. |

### Acceptance Criteria

The corpus is complete when:
- ≥ 95% of entries in `corpus_grounded.jsonl` have a populated `source_references` field
- 0 entries contain error codes not present in their cited source document
- Duplicate rate < 5% (Jaccard > 0.80 on `query` field)
- Coverage matrix shows ≥ 5 entries per domain × incident_type cell for the 6 primary domains
- All LLM-generated entries remain in `corpus_pending_review.jsonl` until manually promoted
- Total grounded corpus: 2,000–5,000 entries
