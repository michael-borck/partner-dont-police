# Partner, Don't Police: editorial revision record

Date: 2026-09-15. Baseline: `75321fec1847ba32a94764cb810a5f3d639a3d93`.
Status: **approved editorial work implemented and locally validated; author decisions and release proof remain open**. Not committed, pushed or published in this pass.

## What changed

The sixteen core chapters retain their filenames but now place ethics before first use, critique before simulation, and self-assessment before assessment design. Repeated advocacy, generic discipline catalogues, forced disagreement and unsupported guarantees were cut.

Assessment now separates supported practice, submitted process evidence, independent capability and misconduct procedures. Transcript length, Flesch scores, model marks and conversation volume are not achievement bands. The revised rubric rewards disciplinary judgement, evidence and limits, with complete illustrative weights and non-AI routes.

The first-use data gate covers classification, authority, approved account/features, handling and an alternative route. Enterprise access and removing names are not blanket permission. Model/product distinctions, extraction, context, legal shorthand and consequential references were corrected or scoped. Generated personas are not independent evidence.

The original fictional **PDP-2026.1** pack supplies:

- P1-D1–D5: policy, records, prior-contact note, Alex's statement and authority.
- P1-A/P1-B: contrasting responses, with illustrative educator scores of 4/20 and 17/20.
- P1-F: explicitly authored flawed feedback, plus a corrected P1-R response and decision note.
- P2-D1–D4: an independent changed case requiring attention to retaliation and independent review.
- S1 and M1: numerical supplier and marketing adaptations, with checkable answers.
- P3: a pilot decision sheet for actual future observations.

The InnovateCo case now includes all four role cards, shared records and a bounded event/state ledger. It does not invent completed outcomes. Every core chapter provides a short activity; fixed inputs and paper routes remove dependence on a paid model.

The prompt library and 90-minute workshop were fully revised and included in HTML/PDF/EPUB appendices. The self-contained M1 HTML decision sheet exports plain text and offers printing; it has no server submission or autosave. The printed pack supplies the same task.

README, preface, reading routes, glossary and references now match the configured book. Obsolete tabbed-example promises and glossary tool-output contamination were removed. Canonical downloads, resource copies and print includes were repaired. Two author domains failed repeated checks; their contact links were replaced with the verified book repository and open-book collection.

ISBN **979-8-2542-3619-1** and artwork are unchanged. The author subsequently confirmed CC BY 4.0 International; metadata, official legal text and copyright notices now agree. The Amazon placeholder now uses the established ISBN search, not an invented ASIN.

## Scope and size

Baseline configured prose: approximately 48,759 words; core prose: 36,396.
Revised prose: approximately **25,542 words**, including the new pack and expanded resource includes; core prose: **16,090**, median **1,011**.
Configured headings fell from 612 to 279 and bullet lines from 1,593 to 137.

These are diagnostic counts, excluding fenced prompts/code, not quality scores. The initial metric tool omitted Markdown includes; it now expands them with cycle and book-boundary checks. Historical baseline files are preserved; revised metrics have separate filenames. The new plain-text export includes teaching prompts and included resources, approximately 28,746 whitespace-delimited words.

This is a substantial shortening, not a light copyedit. The author should review voice and the level of explanation in the shorter chapters. Removed material remains recoverable from Git history.

## Checks completed

- Eight offline manuscript tests pass, including licence consistency and hypothetical-case framing: order/files, source targets, obsolete artifacts, case arithmetic/source IDs, safety/non-AI route checks and decision-sheet boundaries.
- Fifteen publisher tests pass, including new include/export/cycle/path-boundary regressions and included-resource metric coverage.
- Decision-sheet JavaScript logic test passes for payload, filename, multiline text, print content and restoration using a minimal DOM. This is **not** a browser download or accessibility certification.
- Full preprocessing, text export and fresh HTML/PDF/EPUB render pass.
- Rendered validation: **28 HTML pages, 5,688 local targets/anchors, 30 EPUB spine entries; zero errors**. EPUB XML, heading order and archive integrity checked.
- PDF: **146 pages, 6 × 9 inches**; automated word bounds found no text outside the physical page. Selected physical pages 68, 104, 118 and 129 were visually reviewed for assessment/calibration/workshop tables. This is not a complete visual proof.
- Cover, author photo, decision sheet, prompt Markdown and case manifest are present in fresh HTML output.
- Final configured-manuscript external check: 24 URLs; 22 HTTP 200, two HTTP 403 access restrictions (Dawson DOI and Wineburg/McGrew publisher page). Bibliographic details were checked through the author's institutional repository and publisher web page. Reachability does not establish applicability.
- Publishing metadata audit: zero errors; four existing warnings remain: Amazon search URL, missing recorded ASIN, dashboard status unverified and uploaded source commit unknown.
- Both repository diffs pass whitespace checks.

The author-approved licence and international-example follow-up was rebuilt on 2026-09-15. HTML, PDF, EPUB and plain text contain CC BY 4.0 International with the conflicting restrictions removed; PDF/EPUB/plain text contain the fictional-example framing. The updated PDF copyright page (physical page 2) was visually checked. The earlier 24-URL reachability snapshot is retained; the added official Creative Commons legal code was checked separately.

## Author decisions and release gates

1. **Licence — resolved:** the author confirmed CC BY 4.0 International on 2026-09-15. The official unmodified text from https://creativecommons.org/licenses/by/4.0/legalcode.txt replaces the conflicting LICENSE. Metadata and both copyright formats now name and link the approved licence; contradictory blanket reproduction restrictions were removed. This does not confirm third-party/artwork rights.
2. **International stories — resolved:** the author approved hypothetical recasting on 2026-09-15. All three are now explicitly fictional planning exercises, with proposed actions and checks rather than observed results. National stereotypes and unsupported success claims were removed.
3. **Artwork/reused material:** confirm origin and permission for existing cover/illustrations and any reused third-party materials. Other books' confirmations do not resolve PDP's provenance.
4. **Fresh educator trial:** a reader who did not develop the pack should complete P1 calibration, challenge P1-F and attempt P2 before seeing its checks. Record disagreements, missing information, time and the justified continue/revise/pause/stop decision. A second reader should try the paper/non-AI and non-HR routes.
5. **Human release proof:** read the full PDF/EPUB, including long prompts and front matter, on target devices; test keyboard/screen-reader use, actual downloaded text content, printing and reload loss in the HTML sheet. Review institutional/legal requirements before classroom use. The PDF is not claimed to be tagged or accessibility-certified.
6. **Release direction:** approve remaining wording, then separately direct commit/push, hosted edition/chatbot refresh and any KDP submission. No account state or current Amazon edition was established by these source checks.

## Repeat locally

From the books workspace:

```sh
python3 partner-dont-police/scripts/check_manuscript.py
node partner-dont-police/scripts/check_decision_sheet.cjs
python3 -m unittest discover -s book-publisher/tools -p 'test_*.py'
python3 book-publisher/publish.py --book pdp --preprocess --llm --render
python3 book-publisher/tools/check_rendered_book.py partner-dont-police
python3 book-publisher/publish.py --book pdp --audit
```

External reachability is a separate network check:

```sh
python3 book-publisher/tools/check_external_book_links.py partner-dont-police
```
