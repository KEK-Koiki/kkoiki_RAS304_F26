# Repository map

```text
docs/                         Published Markdown and stable download URLs
  index.md                    Home page
  01-Block-Diagram/            Diagram page and exported PNG/SVG/ZIP
  02-Component-Selection/      Comparisons, MCC plan and generated photo cards
  03-BOM/                     Generated priced page, CSV and sourcing record
  04-Schematic/               Schematic page, reviewed PDF/PNG/KiCad ZIP/ERC
  05-Power-Budget/             Power page, editable workbook and input JSON
  Appendix/                   Review checklist and earlier sensor assignment
  static/parts/               Supplier reference photographs
  stylesheets/                Small CSS files grouped by responsibility

design/
  diagrams/encoder.svg        Editable approved diagram master
  ecad/encoder-revb/          Raw KiCad project, library and review records

data/bom/                     Small purchasing catalogs by component group
templates/
  bom/page.md                 BOM prose with table/total insertion points
  components/                Small selected-part and adapter card templates

tools/
  bom/render.py               Refresh tables/cards/CSV from purchasing data
  diagrams/export.mjs         Export the SVG as public images
  diagrams/package.py         Refresh the diagram source ZIP
  power-budget/               Optional advanced workbook authoring source
  check_links.py              Check a MkDocs build's links/assets/ZIP files

archive/                      Unused original template and authoring history
custom_theme/main.html        Existing MkDocs template overrides
.github/workflows/pages.yml   GitHub Pages build/deployment
mkdocs.yml                    Site identity, navigation and plugins
requirements.txt              Python website dependencies
package.json                  Optional Node diagram-export dependency
```

`site/`, `node_modules/` and `_artifacts/` are generated/local folders, not tracked editing sources. An existing local copy may remain after migration; it is safe to rebuild it. No public URLs depend on their presence in the main branch.

The detailed file-by-file editing instructions are in [EDITING.md](EDITING.md).
