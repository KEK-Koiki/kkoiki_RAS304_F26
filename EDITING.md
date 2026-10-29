# Quick editing guide

The website keeps its original assignment folders. You can edit normal page text directly in VS Code or with the pencil link on the published page. Use the source paths below for generated tables and figures so a later export does not undo your edits.

## 1. Page text

| Website section | Editable Markdown |
| --- | --- |
| Overview | `docs/index.md` |
| Block Diagram | `docs/01-Block-Diagram/Block-Diagram.md` |
| Component Selection | `docs/02-Component-Selection/Component-Selection.md` |
| Schematic | `docs/04-Schematic/schematic.md` |
| Power Budget | `docs/05-Power-Budget/Power-Budget.md` |
| Review & Resources | `docs/Appendix/index.md` |

Headings beginning with `##` divide each page into searchable sections. Use short Markdown links and descriptive image text. Existing image/download names are retained to preserve links already shared with the instructor.

The BOM page and component **photo cards** have structured sources described below. The component comparison tables and PIC/MCC section remain ordinary editable Markdown.

## 2. Parts, prices and BOM tables

Choose the smallest relevant source file:

| Catalog | Contents |
| --- | --- |
| `data/bom/core.json` | Nano, optical sensors, op-amp, Schmitt inverter, regulator |
| `data/bom/passives.json` | Resistors and capacitors |
| `data/bom/interfaces.json` | Headers, jack, fuse/holder, switch, LEDs and test points |
| `data/bom/adapter.json` | Optional external power adapter |
| `data/bom/metadata.json` | Price review date, currency and pricing basis |

Each part has a readable `description`, `refs`, `qty`, `manufacturer`, `mpn`, `price`, `source` and `note`. `price` is the **unit** USD price at the stated tier; `qty` is the number required. Do not type a line total: the tool calculates it. Preserve the existing `group` and `key` fields when changing an existing part.

After checking the supplier page, update its price/source and the review date. Then run:

```powershell
python tools/bom/render.py
```

This updates:

- `docs/03-BOM/BOM.md`: tables, category totals, notes and subtotal.
- `docs/03-BOM/encoder-revb-bom.csv`: spreadsheet-friendly export.
- `docs/03-BOM/encoder-parts-sources.json`: public sourcing record.
- Only the photo-card region of the component-selection page; its technical discussion is preserved.

For BOM introductions, cost explanations or unpriced-item wording, edit `templates/bom/page.md`, then run the same command. Keep the `{{TOKEN}}` markers: those are the insertion points for generated tables, totals and part notes.

For card layout/wording, edit the small files in `templates/components/`. The adapter card's voltage/description is editorial text: update that template too if you choose a different supply. `--check` reports stale generated content without changing any file.

### Product pictures

Pictures are in `docs/static/parts/`. Keep the source/credit URL in the part record. `local_image` is relative to the public sourcing record; the renderer adjusts it for the deeper rendered HTML page. A typical value is `../static/parts/tcst2103.jpg`.

The page uses locally stored reference photos so it does not depend on a remote image host. Do not infer dimensions or electrical specifications from a photograph.

## 3. Block diagram

The master is **`design/diagrams/encoder.svg`**. It is formatted as readable XML and opens in SVG editors such as Inkscape. Search the text labels (for example `RB0`, `L7805` or `J6`) to make a small text change. An SVG editor is easier for moving boxes and wires.

Export after editing:

```powershell
npm install
npm run diagram:export
```

The tool in `tools/diagrams/` updates the existing public PNG/SVG filenames and source ZIP in `docs/01-Block-Diagram/`. Both image aliases are intentionally retained: the home page and block-diagram page use those established URLs. The exporter never overwrites page text.

`npm run diagram:check` compares the master SVG's rendered pixels with the published PNG. Use the same fonts, especially Arial, for consistent rendering across computers. If Python is named differently on your system, set `PYTHON` before running the export; Python only packages the ZIP.

## 4. Schematic

Open `design/ecad/encoder-revb/Team103_Encoder_EK.kicad_pro` in KiCad. Keep `EK.kicad_sym` and `sym-lib-table` beside the project. Review notes and the recorded ERC report are in that folder too.

After an intentional electrical change, run ERC and review the design. Export the new PDF/PNG and package the project/library files into the existing downloads under `docs/04-Schematic/`. Update the revision and result text in `schematic.md`. The website does not build KiCad files automatically.

The previous sensor-PCB exercise remains a separate downloadable assignment under `docs/Appendix/`; it is not the current encoder PCB.

## 5. Power budget

For quick edits, open `docs/05-Power-Budget/Team103_Encoder_Power_Budget.xlsx` in Excel. Update assumptions in `budget-inputs.json` and the displayed explanation/table in `Power-Budget.md` to match the revised workbook. These published outputs are intentionally reviewed manually, not changed by a normal site build.

Advanced authoring provenance is in `tools/power-budget/`. Its optional builder requires the Codex artifact runtime and writes a candidate workbook to `_artifacts/`; ordinary site work does not require that runtime. See the README in that folder before using it.

## 6. Styles and navigation

| File under `docs/stylesheets/` | Responsibility |
| --- | --- |
| `base.css` | Colors, typography, tables, shared controls, header/footer |
| `overview.css` | Home hero, navigation cards, metadata and cost tiles |
| `responsive.css` | Existing home-page phone/tablet breakpoints |
| `print.css` | Print layout |
| `products.css` | Product cards, BOM thumbnails and product-table styles |
| `layout.css` | Wide-screen space for the detailed assignment pages |
| `extra.css` | Small ordered import list; preserve its order |

Change page order, titles and repository links in `mkdocs.yml`. Keep Markdown filenames and directories when a public URL must stay stable. `custom_theme/main.html` contains the existing theme overrides; change it only for page-wide template behavior.

## 7. Check and publish

```powershell
python tools/bom/render.py --check
python -m mkdocs build --strict
python tools/check_links.py
git diff --check
git status
```

Preview changed pages with `python -m mkdocs serve`. Check photos, downloads and readability. Commit the relevant sources **and** updated generated exports. Push to `main`; GitHub Actions builds and deploys the site. You do not need to commit `site/`.

Old template examples and historical scripts are in `archive/`. They are reference material, not current editing entry points. Never run the old all-in-one scripts from the archive against the maintained website.

VS Code also provides **Terminal > Run Task** entries for preview, build, generated-table checks and link checks. Generated/dependency folders are hidden in its Explorer and excluded from ordinary search; the archive remains browsable.
