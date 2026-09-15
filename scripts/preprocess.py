#!/usr/bin/env python3
"""Copy included teaching resources into the publisher's generated print tree."""
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "_print_source"

def main():
    if not OUTPUT_DIR.is_dir():
        raise SystemExit("Run standard preprocessing before this hook.")
    for name in ("tools", "resources"):
        source = PROJECT_ROOT / name
        if source.is_dir():
            shutil.copytree(source, OUTPUT_DIR / name, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("._*", ".DS_Store"))
            print(f"    Copied teaching resources: {name}")
    # Included Markdown needs the same print processing as configured QMD.
    sys.path.insert(0, str(PROJECT_ROOT.parent / "book-publisher" / "tools"))
    from preprocess_for_print import strip_markdown_links, wrap_code_blocks, convert_blockquotes_for_print
    for source in (OUTPUT_DIR / "tools").glob("*.md"):
        if source.name.startswith("._"):
            continue
        text = strip_markdown_links(source.read_text(encoding="utf-8"))
        text = wrap_code_blocks(text)
        text = convert_blockquotes_for_print(text)
        source.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
