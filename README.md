# Partner, Don't Police

An open Quarto book for business educators designing AI-supported practice and credible assessment.

- [Read the free edition](https://michael-borck.github.io/partner-dont-police)
- Paperback ISBN: **979-8-2542-3619-1** — [search Amazon](https://www.amazon.com.au/s?k=9798254236191)
- [All open books](https://books.borck.education)

The configured book has sixteen core chapters. Ethics precedes tool use; critique precedes simulation; self-assessment precedes assessment design. Appendices include the fictional PDP-2026.1 pilot pack, prompt library, workshop guide, rubrics, alignment, stress testing, glossary and reading list.

## Working with the manuscript

`_quarto.yml` is the authoritative chapter order. `index.qmd` is the maintained preface. The legacy `preface.qmd` is not configured.

`tools/prompt-library.md` and `tools/workshop-guide.md` are included in their appendix wrappers. `tools/decision-sheet.html` is a self-contained marketing exercise, with manual text export and no autosave or submission service. `resources/pdp-2026-1/manifest.json` records the fictional pack's checkable data.

From this repository:

```sh
python3 scripts/check_manuscript.py
quarto render --to html
```

For the KDP-oriented PDF/EPUB pipeline, run from the parent books workspace with the sibling publisher installed:

```sh
python3 book-publisher/publish.py --book pdp --preprocess --llm --render
python3 book-publisher/tools/check_rendered_book.py partner-dont-police
python3 book-publisher/publish.py --book pdp --audit
```

The publisher prepares a disposable `_print_source/` tree with separate PDF and EPUB profiles. The source manuscript remains the maintained edition. Generated files are not a KDP submission or a claim that Amazon carries the latest revision.

## Revision and release

See `EDITORIAL-REVISION.md` for the revision record, checks and outstanding release gates. The pilot is fictional and has not been validated through a reported classroom trial. Check local policy, access, workload and independent assessment before use.

The author confirmed [CC BY 4.0 International](https://creativecommons.org/licenses/by/4.0/) for this book. The official legal text is in `LICENSE-CONTENT.md`; metadata and copyright pages use the same licence. The author also approved recasting the international examples as hypothetical teaching scenarios. Existing artwork/third-party permissions and reader/release proof remain gates recorded in the revision note.

## Licence

Book content is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0 International)](https://creativecommons.org/licenses/by/4.0/). Original code examples and accompanying software are licensed under the [MIT License](https://opensource.org/licenses/MIT).

These grants cover material the author has authority to license. Separately credited third-party material retains its stated terms. Give appropriate credit, link the content licence and indicate changes; retain the MIT notice when reusing code.

See [LICENSE](LICENSE), [LICENSE-CONTENT.md](LICENSE-CONTENT.md) and [LICENSE-CODE.md](LICENSE-CODE.md) for scope and full terms.
