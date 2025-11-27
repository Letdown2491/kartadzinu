#!/usr/bin/env python3
"""Convert vocabulary.md to vocab-data.js for the Kartadzinu website."""

import re
import json

def parse_vocabulary(md_path):
    """Parse vocabulary.md and return list of entry dicts."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = []

    # Pattern for entries: **word** /pron/ *pos*
    entry_pattern = re.compile(
        r'^\*\*([^*]+)\*\*\s+/([^/]+)/\s+\*([^*]+)\*(?:\s+\(([^)]+)\))?',
        re.MULTILINE
    )

    # Split by entries
    parts = re.split(r'\n(?=\*\*[a-záéíóú])', content, flags=re.IGNORECASE)

    for part in parts:
        match = entry_pattern.match(part)
        if not match:
            continue

        word = match.group(1).strip()
        pron = match.group(2).strip()
        pos = match.group(3).strip()
        origin = match.group(4).strip() if match.group(4) else None

        # Extract definitions (lines starting with 1., 2., etc.)
        defs = []
        def_pattern = re.compile(r'^\d+\.\s+(.+)$', re.MULTILINE)
        for def_match in def_pattern.finditer(part):
            defs.append(def_match.group(1).strip())

        # Extract examples (lines with *example* "translation")
        examples = []
        ex_pattern = re.compile(r'^\s+-\s+\*([^*]+)\*\s+"([^"]+)"', re.MULTILINE)
        for ex_match in ex_pattern.finditer(part):
            examples.append(ex_match.group(1).strip())
            examples.append(ex_match.group(2).strip())

        entry = {
            "word": word,
            "pron": f"/{pron}/",
            "pos": pos,
            "defs": defs if defs else ["(see entry)"]
        }

        if examples:
            entry["ex"] = examples[:2]  # Keep first example pair

        if origin:
            entry["origin"] = origin

        entries.append(entry)

    return entries

def write_js(entries, output_path):
    """Write entries as JavaScript file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("// Kartadzinu Vocabulary Data\n")
        f.write(f"// Generated from vocabulary.md - {len(entries)} entries\n")
        f.write("const vocabData = ")
        json.dump(entries, f, ensure_ascii=False, indent=2)
        f.write(";\n")

if __name__ == "__main__":
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    md_path = os.path.join(project_dir, "reference", "vocabulary.md")
    js_path = os.path.join(project_dir, "js", "vocab-data.js")

    # Create js directory if needed
    os.makedirs(os.path.dirname(js_path), exist_ok=True)

    entries = parse_vocabulary(md_path)
    write_js(entries, js_path)

    print(f"Converted {len(entries)} vocabulary entries to {js_path}")
