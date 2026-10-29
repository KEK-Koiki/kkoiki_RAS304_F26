# Elijah Koiki — RAS304 Team 103

Individual datasheet for the two-motor encoder subsystem.

Live site: https://kek-koiki.github.io/kkoiki_RAS304_F26/

## Local development

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Run `python -m mkdocs build --strict` before publishing. Markdown lives in `docs/`; existing assignment URLs are retained. Push to `main` to trigger the GitHub Pages workflow. Build output in `site/` is ignored for future changes (legacy tracked output is retained).

The schematic's ERC pass is recorded evidence, not hardware validation. Open technical decisions and missing final inputs are listed on the Review & Resources page. No motor/ribbon approval, firmware implementation or fabrication readiness is claimed.
