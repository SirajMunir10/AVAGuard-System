"""
AVAGuard RAG — Query FAISS Index

Loads the FAISS index and retrieves relevant corpus chunks for a given query.
Returns the actual text content (not just filenames) for downstream LLM generation.

Usage:
    python query_index.py                           # Interactive REPL mode
    python query_index.py --query "What is MFA?"    # Single query mode
    python query_index.py --top-k 5                 # Return top 5 results
"""

import sys
import argparse
import pickle
from pathlib import Path
from typing import List, Dict, Any

import faiss
from sentence_transformers import SentenceTransformer

# === Defaults ===
SCRIPT_DIR = Path(__file__).parent
DEFAULT_INDEX_DIR = SCRIPT_DIR / "faiss_index"


def load_index(index_dir: Path):
    """Load the FAISS index and metadata from disk."""
    index_dir = Path(index_dir)
    index_path = index_dir / "faiss.index"
    meta_path = index_dir / "meta.pkl"

    if not index_path.exists() or not meta_path.exists():
        print(f"Error: Index not found at {index_dir}")
        print("Run build_index.py first to create the index.")
        sys.exit(1)

    index = faiss.read_index(str(index_path))

    with open(meta_path, "rb") as f:
        index_metadata = pickle.load(f)

    return index, index_metadata


def query(
    query_text: str,
    index,
    index_metadata: dict,
    model: SentenceTransformer,
    top_k: int = 3
) -> List[Dict[str, Any]]:
    """
    Query the FAISS index and return the top-k most relevant documents.

    Returns:
        List of dicts, each containing:
        - filename: name of the corpus file
        - relative_path: path relative to corpus root
        - text: full text content of the document
        - distance: L2 distance (lower = more relevant)
        - word_count: number of words in the document
    """
    query_embedding = model.encode([query_text])
    distances, indices = index.search(query_embedding, top_k)

    documents = index_metadata.get("documents", [])
    texts = index_metadata.get("texts", [])

    results = []
    for i, idx in enumerate(indices[0]):
        if idx < 0 or idx >= len(documents):
            continue

        doc_meta = documents[idx]
        result = {
            "filename": doc_meta.get("filename", f"doc_{idx}"),
            "relative_path": doc_meta.get("relative_path", ""),
            "text": texts[idx] if idx < len(texts) else "",
            "distance": float(distances[0][i]),
            "word_count": doc_meta.get("word_count", 0),
        }
        results.append(result)

    return results


def print_results(results: List[Dict[str, Any]], show_text: bool = True):
    """Pretty-print query results."""
    if not results:
        print("No results found.")
        return

    for i, r in enumerate(results, 1):
        print(f"\n{'='*70}")
        print(f"Result {i}: {r['filename']}")
        print(f"  Path: {r['relative_path']}")
        print(f"  Distance: {r['distance']:.4f}")
        print(f"  Words: {r['word_count']}")
        if show_text:
            # Show first 500 chars as preview
            preview = r['text'][:500]
            if len(r['text']) > 500:
                preview += "..."
            print(f"  Preview:\n    {preview}")
        print(f"{'='*70}")


def interactive_mode(index, index_metadata, model, top_k: int = 3):
    """Run an interactive query REPL."""
    print("\n🛡️  AVAGuard RAG Query Interface")
    print(f"   Model: {index_metadata.get('model_name', 'unknown')}")
    print(f"   Documents indexed: {index_metadata.get('total_documents', '?')}")
    print(f"   Returning top {top_k} results per query")
    print(f"   Type 'exit' or 'quit' to stop\n")

    while True:
        try:
            query_text = input("Query > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not query_text or query_text.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        results = query(query_text, index, index_metadata, model, top_k)
        print_results(results)


def main():
    parser = argparse.ArgumentParser(description="Query the AVAGuard RAG index")
    parser.add_argument(
        "--query", "-q", type=str, default=None,
        help="Single query string (omit for interactive mode)"
    )
    parser.add_argument(
        "--top-k", "-k", type=int, default=3,
        help="Number of results to return (default: 3)"
    )
    parser.add_argument(
        "--index-dir", type=Path, default=DEFAULT_INDEX_DIR,
        help=f"Path to index directory (default: {DEFAULT_INDEX_DIR})"
    )
    parser.add_argument(
        "--no-text", action="store_true",
        help="Don't show text preview in results"
    )
    args = parser.parse_args()

    # Load index
    index, index_metadata = load_index(args.index_dir)
    model_name = index_metadata.get("model_name", "sentence-transformers/all-MiniLM-L6-v2")

    print(f"Loading model: {model_name}")
    model = SentenceTransformer(model_name)
    print("Index and model loaded successfully.\n")

    if args.query:
        # Single query mode
        results = query(args.query, index, index_metadata, model, args.top_k)
        print_results(results, show_text=not args.no_text)
    else:
        # Interactive mode
        interactive_mode(index, index_metadata, model, args.top_k)


if __name__ == "__main__":
    main()
