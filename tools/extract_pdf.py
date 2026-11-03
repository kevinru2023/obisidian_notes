#!/usr/bin/env python3
"""
PDF extraction tool using docling (local, no API calls).
Converts PDFs to clean Markdown for wiki ingestion.

Handles text-based papers and image-heavy lecture slides.
Math is extracted using docling's built-in formula detection.

Setup:
    pip install docling

Usage:
    # Extract a single PDF
    python tools/extract_pdf.py path/to/file.pdf

    # Specify output path
    python tools/extract_pdf.py file.pdf raw-sources/courses/CS434/lecture01.md

    # Batch convert all PDFs in a directory
    python tools/extract_pdf.py --dir raw-sources/courses/CS434/
"""

import argparse
import sys
from pathlib import Path


def extract(input_path: Path, output_path: Path) -> bool:
    try:
        from docling.document_converter import DocumentConverter
    except ImportError:
        print("Error: docling not installed. Run: pip install docling", file=sys.stderr)
        return False

    try:
        converter = DocumentConverter()
        result = converter.convert(str(input_path))
        md = result.document.export_to_markdown()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(md, encoding="utf-8")
        print(f"  {input_path} → {output_path}")
        return True
    except Exception as e:
        print(f"  ERROR {input_path}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDFs to Markdown using docling (local)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", nargs="?", help="Input PDF file")
    parser.add_argument("output", nargs="?", help="Output .md file (default: same name)")
    parser.add_argument("--dir", metavar="DIR", help="Batch-convert all PDFs in a directory")

    args = parser.parse_args()

    if not args.input and not args.dir:
        parser.print_help()
        sys.exit(1)

    if args.dir:
        input_dir = Path(args.dir)
        if not input_dir.is_dir():
            print(f"Error: '{args.dir}' is not a directory", file=sys.stderr)
            sys.exit(1)

        files = sorted(input_dir.rglob("*.pdf"))
        if not files:
            print(f"No PDFs found in {args.dir}")
            sys.exit(0)

        print(f"Converting {len(files)} PDF(s) in {args.dir}...")
        success = sum(extract(f, f.with_suffix(".md")) for f in files)
        print(f"\nDone: {success}/{len(files)} converted successfully")

    else:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: '{args.input}' not found", file=sys.stderr)
            sys.exit(1)

        output_path = Path(args.output) if args.output else input_path.with_suffix(".md")
        if not extract(input_path, output_path):
            sys.exit(1)


if __name__ == "__main__":
    main()
