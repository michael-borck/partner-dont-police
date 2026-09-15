#!/usr/bin/env python3
"""Offline source regressions; passing is not educational or release approval."""
import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONFIG = (ROOT / "_quarto.yml").read_text()
FILES = re.findall(r"^\s*-\s+(\S+\.qmd)\s*$", CONFIG, re.M)
ORDER = ["introduction","understanding-ai","ethics-integrity","getting-started","seven-techniques","managing-context","critique-toolkit","flight-simulator","self-assessment","assessment","transforming-content","virtual-company","unit-design","global-perspectives","implementation-practicalities","conclusion"]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.labels, self.urls = set(), set(), []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "label":
            self.labels.add(attrs.get("for"))
        for name in ("src", "href"):
            if name in attrs:
                self.urls.append(attrs[name])

class ManuscriptTests(unittest.TestCase):
    def test_international_examples_are_hypothetical(self):
        text = (ROOT / "chapters/global-perspectives.qmd").read_text()
        self.assertIn("fictional teaching scenarios", text)
        self.assertIn("not reports about", text)
        self.assertEqual(len(re.findall(r"^#### Example [1-3]:", text, re.M)), 3)
        for old_claim in ("Successful Adaptation Examples", "**Results:**",
                          "Enhanced student engagement, improved learning outcomes",
                          "pending source/provenance review"):
            self.assertNotIn(old_claim, text)

    def test_licence_consistency(self):
        self.assertIn('license: "CC BY 4.0 International"', CONFIG)
        legal = (ROOT / "LICENSE-CONTENT.md").read_text()
        self.assertTrue(legal.startswith("Attribution 4.0 International\n"))
        self.assertIn("Section 8 -- Interpretation.", legal)
        self.assertIn("Directive 96/9/EC", legal)
        self.assertNotIn("ShareAlike", legal)
        for name in ("copyright.qmd", "copyright-page.tex", "README.md"):
            text = (ROOT / name).read_text()
            self.assertIn("CC BY 4.0 International", text, name)
            self.assertIn("https://creativecommons.org/licenses/by/4.0/", text, name)
            self.assertNotIn("All rights reserved", text, name)
            self.assertNotIn("No part of this publication may be reproduced", text, name)

    def test_configuration_and_order(self):
        self.assertEqual(len(FILES), 28)
        self.assertEqual(len(FILES), len(set(FILES)))
        self.assertEqual([Path(p).stem for p in FILES if p.startswith("chapters/")], ORDER)
        for name in FILES:
            self.assertTrue((ROOT / name).is_file(), name)
        for name in ("cover.png", "images/**", "tools/**", "resources/**"):
            self.assertIn("- " + name, CONFIG)
        for name in ("partner-dont-police.pdf", "partner-dont-police.epub", "llm.txt"):
            self.assertIn("href: /" + name, CONFIG)

    def test_local_source_targets(self):
        paths = [ROOT / p for p in FILES]
        paths += [p for p in (ROOT / "tools").glob("*.md") if not p.name.startswith("._")]
        for path in paths:
            text = path.read_text()
            for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                url = urlsplit(target)
                if url.scheme or not url.path or url.path.startswith("/"):
                    continue
                destination = path.parent / unquote(url.path)
                self.assertTrue(destination.exists(), f"{path.name}: {target}")

    def test_no_editor_artifacts_or_old_promises(self):
        for name in FILES:
            text = (ROOT / name).read_text()
            for forbidden in ("<parameter name=", "</content>", "all eight business disciplines",
                              "Chapters 19", "add your Amazon listing URL here"):
                self.assertNotIn(forbidden, text, name)
        for name in ("prompt-library", "workshop-guide"):
            self.assertIn("include ../tools/" + name + ".md",
                          (ROOT / "appendices" / (name + ".qmd")).read_text())

    def test_pack_arithmetic_and_source_ids(self):
        manifest = json.loads((ROOT / "resources/pdp-2026-1/manifest.json").read_text())
        pack = (ROOT / "appendices/pilot-pack.qmd").read_text()
        self.assertTrue(manifest["fictional"])
        self.assertEqual(sum(manifest["lesson_minutes"]), 60)
        self.assertEqual(sum(manifest["weights"]), 100)
        self.assertEqual(len(manifest["criteria"]), 5)
        for key, expected in (("P1-A", 4), ("P1-B", 17)):
            scores = manifest["sample_scores"][key]
            self.assertEqual(len(scores), len(manifest["criteria"]))
            self.assertTrue(all(0 <= n <= manifest["max_each"] for n in scores))
            self.assertEqual(sum(scores), expected)
        for source in manifest["sources"]:
            self.assertIn(source, pack)
        for criterion, a, b in zip(manifest["criteria"], manifest["sample_scores"]["P1-A"],
                                   manifest["sample_scores"]["P1-B"]):
            self.assertIn(f"| {criterion} | {a} | {b} |", pack)
        self.assertFalse(manifest["practice_threshold"]["institutional_standard"])
        self.assertIn("14/20", pack)
        supplier = manifest["supplier"]
        totals = [o["unit_price"] * supplier["quantity"] + o["freight"]
                  for o in supplier["offers"]]
        self.assertEqual(totals, [3800, 3500, 4000])
        self.assertEqual(supplier["quantity"] - supplier["offers"][1]["capacity"], 40)
        for total in totals:
            self.assertIn(f"${total:,}", pack)
        campaigns = manifest["marketing"]
        self.assertEqual([100*c["clicks"]/c["impressions"] for c in campaigns], [4, 5])
        self.assertEqual([100*c["purchases"]/c["clicks"] for c in campaigns], [5, 5])
        self.assertIn("4% and 5%", pack)

    def test_independent_route_and_safety(self):
        pack = (ROOT / "appendices/pilot-pack.qmd").read_text()
        self.assertIn("Use no model", pack)
        self.assertIn("STOP", pack)
        self.assertIn("not a report of a classroom trial", pack)
        offline = 0
        for name in FILES:
            if name.startswith("chapters/"):
                text = (ROOT / name).read_text().lower()
                offline += any(word in text for word in ("no ai", "no model", "paper", "without ai"))
        self.assertGreaterEqual(offline, 6)
        for name in ("prompt-library", "workshop-guide"):
            text = (ROOT / "tools" / (name + ".md")).read_text()
            self.assertIn("data gate", text)
            self.assertIn("STOP", text)

    def test_decision_sheet_boundaries(self):
        html = (ROOT / "tools/decision-sheet.html").read_text()
        page = Page()
        page.feed(html)
        for field in ("claim", "check", "decision"):
            self.assertIn(field, page.ids)
            self.assertIn(field, page.labels)
        self.assertFalse(page.urls)
        self.assertIn("connect-src 'none'", html)
        for api in ("fetch(", "XMLHttpRequest", "localStorage", "sessionStorage", "innerHTML"):
            self.assertNotIn(api, html)
        self.assertIn("pdp-m1-response.txt", html)
        self.assertIn("does not autosave", html)

if __name__ == "__main__":
    unittest.main(verbosity=2)
