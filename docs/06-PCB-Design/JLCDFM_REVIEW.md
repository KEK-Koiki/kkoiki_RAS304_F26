# JLCDFM review — Revision D

Analysis completed against the exact Gerber ZIP with SHA-256 `4326565b6bc3e0e5cf9ff5fd74e7aa2d9d9549c44958eb962b935ef82f673ed3`.
Viewer: https://jlcdfm.com/viewer?pcbUploadFileId=645131007235584001
Default JLCDFM rules were retained. No thresholds were relaxed or findings hidden.

## Corrections made

Silkscreen strokes were increased to 0.18 mm, labels near pads and tented vias were moved, and near-pad outline graphics were moved to fabrication layers. All component references remain present. Project-local footprint copies match the schematic and board. Copper connectivity, pad positions and drill geometry were preserved. KiCad ERC is zero errors/warnings; GUI DRC is zero errors/warnings and zero unconnected; CLI schematic parity is zero; 219 static checks pass.

## Final default-rule results

The trace spacing, trace-to-edge, pad spacing, pad-to-edge, PTH-to-trace clearance, annular ring, solder-mask, silkscreen clearance, silkscreen width, drill spacing and missing-drill checks report no Danger/Warning findings. Counts in the green column are Good observations, not errors.

Remaining findings are intentionally visible in the evidence:

- **10 Danger / 7 Warning `tht to smd` findings.** The detail describes a via/pad proximity assembly rule, with default Danger below 2.03 mm and Warning below 3.05 mm. The observed minimum is about 1.39 mm. This board is intended for manual assembly, not automated wave soldering; these generous default assembly separations still require physical assembly/fit review. This is not an unconditional vendor approval.
- **13 sharp-corner warnings.** Review track junction and pad-entry geometry. Copper widths/clearances satisfy the stricter configured KiCad rules; these heuristic warnings have not been silently suppressed.
- **42 unconnected-trace-end warnings.** Gerber geometry heuristics do not have the source connectivity model. Source KiCad reports zero unrouted connections and schematic parity issues. Review these separately if the manufacturer requests it; do not interpret the screenshot as proving each heuristic resolved.
- **8 PTH-without-pad warnings.** The viewer labels both drill files as plated, including the explicitly named NPTH file. The design contains four non-plated mounting holes; the Excellon header identifies that file as NonPlated. Manufacturer review must preserve NPTH classification. Do not add copper to these mounting holes to silence an import warning.

## Release status

The required real preview/analysis screenshots now exist. They show completed analysis with the findings above; they are not an all-green report. Physical fit, adapter voltage/polarity/plug size, course exceptions, price review and student order approval remain pending. No order or Canvas submission was made.
