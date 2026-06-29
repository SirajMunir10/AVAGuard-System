"""
AVAGuard RAG — Build FAISS Index from Corpus Files

Reads all .txt and .md files from the corpus directory, chunks them,
generates embeddings using sentence-transformers, and builds a FAISS
index for semantic search.

Supports:
  - Configurable chunk size and overlap
  - BGE model query prefix detection
  - Per-chunk metadata with framework/category inference
  - Force rebuild flag

Usage:
    python build_index.py
    python build_index.py --model BAAI/bge-base-en-v1.5 --chunk-size 512 --chunk-overlap 64
    python build_index.py --force-rebuild
"""

import os
import sys
import argparse
import pickle
import json
import re
from pathlib import Path
from datetime import datetime, timezone

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# === Defaults (relative to this script's location) ===
SCRIPT_DIR = Path(__file__).parent
DEFAULT_CORPUS_DIR = SCRIPT_DIR / "corpus"
DEFAULT_INDEX_DIR = SCRIPT_DIR / "faiss_index"
DEFAULT_MODEL = "BAAI/bge-base-en-v1.5"
DEFAULT_CHUNK_SIZE = 512   # words
DEFAULT_CHUNK_OVERLAP = 64  # words

# Framework inference mapping from directory names
FRAMEWORK_MAP = {
    'cis_benchmarks': 'CIS',
    'nist_frameworks': 'NIST',
    'azure_security': 'Azure Security',
    'aws_security': 'AWS Security',
    'gcp_security': 'GCP Security',
    'compliance_general': 'Compliance General',
    'mitre_attack': 'MITRE ATT&CK',
    'windows_security': 'Windows Security',
    'linux_security': 'Linux Security',
    'application_security': 'Application Security',
    'network_security': 'Network Security',
    'incident_response': 'Incident Response',
    'siem_platforms': 'SIEM Platforms',
    'vulnerability_management': 'Vulnerability Management',
    'malware_analysis': 'Malware Analysis',
    'emerging_tech': 'Emerging Technology',
}


def chunk_text(text: str, chunk_size: int = 512, overlap: int = 64) -> list:
    """
    Split text into overlapping chunks by word count.

    Args:
        text: The full document text.
        chunk_size: Maximum words per chunk.
        overlap: Number of overlapping words between adjacent chunks.

    Returns:
        List of chunk strings.
    """
    words = text.split()
    if len(words) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def infer_framework_category(relative_path: str) -> tuple:
    """
    Infer framework and category from file's directory structure.

    Example:
        'cis_benchmarks/intune_win11/file.txt' -> ('CIS', 'intune_win11')
        'azure_security/file.txt' -> ('Azure Security', '')
        'file.txt' -> ('General', '')
    """
    parts = Path(relative_path).parts

    if len(parts) == 1:
        # Root-level file
        return ('General', '')
    elif len(parts) == 2:
        # One level deep: framework/file.txt
        framework_dir = parts[0]
        framework = FRAMEWORK_MAP.get(framework_dir, framework_dir.replace('_', ' ').title())
        return (framework, '')
    else:
        # Two+ levels deep: framework/category/file.txt
        framework_dir = parts[0]
        category = parts[1]
        framework = FRAMEWORK_MAP.get(framework_dir, framework_dir.replace('_', ' ').title())
        return (framework, category)


import hashlib
from rank_bm25 import BM25Okapi

def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def build_index(corpus_dir: Path, index_dir: Path, model_name: str,
                chunk_size: int, chunk_overlap: int, force_rebuild: bool = False,
                incremental: bool = False):
    """Build a FAISS index from all text files in the corpus directory."""

    corpus_dir = Path(corpus_dir)
    index_dir = Path(index_dir)

    if not corpus_dir.exists():
        print(f"Error: Corpus directory not found: {corpus_dir}")
        sys.exit(1)

    index_path = index_dir / "faiss.index"
    meta_path = index_dir / "meta.pkl"
    cache_path = index_dir / "incremental_cache.pkl"
    bm25_path = index_dir / "bm25.pkl"

    if index_path.exists() and not force_rebuild and not incremental:
        print(f"Warning: Index already exists at {index_path}")
        print("Use --force-rebuild to overwrite or --incremental to update incrementally.")
        confirm = input("Proceed anyway? [y/N]: ").strip().lower()
        if confirm != 'y':
            print("Aborted.")
            sys.exit(0)

    # Collect all text files (recursively — supports subdirectories)
    extensions = {".txt", ".md"}
    files = sorted([
        f for f in corpus_dir.rglob("*")
        if f.suffix.lower() in extensions and f.stat().st_size > 0
    ])

    if not files:
        print(f"Error: No .txt or .md files found in {corpus_dir}")
        sys.exit(1)

    print(f"Found {len(files)} corpus files in {corpus_dir}")

    # Load incremental cache if requested and exists
    cache = {}
    if incremental and cache_path.exists() and index_path.exists() and meta_path.exists():
        try:
            with open(cache_path, "rb") as f:
                cache_data = pickle.load(f)
            # Verify cache compatibility
            if cache_data.get("model_name") == model_name and \
               cache_data.get("chunk_size") == chunk_size and \
               cache_data.get("chunk_overlap") == chunk_overlap:
                cache = cache_data.get("files", {})
                print(f"Loaded incremental cache for {len(cache)} files.")
            else:
                print("Cache parameters mismatched. Doing a clean rebuild.")
        except Exception as e:
            print(f"Failed to load cache ({e}). Doing a clean rebuild.")

    now_iso = datetime.now(timezone.utc).isoformat()

    # Track files to process
    reused_count = 0
    new_modified_files = []
    
    # Store active paths for GC
    active_rel_paths = set()

    # Map files and check hashes
    for filepath in files:
        rel_path = str(filepath.relative_to(corpus_dir))
        active_rel_paths.add(rel_path)
        file_hash = compute_sha256(filepath)
        
        if rel_path in cache and cache[rel_path].get("hash") == file_hash:
            reused_count += 1
        else:
            new_modified_files.append((filepath, rel_path, file_hash))

    print(f"Incremental Status: {reused_count} files up-to-date, {len(new_modified_files)} new/modified files to index.")

    # Only load models if we actually have new or modified files to process
    new_chunks = []
    new_metadata = []
    new_embeddings = None
    
    if new_modified_files:
        print(f"Loading embedding model: {model_name}")
        model = SentenceTransformer(model_name)
        
        # Detect if BGE model
        is_bge = 'bge' in model_name.lower()
        if is_bge:
            print("  -> BGE model detected. Documents will be encoded without prefix.")

        # Chunk and prepare files
        for filepath, rel_path, file_hash in new_modified_files:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read().strip()
            if not text:
                continue

            framework, category = infer_framework_category(rel_path)
            chunks = chunk_text(text, chunk_size, chunk_overlap)
            
            file_chunks_data = []
            for chunk_idx, chunk_text_str in enumerate(chunks):
                file_chunks_data.append({
                    "text": chunk_text_str,
                    "metadata": {
                        'filename': filepath.name,
                        'relative_path': rel_path,
                        'chunk_index': chunk_idx,
                        'total_chunks': len(chunks),
                        'framework': framework,
                        'category': category,
                        'word_count': len(chunk_text_str.split()),
                        'char_count': len(chunk_text_str),
                        'source_type': 'generated',
                        'indexed_at': now_iso,
                        'embedding_model': model_name,
                    }
                })
            
            # Save mapping in temp list for encoding in batch
            new_chunks.extend([c["text"] for c in file_chunks_data])
            new_metadata.extend(file_chunks_data)

        if new_chunks:
            print(f"Generating embeddings for {len(new_chunks)} new chunks...")
            new_embeddings = model.encode(new_chunks, show_progress_bar=True, batch_size=32)
            
            # Map embeddings back to their cache structure
            start_idx = 0
            for filepath, rel_path, file_hash in new_modified_files:
                # Find chunks for this file
                file_chunks = [c for c in new_metadata if c["metadata"]["relative_path"] == rel_path]
                if not file_chunks:
                    continue
                
                cached_chunks = []
                for chunk in file_chunks:
                    emb = new_embeddings[start_idx]
                    cached_chunks.append({
                        "text": chunk["text"],
                        "metadata": chunk["metadata"],
                        "embedding": emb
                    })
                    start_idx += 1
                
                cache[rel_path] = {
                    "hash": file_hash,
                    "chunks": cached_chunks
                }

    # Garbage collect deleted files from cache
    cache = {k: v for k, v in cache.items() if k in active_rel_paths}

    # Reassemble all chunks, metadata, and embeddings from cache
    all_chunks = []
    all_metadata = []
    all_embeddings_list = []
    file_stats = {
        'total_files': len(cache),
        'total_chunks': 0,
        'files_by_framework': {},
    }

    for rel_path, cached_data in sorted(cache.items()):
        framework, _ = infer_framework_category(rel_path)
        file_stats['files_by_framework'][framework] = \
            file_stats['files_by_framework'].get(framework, 0) + 1
            
        for chunk in cached_data["chunks"]:
            all_chunks.append(chunk["text"])
            all_metadata.append(chunk["metadata"])
            all_embeddings_list.append(chunk["embedding"])

    file_stats['total_chunks'] = len(all_chunks)
    
    if not all_embeddings_list:
        print("Error: No chunks indexed.")
        sys.exit(1)

    all_embeddings = np.array(all_embeddings_list)
    dimension = all_embeddings.shape[1]

    # Build new FAISS index
    index = faiss.IndexFlatL2(dimension)
    index.add(all_embeddings)

    # Pre-build BM25Okapi index and serialize it
    print("Pre-building BM25 Index...")
    tokenized_chunks = [text.lower().split() for text in all_chunks]
    bm25 = BM25Okapi(tokenized_chunks)

    # Save everything to disk
    index_dir.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(index_path))

    index_metadata = {
        'documents': all_metadata,
        'texts': all_chunks,
        'model_name': model_name,
        'corpus_dir': str(corpus_dir),
        'total_documents': file_stats['total_files'],
        'total_chunks': file_stats['total_chunks'],
        'chunk_size': chunk_size,
        'chunk_overlap': chunk_overlap,
        'dimension': dimension,
        'built_at': now_iso,
        'files_by_framework': file_stats['files_by_framework'],
    }

    with open(meta_path, "wb") as f:
        pickle.dump(index_metadata, f)

    with open(bm25_path, "wb") as f:
        pickle.dump(bm25, f)

    # Save cache
    with open(cache_path, "wb") as f:
        pickle.dump({
            "model_name": model_name,
            "chunk_size": chunk_size,
            "chunk_overlap": chunk_overlap,
            "files": cache
        }, f)

    print(f"\n{'='*60}")
    print(f"[OK] Index and BM25 built and saved successfully!")
    print(f"  Index:      {index_path} ({index_path.stat().st_size:,} bytes)")
    print(f"  Metadata:   {meta_path} ({meta_path.stat().st_size:,} bytes)")
    print(f"  BM25:       {bm25_path} ({bm25_path.stat().st_size:,} bytes)")
    print(f"  Cache:      {cache_path} ({cache_path.stat().st_size:,} bytes)")
    print(f"  Files:      {file_stats['total_files']}")
    print(f"  Chunks:     {file_stats['total_chunks']}")
    print(f"  Dimension:  {dimension}")
    print(f"  Model:      {model_name}")
    print(f"  Chunk size: {chunk_size} words (overlap: {chunk_overlap})")
    print(f"{'='*60}")

    # Invalidate web portal query cache after re-indexing
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
        django.setup()
        from django.core.cache import cache
        cache.clear()
        print("[OK] Web portal query cache invalidated.")
    except Exception:
        pass  # Non-critical if Django is not configured


def main():
    parser = argparse.ArgumentParser(description="Build FAISS index from corpus files")
    parser.add_argument(
        "--corpus-dir", type=Path, default=DEFAULT_CORPUS_DIR,
        help=f"Path to corpus directory (default: {DEFAULT_CORPUS_DIR})"
    )
    parser.add_argument(
        "--index-dir", type=Path, default=DEFAULT_INDEX_DIR,
        help=f"Path to save index (default: {DEFAULT_INDEX_DIR})"
    )
    parser.add_argument(
        "--model", type=str, default=DEFAULT_MODEL,
        help=f"Sentence-transformers model name (default: {DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--chunk-size", type=int, default=DEFAULT_CHUNK_SIZE,
        help=f"Words per chunk (default: {DEFAULT_CHUNK_SIZE})"
    )
    parser.add_argument(
        "--chunk-overlap", type=int, default=DEFAULT_CHUNK_OVERLAP,
        help=f"Word overlap between chunks (default: {DEFAULT_CHUNK_OVERLAP})"
    )
    parser.add_argument(
        "--force-rebuild", action="store_true",
        help="Skip confirmation and overwrite existing index"
    )
    parser.add_argument(
        "--incremental", action="store_true",
        help="Build index incrementally using cached embeddings"
    )
    args = parser.parse_args()

    build_index(
        args.corpus_dir, args.index_dir, args.model,
        args.chunk_size, args.chunk_overlap, args.force_rebuild,
        args.incremental
    )


if __name__ == "__main__":
    main()