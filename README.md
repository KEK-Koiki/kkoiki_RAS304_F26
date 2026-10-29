# Elijah Koiki — RAS304 Team 103

Individual motor encoder datasheet for the **2 DOF Smart Robot Arm Joint Showcase**.

**[Published website](https://kek-koiki.github.io/kkoiki_RAS304_F26/)** · **[Quick editing guide](EDITING.md)** · **[Repository map](REPOSITORY_MAP.md)** · **[Change record](CHANGELOG.md)**

## Start here

| What you want to change | Start with |
| --- | --- |
| Home page wording | `docs/index.md` |
| Block diagram labels or lines | `design/diagrams/encoder.svg` |
| Block diagram explanation | `docs/01-Block-Diagram/Block-Diagram.md` |
| Component comparisons or MCC pin plan | `docs/02-Component-Selection/Component-Selection.md` |
| Part numbers, quantities, prices or supplier links | The relevant small JSON file in `data/bom/` |
| BOM introduction, notes or section wording | `templates/bom/page.md` |
| Schematic circuit | `design/ecad/encoder-revb/Team103_Encoder_EK.kicad_pro` in KiCad |
| Schematic explanation | `docs/04-Schematic/schematic.md` |
| Power calculations | Excel workbook and JSON inputs in `docs/05-Power-Budget/` |
| Colors, fonts or spacing | Named files in `docs/stylesheets/` |
| Page order or website identity | `mkdocs.yml` |

The original numbered assignment folders and public URLs are preserved. `docs/` contains published pages and exports; `design/`, `data/`, `templates/` and `tools/` contain editable sources. Old examples live in `archive/`.

## Preview and publish

Use Python 3.12 or newer:

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open the local URL printed by MkDocs. Stop the preview with Ctrl+C.

Before committing:

```powershell
python tools/bom/render.py --check
python -m mkdocs build --strict
python tools/check_links.py
```

Commit and push to `main` to deploy through `.github/workflows/pages.yml`. Review the successful GitHub Actions run before assuming the public website has updated.

Node.js is **optional** for website builds. It is only needed to export the diagram after editing its SVG:

```powershell
npm install
npm run diagram:export
```

Generated `site/`, local `node_modules/` and `_artifacts/` are ignored by Git. Do not edit generated HTML to change the website. See [EDITING.md](EDITING.md) for the source/export relationships.

## Engineering status

The website records an ERC-reviewed schematic and provisional purchasing/power estimates. Hardware validation, physical fit, firmware and final team interface approval remain separate engineering work. Repository organization does not change the circuit or claim fabrication readiness.

The tested optional Node dependency tree is recorded in pnpm-lock.yaml; pnpm users can install it with pnpm install --frozen-lockfile.
