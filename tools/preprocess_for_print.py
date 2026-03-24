#!/usr/bin/env python3
"""
PDP-specific preprocessing hook for print output.

Called by the standard book-publisher preprocessing pipeline AFTER files
have been copied to _print_source/ and links have been stripped.

This hook converts panel-tabset blocks into single-discipline callout
boxes, rotating through disciplines for variety. It operates on files
in _print_source/ in-place.
"""

import re
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

    # Note: plain-text URL here since embedded links are stripped for KDP
    callout = (
        f'::: {{.callout-tip title="Example: {chosen_name}"}}\n'
        f"{content}\n"
        f":::\n\n"
        f"*See the online edition ({ONLINE_URL}) for examples across all eight business disciplines.*"
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


def main():
    """
    Process all .qmd files in _print_source/ to convert tabsets.

    Called as a hook by the standard book-publisher preprocessing pipeline.
    Files are already in _print_source/ — we modify them in-place.
    """
    global _discipline_index
    _discipline_index = 0

    if not OUTPUT_DIR.exists():
        print("  Error: _print_source/ does not exist. Run standard preprocessing first.")
        return

    # Process all .qmd files in _print_source/
    qmd_files = sorted(OUTPUT_DIR.rglob("*.qmd"))
    for qmd_file in qmd_files:
        text = qmd_file.read_text(encoding="utf-8")

        # Only process files that actually contain tabsets
        if ".panel-tabset" not in text:
            continue

        processed = process_tabsets(text)
        qmd_file.write_text(processed, encoding="utf-8")
        rel_path = qmd_file.relative_to(OUTPUT_DIR)
        print(f"    Converted tabsets: {rel_path}")


if __name__ == "__main__":
    main()
