# Focused tools

These tools run from any working directory and resolve the repository from their own location. They have no hardcoded user or checkout paths.

| Task | Command from the repository root |
| --- | --- |
| Refresh BOM and product cards | `python tools/bom/render.py` |
| Check generated BOM/card content | `python tools/bom/render.py --check` |
| Export edited SVG | `npm run diagram:export` |
| Check SVG/PNG consistency | `npm run diagram:check` |
| Check built links and downloads | `python tools/check_links.py` |
| Check another build directory | `python tools/check_links.py path/to/build` |

Python builds the website. Node/Sharp is optional for diagram export. The power-budget builder is an advanced optional authoring record with its own README; it is not part of a normal website build.

Do not use the archived one-time authoring scripts to edit the maintained source. See the root `EDITING.md` for the authoritative source of each output.
