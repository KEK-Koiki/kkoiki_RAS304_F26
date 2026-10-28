---
title: Power Budget
---


# Power Budget

This **preliminary encoder-board planning estimate** accounts for the four emitters, PIC board, analog/logic ICs and support loads, then adds the required **25% margin**. Motors are powered on the motor-driver subsystem and are excluded from this local rail.

!!! warning "Estimate, not a verified maximum-current budget"
    The Nano, amplifier and logic entries include explicitly labeled planning allowances. They are not measured results or datasheet absolute maxima. A final course-template budget requires verified worst-case operating currents, the exact adapter and thermal measurements. Absolute maximum ratings are stress limits and should not be used as intended operating points.

## A · Loads on the +5 V rail

| Load | Quantity | Unit current (mA) | Total (mA) | Basis |
| --- | ---: | ---: | ---: | --- |
| Nano board + MCU | 1 | 100.00 | 100.00 | Planning allowance; actual firmware/debugger load unmeasured |
| TCST2103 emitters | 4 | 17.05 | 68.18 | Calculated nominal, 220 ohm / 1.25 V assumed LED drop |
| Collector pull-ups | 4 | 1.06 | 4.26 | All four raw nodes low; conservative pull-up bound |
| MCP6004 + feedback | 1 | 2.00 | 2.00 | Planning allowance including output/feedback loading |
| SN74HC14 | 1 | 5.00 | 5.00 | Planning allowance; depends on input edges and frequency |
| Power + debug LEDs | 2 | 3.00 | 6.00 | Planning allowance, 1k series resistors |
| Debug pull-up | 1 | 0.50 | 0.50 | Button held low, 10k at 5 V |

## B · Rail demand and margin

| Result | Planning estimate |
| --- | ---: |
| Sum of local +5 V loads | **185.94 mA** |
| Safety margin | **25%** |
| +5 V design-current estimate with margin | **232.42 mA** |
| Output power at the margin load | **1.162 W** |

The emitters alone account for about 68 mA under the nominal forward-drop assumption. Measure blocked/unblocked sensor currents and the running Nano board to replace the allowances. Current uncertainty and regulator heating matter more than the regulator's headline current rating.

## C · Regulator and thermal check

The schematic uses **L7805ACV**. Ignoring regulator ground current, `P_loss = (V_in − 5 V) × I_out`.

| Input | Dissipation at 232.42 mA | Ideal linear conversion efficiency |
| --- | ---: | ---: |
| 9 V | **0.930 W** | 55.6% |
| 12 V | **1.627 W** | 41.7% |

Regulator ground current adds input demand and dissipation. A heatsink/thermal design cannot be accepted from these numbers alone: check the actual package's junction-to-ambient or heatsink path, ambient temperature, maximum junction temperature and mounting. At the earlier review example of 250 mA, 12 V input produces approximately **1.75 W** before ground-current loss.

## D · External source

The team PRD specifies a **9 V wall adapter**, while the schematic allows 9–12 V at J1. A particular adapter is still unselected. Its usable continuous current must exceed the margin load plus regulator ground current, with appropriate polarity and connector fit. Until its rated output and regulator current are verified, remaining source capacity is **unavailable**. Start bring-up with a current-limited bench supply.

The drawn 500 mA fuse does not establish a safe supply rating or guaranteed semiconductor protection. Check the time-current characteristic, inrush, wiring and regulator thermal limits before accepting it.

## E · Battery runtime

**Not applicable to the current wall-powered concept.** If a battery is selected later, add usable capacity, discharge limits, conversion loss and runtime at the verified load.

## Reusable calculation

[Editable power-budget workbook](Team103_Encoder_Power_Budget.xlsx){.download} [Machine-readable inputs](budget-inputs.json){.download}

The workbook follows sections A–E and exposes the assumptions. It is a working planning model; final supplier and measurement data must replace the marked allowances before claiming a completed worst-case course budget.
