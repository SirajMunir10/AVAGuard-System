"""
Django management command to rebuild the FAISS vector index.

Usage:
    python manage.py rebuild_index
    python manage.py rebuild_index --corpus-dir /path/to/corpus
    python manage.py rebuild_index --model sentence-transformers/all-MiniLM-L6-v2
"""

import sys
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'Rebuild the FAISS vector index from corpus files'

    def add_arguments(self, parser):
        default_index_dir = getattr(settings, 'AI_INDEX_DIR', '')
        project_root = getattr(settings, 'PROJECT_ROOT', Path('.'))

        parser.add_argument(
            '--corpus-dir',
            type=str,
            default=str(project_root / 'rag-train' / 'll-finetuning' / 'rag' / 'corpus'),
            help='Path to the corpus directory containing .txt/.md files',
        )
        parser.add_argument(
            '--index-dir',
            type=str,
            default=default_index_dir,
            help='Path to save the FAISS index',
        )
        parser.add_argument(
            '--model',
            type=str,
            default='sentence-transformers/all-MiniLM-L6-v2',
            help='Sentence-transformers model name for embeddings',
        )

    def handle(self, *args, **options):
        corpus_dir = Path(options['corpus_dir'])
        index_dir_option = options['index_dir']
        if not index_dir_option:
            project_root = getattr(settings, 'PROJECT_ROOT', Path('.'))
            index_dir = Path(project_root) / 'rag-train' / 'll-finetuning' / 'rag' / 'faiss_index'
        else:
            index_dir = Path(index_dir_option)
        model_name = options['model']

        if not corpus_dir.exists():
            raise CommandError(f"Corpus directory not found: {corpus_dir}")

        # Import here to avoid loading FAISS/torch at Django startup
        try:
            import faiss
            from sentence_transformers import SentenceTransformer
        except ImportError as e:
            raise CommandError(
                f"Missing dependency: {e}. "
                "Install with: pip install faiss-cpu sentence-transformers"
            )

        # Collect corpus files
        extensions = {'.txt', '.md'}
        files = sorted([
            f for f in corpus_dir.rglob('*')
            if f.suffix.lower() in extensions and f.stat().st_size > 0
        ])

        if not files:
            raise CommandError(f"No .txt or .md files found in {corpus_dir}")

        self.stdout.write(f"Found {len(files)} corpus files in {corpus_dir}")
        self.stdout.write(f"Loading embedding model: {model_name}")

        model = SentenceTransformer(model_name)

        documents = []
        metadata = []

        for filepath in files:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read().strip()
                if text:
                    documents.append(text)
                    rel_path = filepath.relative_to(corpus_dir)
                    metadata.append({
                        'filename': filepath.name,
                        'relative_path': str(rel_path),
                        'word_count': len(text.split()),
                        'char_count': len(text),
                    })

        self.stdout.write(f"Loaded {len(documents)} non-empty documents")
        self.stdout.write("Generating embeddings...")

        embeddings = model.encode(documents, show_progress_bar=True)

        # Build FAISS index
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings)

        # Save
        index_dir = Path(index_dir)
        index_dir.mkdir(parents=True, exist_ok=True)

        import pickle
        index_path = index_dir / 'faiss.index'
        meta_path = index_dir / 'meta.pkl'

        faiss.write_index(index, str(index_path))

        index_metadata = {
            'documents': metadata,
            'texts': documents,
            'model_name': model_name,
            'corpus_dir': str(corpus_dir),
            'total_documents': len(documents),
        }

        with open(meta_path, 'wb') as f:
            pickle.dump(index_metadata, f)

        self.stdout.write(self.style.SUCCESS(
            f"\n[OK] Index rebuilt successfully!\n"
            f"  Index: {index_path} ({index_path.stat().st_size:,} bytes)\n"
            f"  Metadata: {meta_path} ({meta_path.stat().st_size:,} bytes)\n"
            f"  Documents indexed: {len(documents)}\n"
            f"  Embedding dimension: {dimension}\n"
            f"  Model: {model_name}"
        ))
