#!/usr/bin/env python3
"""
Preprocess Partner, Don't Police .qmd files for PDF/EPUB output.

Converts tabset panels into single-discipline callout boxes,
rotating through disciplines for variety. Outputs preprocessed
files into _print_source/ with a matching _quarto.yml for PDF/EPUB.
"""

import re
import shutil
import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "_print_source"

DISCIPLINES = [
    "Business & Marketing",
    "Management",
    "Human Resources",
    "Tourism & Hospitality",
    "Supply Chain & Logistics",
    "Information Systems",
    "Accounting & Finance",
    "Economics",
]

# Alternate name forms used in tab headings
DISCIPLINE_ALIASES = {
    "Management & Organisation Studies": "Management",
    "Management & Organization Studies": "Management",
    "Supply Chain": "Supply Chain & Logistics",
}

ONLINE_URL = "https://michael-borck.github.io/partner-dont-police"

# Counter for rotating disciplines across the whole book
_discipline_index = 0


def normalise_discipline(heading: str) -> str:
    """Map a tab heading to a canonical discipline name."""
    h = heading.strip().strip("#").strip()
    if h in DISCIPLINE_ALIASES:
        return DISCIPLINE_ALIASES[h]
    # Fuzzy match: check if any discipline name is contained in the heading
    for d in DISCIPLINES:
        if d.lower() in h.lower() or h.lower() in d.lower():
            return d
    return h


def pick_discipline() -> str:
    """Return the next discipline in rotation."""
    global _discipline_index
    d = DISCIPLINES[_discipline_index % len(DISCIPLINES)]
    _discipline_index += 1
    return d


def parse_tabset_tabs(block: str) -> dict[str, str]:
    """
    Parse a tabset block into {discipline_name: content} pairs.

    Tab headings use ## or # markdown headings inside the tabset.
    """
    tabs = {}
    # Split on heading lines (# or ##) that mark tab starts
    parts = re.split(r"^(#{1,2}\s+.+)$", block, flags=re.MULTILINE)

    current_heading = None
    for part in parts:
        heading_match = re.match(r"^#{1,2}\s+(.+)$", part.strip())
        if heading_match:
            current_heading = normalise_discipline(heading_match.group(1))
        elif current_heading is not None:
            content = part.strip()
            if content:
                tabs[current_heading] = content
            current_heading = None

    return tabs


def tabset_to_callout(block: str) -> str:
    """
    Convert a tabset block to a single callout-tip box.

    Picks one discipline via rotation. Falls back to first available
    if the target discipline isn't in this tabset.
    """
    tabs = parse_tabset_tabs(block)
    if not tabs:
        return ""

    target = pick_discipline()

    # Try to find the target discipline; fall back to any available
    if target in tabs:
        chosen_name = target
    else:
        # Try partial match
        chosen_name = None
        for name in tabs:
            if target.lower() in name.lower() or name.lower() in target.lower():
                chosen_name = name
                break
        if chosen_name is None:
            chosen_name = list(tabs.keys())[0]

    content = tabs[chosen_name]

    callout = (
        f'::: {{.callout-tip title="Example: {chosen_name}"}}\n'
        f"{content}\n"
        f":::\n\n"
        f"*See the [online edition]({ONLINE_URL}) for examples across all eight business disciplines.*"
    )
    return callout


def process_tabsets(text: str) -> str:
    """
    Find all ::: {.panel-tabset} ... ::: blocks and replace them.

    Handles nested ::: divs by counting open/close markers.
    """
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect tabset opening — handles both ::: and :::: variants
        if re.match(r"^:{3,}\s*\{\.panel-tabset\}", line.strip()):
            # Collect the entire tabset block
            depth = 1
            block_lines = []
            i += 1
            while i < len(lines) and depth > 0:
                l = lines[i]
                stripped = l.strip()
                # Opening a new div (but not a tabset — those would be nested)
                if re.match(r"^:{3,}\s*\{", stripped) or re.match(
                    r"^:{3,}\s*$", stripped
                ):
                    if re.match(r"^:{3,}\s*$", stripped):
                        depth -= 1
                        if depth == 0:
                            i += 1
                            break
                    else:
                        depth += 1
                block_lines.append(l)
                i += 1

            block_text = "\n".join(block_lines)
            callout = tabset_to_callout(block_text)
            result.append(callout)
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def generate_quarto_yml():
    """Generate _quarto.yml for print output based on the main one."""
    main_config_path = PROJECT_ROOT / "_quarto.yml"
    with open(main_config_path) as f:
        config = yaml.safe_load(f)

    # Keep book metadata and chapter list
    book = config.get("book", {})

    # Remove HTML-only features
    book.pop("favicon", None)

    print_config = {
        "project": {"type": "book", "output-dir": "_book"},
        "book": book,
        "format": {
            "pdf": {
                "documentclass": "book",
                "classoption": ["6in:9in"],
                "toc": True,
                "toc-depth": 1,
                "number-sections": True,
                "hyperrefoptions": "draft",
                "geometry": [
                    "paperwidth=6in",
                    "paperheight=9in",
                    "inner=1in",
                    "outer=0.625in",
                    "top=0.75in",
                    "bottom=0.75in",
                ],
                "include-in-header": "pdf-header.tex",
                "include-before-body": "copyright-page.tex",
            },
            "epub": {
                "toc": True,
                "toc-depth": 1,
                "css": "epub-styles.css",
            },
        },
    }

    output_path = OUTPUT_DIR / "_quarto.yml"
    with open(output_path, "w") as f:
        yaml.dump(print_config, f, default_flow_style=False, sort_keys=False)


def copy_assets():
    """Copy non-qmd assets needed for the build."""
    # Copy images directory if it exists
    images_src = PROJECT_ROOT / "images"
    if images_src.exists():
        images_dst = OUTPUT_DIR / "images"
        if images_dst.exists():
            shutil.rmtree(images_dst)
        shutil.copytree(images_src, images_dst)

    # Copy cover image
    cover = PROJECT_ROOT / "cover.png"
    if cover.exists():
        shutil.copy2(cover, OUTPUT_DIR / "cover.png")

    # Copy tex and css files from the print support directory
    for f in ["pdf-header.tex", "copyright-page.tex", "epub-styles.css"]:
        src = PROJECT_ROOT / f
        if src.exists():
            shutil.copy2(src, OUTPUT_DIR / f)


def main():
    global _discipline_index
    _discipline_index = 0

    # Clean and create output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Read main quarto config to get chapter list
    with open(PROJECT_ROOT / "_quarto.yml") as f:
        config = yaml.safe_load(f)

    book = config.get("book", {})
    chapters = book.get("chapters", [])
    appendices = book.get("appendices", [])
    all_files = chapters + appendices

    # Process each qmd file in chapter order (so rotation is deterministic)
    for entry in all_files:
        # entries can be strings or dicts with 'file' key
        if isinstance(entry, dict):
            filename = entry.get("file", "")
        else:
            filename = entry

        if not filename.endswith(".qmd"):
            continue

        src = PROJECT_ROOT / filename
        if not src.exists():
            print(f"  Warning: {filename} not found, skipping")
            continue

        text = src.read_text(encoding="utf-8")
        processed = process_tabsets(text)
        dst = OUTPUT_DIR / filename
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(processed, encoding="utf-8")
        print(f"  Processed: {filename}")

    # Generate print quarto config
    generate_quarto_yml()
    print("  Generated: _quarto.yml")

    # Copy assets
    copy_assets()
    print("  Copied assets")

    print(f"\nDone! Output in {OUTPUT_DIR}")
    print("To build PDF:  cd _print_source && quarto render --to pdf")
    print("To build EPUB: cd _print_source && quarto render --to epub")


if __name__ == "__main__":
    main()
