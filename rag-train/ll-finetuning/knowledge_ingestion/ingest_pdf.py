import argparse
import fitz  # PyMuPDF
import json
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF."""
    print(f"Extracting text from {pdf_path}...")
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None

def save_to_jsonl(text, source_name, output_file):
    """Saves the extracted text to a JSONL file."""
    # Chunking: Large books are too big for one context window.
    # We split by paragraphs or roughly 2000 chars for training chunks.
    
    chunks = []
    current_chunk = ""
    
    for paragraph in text.split('\n\n'):
        if len(current_chunk) + len(paragraph) < 2000:
            current_chunk += paragraph + "\n\n"
        else:
            chunks.append(current_chunk)
            current_chunk = paragraph + "\n\n"
    if current_chunk:
        chunks.append(current_chunk)

    mode = 'a' if os.path.exists(output_file) else 'w'
    with open(output_file, mode, encoding='utf-8') as f:
        for chunk in chunks:
            if chunk.strip():
                entry = {
                    "text": f"### Source: {source_name}\n\n{chunk.strip()}"
                }
                f.write(json.dumps(entry) + "\n")
    
    print(f"Saved {len(chunks)} chunks to {output_file}")

import os

def main():
    parser = argparse.ArgumentParser(description="Ingest PDF content for LLM fine-tuning.")
    parser.add_argument("--pdf", required=True, type=Path, help="Path to the PDF file.")
    parser.add_argument("--output", default="../data/train.jsonl", type=Path, help="Path to the output JSONL file.")
    
    args = parser.parse_args()
    
    if not args.pdf.exists():
        print(f"Error: PDF file not found: {args.pdf}")
        return

    text = extract_text_from_pdf(args.pdf)
    if text:
        save_to_jsonl(text, args.pdf.name, args.output)
        print("Done!")

if __name__ == "__main__":
    main()
