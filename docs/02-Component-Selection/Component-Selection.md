---
title: Component Selection
---


# Component Selection

The current choices follow the revised **two-motor optical encoder subsystem**. These comparison tables explain engineering tradeoffs; choices already drawn in Revision B are distinguished from alternatives and decisions awaiting physical measurements.

!!! note "Selection status"
    Current manufacturer pages are linked for verification. Exact orderable packages, supplier quotations and component photographs for every commercial alternative still need a procurement pass; no unverified prices are presented as quotations. Motor and ribbon decisions are deferred until the team confirms them.

## Optical sensing — individual subsystem

| Candidate | Advantages for this project | Limitations | Decision |
| --- | --- | --- | --- |
| **[Vishay TCST2103](https://www.vishay.com/en/product/81147/)** | Bare transmissive LED/phototransistor; analog collector node accessible to the custom front end | Needs a slotted disk, two sensors per shaft and rigid alignment | **Current selection: four sensors** |
| [Vishay TCST1103 family](https://www.vishay.com/en/product/83764/) | Another bare transmissive option with a documented mechanical package | Mechanical fit and optical response require comparison with the actual disk | Alternative if mounting favors this package |
| Custom reflective optical arrangement | Could read a patterned surface without placing a disk inside a fork | Depends on reflectance, ambient light and sensor standoff; needs new optical characterization | Architecture alternative; specific part unselected |

The TCST2103 keeps the design based on ordinary motors and gives each shaft an A/B pair. The sensor choice is conditional on disk and bracket fit. A built-in encoder motor would simplify mounting but would change the project's selected approach and needs team approval.

## Analog amplification — individual subsystem

| Candidate | Advantages | Limitations | Decision |
| --- | --- | --- | --- |
| **[MCP6004](https://www.microchip.com/en-us/product/MCP6004)** | Four amplifier channels in one IC; rail-to-rail input/output family; 1 MHz class | Current gain drives high inputs into saturation; recovery must be tested | **Current selection: U2, nominal gain 1.5** |
| [MCP6024](https://www.microchip.com/en-us/product/mcp6024) | Quad rail-to-rail family with 10 MHz bandwidth | More bandwidth may increase sensitivity to noise; power/package review needed | Alternative if measured edge response requires it |
| Two dual amplifiers | Splits channels across two packages for placement flexibility | Larger BOM and layout; exact device and supply compatibility unselected | Architecture alternative |

Each channel uses a 10 kΩ feedback resistor and 20 kΩ resistor to ground: `1 + 10k/20k = 1.5`. The 4.7 kΩ / 1 nF network has a nominal pole near **33.9 kHz** and a time constant of **4.7 µs**. Phototransistor impedance changes the actual response. Optical contrast, amplifier rail behavior and pulse timing require measurement before these values can be accepted.

## Digital edge conditioning — individual subsystem

| Candidate | Advantages | Limitations | Decision |
| --- | --- | --- | --- |
| **[SN74HC14](https://www.ti.com/product/SN74HC14)** | Six Schmitt inverter gates; four are sufficient for the encoder signals | Thresholds and dynamic supply current must be checked at operating voltage and edge rate | **Current selection: SN74HC14N / U3** |
| [CD40106B](https://www.ti.com/product/CD40106B) | Six Schmitt inverter gates; broad supply range | Timing and thresholds differ; cannot substitute without checking the pulse rate | Alternative |
| PIC input conditioning only | Fewer external components | Relies on PIC input behavior and software; removes the explicit external Schmitt stage | Architecture alternative requiring redesign |

The four used HC14 gates provide consistent edge conditioning. Unused inputs are tied to a defined level in the schematic. Both channels of each quadrature pair are inverted, so firmware must establish the actual forward direction during calibration.

## Regulation and power source

| Regulator option | Advantages | Limitations | Decision |
| --- | --- | --- | --- |
| **[ST L78 / L7805ACV](https://www.st.com/en/power-management/l78.html)** | Simple local 5 V rail; familiar through-hole package; matches Revision B | Linear dissipation rises with input voltage; heatsink and load must be verified | **Current schematic selection** |
| [ST L4940V5](https://www.st.com/en/power-management/l4940.html) | Lower dropout can help when input headroom is limited | At the same input/output/current, linear heat remains similar; stability and pinout need review | Alternative, not a drop-in approval |

The team PRD specifies an individual **9 V wall adapter**; Revision B labels its jack 9–12 V. A current-limited bench supply is suitable for development. A final adapter model, plug dimensions, current rating and procurement price have not been selected. A battery option adds runtime, charging and discharge considerations without a current project need. The [power budget](../05-Power-Budget/Power-Budget.md) explains why 9 V is thermally preferable to 12 V for the same load.

## PIC pins and MCC configuration plan

This is the configuration to implement and verify in MCC, derived from the schematic's Nano connector labels. **No completed MCC project or screenshot is available in the reviewed files.** Edge numbers below refer to the Nano board, not the MCU package pins.

| Signal | PIC pin | Nano edge | Planned configuration |
| --- | --- | --- | --- |
| E1A_DIG | RB0 | 46 | Digital input; interrupt-on-change candidate |
| E1B_DIG | RB1 | 10 | Digital input; interrupt-on-change candidate |
| E2A_DIG | RB2 | 9 | Digital input; interrupt-on-change candidate |
| E2B_DIG | RB3 | 47 | Digital input; interrupt-on-change candidate |
| MCU_TX → JP1 → ENC_TX | RC6 | 13 | UART TX via peripheral pin select; final UART instance and baud pending |
| ENC_RX | RC7 | 19 | UART RX via peripheral pin select; team protocol pending |
| DEBUG_LED | RA3 | 16 | Digital output; choose initial low state |
| DEBUG_BTN | RA4 | 17 | Digital input; stable-state firmware debounce |
| Spare GPIO | RA0 / RA1 | 43 / 44 | Reserved; do not assign conflicting peripherals |
| External +5 V | VTG | 51 | Verify Nano external-power procedure; VOFF edge 55 tied to ground |

Disable analog functions on digital signals, configure the selected clock and timing source, initialize quadrature state before enabling interrupts, and verify the worst-case interrupt rate. A periodic timer and an atomic count snapshot can support speed reporting. UART framing, signed count width, update period and fault handling remain firmware design decisions.

## What remains to finalize

Confirm motor and disk geometry; complete commercial comparisons with exact prices and photos; finalize the power adapter and package/footprint choices; capture the actual MCC pin/peripheral configuration; and obtain teaching-team feedback on the amplifier/filter design. The [BOM](../03-BOM/BOM.md) lists the components currently drawn.
