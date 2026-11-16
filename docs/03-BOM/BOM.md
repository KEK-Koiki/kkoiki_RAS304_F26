---
title: Bill of Materials
---

# Bill of Materials

Revision D replaces the obsolete optical-sensor BOM. This list is extracted from the current KiCad netlist and counts one physical package per IC. Test pads and board-only mounting holes are excluded from purchasing rows. Two teacher-supplied integrated-encoder motors are off-board.

<div class="meta"><span>1 two-motor encoder PCB</span><span>Revision D · November 15, 2026</span><span>Class-stock and quote review pending</span></div>

## Cost and purchasing status

The previous $38.95 optical BOM is superseded and must not be used as this board's cost. The course budget is $60 per member with the stated class-supplied exclusions. Actual class stock, sockets, fuse hardware, harnesses, any heatsink, shipping and taxes must be reconciled before a budget pass can be claimed. Motors are teacher-supplied; no motor purchase is proposed. No order is authorized by this page.

[Download current board BOM CSV](BOM_RevD.csv){.download} [KiCad project and fabrication files](../06-PCB-Design/PCB-Design.md){.download}

## Board components

<div class="bom-table" markdown>

| Reference | Qty | Value | Selected footprint / assembly note |
| --- | ---: | --- | --- |
| A1 | 1 | PIC18F57Q43 CURIOSITY NANO | `EK:EK_CuriosityNano_2x28_15.24mm` Two 1x28 female sockets plus existing Nano module; verify actual fit |
| C1 | 1 | 330nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C2 | 1 | 100nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C3 | 1 | 10uF / 25V | `Capacitor_THT:CP_Radial_D5.0mm_P2.00mm`  |
| C4 | 1 | 1nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C5 | 1 | 1nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C6 | 1 | 1nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C7 | 1 | 1nF | `Capacitor_SMD:C_0805_2012Metric`  |
| C8 | 1 | 100nF | `Capacitor_SMD:C_0805_2012Metric` BOTTOM SIDE |
| C9 | 1 | 100nF | `Capacitor_SMD:C_0805_2012Metric` BOTTOM SIDE |
| C10 | 1 | 100nF | `Capacitor_SMD:C_0805_2012Metric` BOTTOM SIDE |
| C11 | 1 | 1uF | `Capacitor_SMD:C_0805_2012Metric`  |
| C12 | 1 | 10uF / 25V | `Capacitor_THT:CP_Radial_D5.0mm_P2.00mm`  |
| C13 | 1 | 10uF / 25V | `Capacitor_THT:CP_Radial_D5.0mm_P2.00mm`  |
| D1 | 1 | GREEN / POWER | `EK:EK_LED_D3.0mm_A1K2` Footprint uses pin1 ANODE / pin2 CATHODE |
| D2 | 1 | YELLOW | `EK:EK_LED_D3.0mm_A1K2` Footprint uses pin1 ANODE / pin2 CATHODE |
| F1 | 1 | 500mA FAST / 5x20mm | `Fuse:Fuseholder_Clip-5x20mm_Littelfuse_111_Inline_P20.00x5.00mm_D1.05mm_Horizontal` Two Littelfuse 111-style clips plus 500mA fast 5x20mm fuse; verify class hardware |
| J1 | 1 | PJ-102AH / 9V CENTER + | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal`  |
| J2 | 1 | MOTOR 1 ENCODER / SCREW | `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-4-5.08_1x04_P5.08mm_Horizontal`  |
| J3 | 1 | MOTOR 2 ENCODER / SCREW | `TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-4-5.08_1x04_P5.08mm_Horizontal`  |
| J6 | 1 | 2x4 IDC / TEAM BUS | `Connector_IDC:IDC-Header_2x04_P2.54mm_Vertical`  |
| J7 | 1 | SPARE GPIO | `Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical`  |
| JP1 | 1 | TX ENABLE | `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`  |
| R1 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R2 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R3 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R6 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R7 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R10 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R11 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R14 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R15 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R18 | 1 | 1k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R19 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R20 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| R21 | 1 | 10k | `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal`  |
| SW1 | 1 | DEBUG / N.O. | `Button_Switch_THT:SW_PUSH_6mm`  |
| U1 | 1 | HTC LM7805 / TO-220 | `Package_TO_SOT_THT:TO-220-3_Vertical` User marking HTC LM7805 317; verify TO-220 and heatsink |
| U2 | 1 | MCP6004 | `Package_DIP:DIP-14_W7.62mm`  |
| U3 | 1 | SN74HC14N | `Package_DIP:DIP-14_W7.62mm`  |

</div>

## Assembly extras and fit checks

A1 needs two 1×28 female sockets plus the existing Nano. F1 needs two compatible clips and one cartridge fuse. JP1 needs a shunt. Add two encoder harnesses, the keyed 8-conductor team cable, mounting standoffs and any required regulator heatsink. J1 is selected as CUI PJ-102AH; the supplied adapter photo does not confirm voltage, polarity or 2.1 mm inner size. Verify the real class parts against the [1:1 print](../06-PCB-Design/Team103_Encoder_RevD_1to1_Fit_Check.pdf) before release. C8/C9/C10 are bottom-side 0805 capacitors. LEDs use custom pin 1 anode / pin 2 cathode footprints.
