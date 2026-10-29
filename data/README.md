# Purchasing inputs

`bom/` separates the current purchasing examples into core electronics, passives, interfaces and an optional adapter. Change the relevant JSON record, update the review date in `metadata.json`, then run `python tools/bom/render.py`.

Extended costs are calculated. Public CSV/JSON downloads and table/card markup are generated from these inputs. Keep source URLs and selection notes with the records. The root `EDITING.md` explains fields and export behavior.
