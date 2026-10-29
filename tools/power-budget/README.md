# Power budget

For a quick edit, open `docs/05-Power-Budget/Team103_Encoder_Power_Budget.xlsx` in Excel and update the table/explanation in `Power-Budget.md`. Inputs and their status are recorded in `budget-inputs.json` beside them.

`build.mjs` is the optional reproducible authoring source. It requires the Codex `@oai/artifact-tool` runtime (not a public npm dependency). It reads the existing JSON and writes a candidate workbook/preview under `_artifacts/power-budget/`; it does not silently replace the published workbook. Review and copy the candidate only after checking the calculations and layout. Ordinary website editing and builds do not need this library.
