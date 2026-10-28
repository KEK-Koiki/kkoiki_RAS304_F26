---
title: Bill of Materials
---


# Bill of Materials

This design BOM is extracted from the **Revision B exported KiCad netlist**. Q1–Q4 are added explicitly because the off-board optical sensors are intentionally excluded from the PCB netlist. IC units count as one physical package each.

[Download BOM CSV](encoder-revb-bom.csv){.download} [Download KiCad project](../04-Schematic/Team103_Encoder_EK_Project.zip){.download}

| References | Quantity | Description / value | Procurement status |
| --- | ---: | --- | --- |
| A1 | 1 | EK PIC18F57Q43 CURIOSITY NANO | Package / sourcing pending |
| C1 | 1 | 0.33uF 25V | Package / sourcing pending |
| C2, C8, C9, C10 | 4 | 0.1uF 25V | Package / sourcing pending |
| C3 | 1 | 10uF 25V | Package / sourcing pending |
| C4, C5, C6, C7 | 4 | 1nF 25V | Package / sourcing pending |
| C11 | 1 | 100nF 25V | Package / sourcing pending |
| D1 | 1 | GREEN / POWER | Package / sourcing pending |
| D2 | 1 | YELLOW / DEBUG | Package / sourcing pending |
| F1 | 1 | 500 mA FAST / REMOVABLE | Package / sourcing pending |
| J1 | 1 | 9-12 V DC / CENTER + | Package / sourcing pending |
| J2 | 1 | E1A SENSOR CABLE | Package / sourcing pending |
| J3 | 1 | E1B SENSOR CABLE | Package / sourcing pending |
| J4 | 1 | E2A SENSOR CABLE | Package / sourcing pending |
| J5 | 1 | E2B SENSOR CABLE | Package / sourcing pending |
| J6 | 1 | 2x4 RIBBON / TEAM BUS | Package / sourcing pending |
| J7 | 1 | SPARE GPIO / POWER | Package / sourcing pending |
| JP1 | 1 | TX ISOLATE | Package / sourcing pending |
| R1, R18 | 2 | 1k 0.25W | Package / sourcing pending |
| R2, R6, R10, R14 | 4 | 220 0.25W | Package / sourcing pending |
| R3, R7, R11, R15 | 4 | 4.7k 0.25W | Package / sourcing pending |
| R4, R8, R12, R16, R19 | 5 | 10k 0.25W | Package / sourcing pending |
| R5, R9, R13, R17 | 4 | 20k 0.25W | Package / sourcing pending |
| SW1 | 1 | DEBUG / N.O. | Package / sourcing pending |
| TP1 | 1 | VIN_FUSED | Package / sourcing pending |
| TP2 | 1 | +5V | Package / sourcing pending |
| TP3 | 1 | GND | Package / sourcing pending |
| TP4 | 1 | E1A_RAW | Package / sourcing pending |
| TP5 | 1 | E1B_RAW | Package / sourcing pending |
| TP6 | 1 | E2A_RAW | Package / sourcing pending |
| TP7 | 1 | E2B_RAW | Package / sourcing pending |
| TP8 | 1 | ENC_TX | Package / sourcing pending |
| TP9 | 1 | ENC_RX | Package / sourcing pending |
| U1 | 1 | L7805ACV | Package / sourcing pending |
| U2 | 1 | MCP6004 | DIP-14 assigned; verify exact orderable suffix |
| U3 | 1 | SN74HC14N | DIP-14 assigned; verify exact orderable suffix |
| Q1–Q4 | 4 | Vishay TCST2103 (off-board) | Physical lead mapping and mounting pending |

## Procurement and assembly notes

Prices and a procurement total are **unavailable until the exact package and supplier choices are confirmed**. The current schematic has several unassigned footprints; the Nano socket, jack, fuse holder, connectors and passive packages need a physical fit check. Use the [component selection references](../02-Component-Selection/Component-Selection.md) to verify manufacturer specifications before ordering.

The 500 mA removable fast fuse is the drawn value, not a completed protection study. Verify its time-current curve, holder rating and wire/trace protection against the actual load. Optical sensors, disks, mounting brackets, cables, an adapter, sockets and any heatsink must be included in the final purchasing list.

**Consistency note:** C11 is **100 nF** in the actual Revision B netlist. With R19 = 10 kΩ, its nominal RC time constant is **1 ms**. An older schematic note says 10 ms; review and correct that annotation or intentionally revise the component value before fabrication.
