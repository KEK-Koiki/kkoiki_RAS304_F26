---
title: Component Selection
---


# Component Selection

The current choices follow the revised **two-motor optical encoder subsystem**. These comparison tables explain engineering tradeoffs; choices already drawn in Revision B are distinguished from alternatives and decisions awaiting physical measurements.

## Selected parts at a glance

These are example orderable versions of the components already drawn in Revision B. Prices are **USD per piece at the supplier's quantity-one tier**, reviewed October 28, 2026. The four sensors therefore cost four times the displayed sensor unit price. The [detailed BOM](../03-BOM/BOM.md) includes quantities, line totals, passives, connectors and fit-check notes.

<div class="component-cards" markdown>
<div class="component-card" markdown>
<img src="../../static/parts/nano.jpg" alt="DM164150 supplier reference photo" width="160" loading="lazy">
<div class="number">A1 · 1 piece</div>
### DM164150
PIC18F57Q43 Curiosity Nano

**$10.61 each · $10.61 extended**

[Supplier & price](https://www.digikey.com/en/products/detail/microchip-technology/DM164150/11586705) · [Manufacturer documentation](https://www.digikey.com/en/products/detail/microchip-technology/DM164150/11586705)
</div>
<div class="component-card" markdown>
<img src="../../static/parts/tcst2103.jpg" alt="TCST2103 supplier reference photo" width="160" loading="lazy">
<div class="number">Q1–Q4 · 4 pieces</div>
### TCST2103
Bare optical interrupter, 3.1 mm slot

**$1.84 each · $7.36 extended**

[Supplier & price](https://www.digikey.com/en/products/detail/vishay-semiconductor-opto-division/TCST2103/2354849) · [Manufacturer documentation](https://www.vishay.com/docs/81147/tcst2103.pdf)
</div>
<div class="component-card" markdown>
<img src="../../static/parts/mcp6004.jpg" alt="MCP6004-I/P supplier reference photo" width="160" loading="lazy">
<div class="number">U2 · 1 piece</div>
### MCP6004-I/P
Quad rail-to-rail op-amp, PDIP-14

**$0.60 each · $0.60 extended**

[Supplier & price](https://www.digikey.com/en/products/detail/MCP6004-I%2FP/MCP6004-I%2FP-ND/523060) · [Manufacturer documentation](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf)
</div>
<div class="component-card" markdown>
<img src="../../static/parts/hc14.jpg" alt="SN74HC14N supplier reference photo" width="160" loading="lazy">
<div class="number">U3 · 1 piece</div>
### SN74HC14N
Hex Schmitt inverter, PDIP-14

**$1.15 each · $1.15 extended**

[Supplier & price](https://www.digikey.com/en/products/detail/texas-instruments/SN74HC14N/277223) · [Manufacturer documentation](https://www.digikey.com/en/products/detail/texas-instruments/SN74HC14N/277223)
</div>
<div class="component-card" markdown>
<img src="../../static/parts/l7805.jpg" alt="L7805ACV supplier reference photo" width="160" loading="lazy">
<div class="number">U1 · 1 piece</div>
### L7805ACV
5 V linear regulator, TO-220

**$1.22 each · $1.22 extended**

[Supplier & price](https://www.digikey.com/en/products/detail/stmicroelectronics/L7805ACV/585962) · [Manufacturer documentation](https://www.st.com/content/ccc/resource/technical/document/datasheet/41/4f/b3/b0/12/d4/47/88/CD00000444.pdf/files/CD00000444.pdf/jcr%3Acontent/translations/en.CD00000444.pdf)
</div>
<div class="component-card" markdown>
<img src="../../static/parts/adapter.jpg" alt="GST18A09-P1J supplier reference photo" width="160" loading="lazy">
<div class="number">EXTERNAL POWER · PURCHASING CANDIDATE</div>
### GST18A09-P1J
9 V / 2 A desktop supply; input cord sold separately.

**$14.10 each**

[Supplier & price](https://www.digikey.com/en/products/detail/mean-well-usa-inc/GST18A09-P1J/7703606) · [Datasheet](https://www.meanwellusa.com/upload/pdf/GST18A/GST18A-spec.pdf)
</div>
</div>

*Product images: manufacturer reference photos via the linked DigiKey listings. Images are representative; confirm suffix, package and dimensions from the datasheet. This sourcing pass does not establish final mounting or team interface approval.*

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

Confirm motor and disk geometry; complete the remaining alternative-product comparisons and recheck supplier prices before ordering; finalize the power adapter and package/footprint choices; capture the actual MCC pin/peripheral configuration; and obtain teaching-team feedback on the amplifier/filter design. The [BOM](../03-BOM/BOM.md) lists the components currently drawn.
