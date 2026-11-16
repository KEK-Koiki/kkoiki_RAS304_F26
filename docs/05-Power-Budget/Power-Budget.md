---
title: Power Budget
---

# Power Budget

Revision D powers the encoders and logic from the local 5 V regulator. The motor winding supply is separate and is not part of this regulator load.

| Load | Planning allocation | Basis |
| --- | ---: | --- |
| Two encoder sensor boards | 20 mA | Supplier attachment: 10 mA maximum each |
| Nano target circuitry | 50 mA | Unmeasured engineering allocation, not a measured maximum |
| MCP6004 + HC14 | 5 mA | Conservative planning allocation; dynamic load depends on edges |
| LEDs, pull-ups and other loads | 25 mA | Planning allowance, not measured consumption |
| Total allocation | 100 mA | Provisional |
| With 25% margin | 125 mA | Design planning load |

At a regulated 9 V input, the LM7805 would dissipate approximately `(9 − 5) × 0.125 = 0.50 W`, plus its quiescent loss. This calculation is not a thermal qualification. Measure actual input voltage under load, rail current, regulator case temperature and startup behavior. Select any heatsink using the real package, ambient temperature and manufacturer thermal data. Do not size the fuse from motor stall current because that current does not pass through this PCB.

The motor listing's 250 mA rated / 1.2 A stall figures refer to each **12 V motor winding**, not the encoder supply. Do not reuse the obsolete optical LED power budget. A current class-stock inventory and supplier quote are needed before claiming compliance with the $60/member course budget.
