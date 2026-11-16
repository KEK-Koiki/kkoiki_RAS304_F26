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
| A1 | 1 | PIC18F57Q43 CURIOSITY NANO | `EK:RevD_A1` Two 1x28 female sockets plus existing Nano module; verify actual fit; Base geometry: EK:EK_CuriosityNano_2x28_15.24mm |
| C1 | 1 | 330nF | `EK:RevD_C1` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C2 | 1 | 100nF | `EK:RevD_C2` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C3 | 1 | 10uF / 25V | `EK:RevD_C3` ; Base geometry: Capacitor_THT:CP_Radial_D5.0mm_P2.00mm |
| C4 | 1 | 1nF | `EK:RevD_C4` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C5 | 1 | 1nF | `EK:RevD_C5` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C6 | 1 | 1nF | `EK:RevD_C6` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C7 | 1 | 1nF | `EK:RevD_C7` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C8 | 1 | 100nF | `EK:RevD_C8` BOTTOM SIDE; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C9 | 1 | 100nF | `EK:RevD_C9` BOTTOM SIDE; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C10 | 1 | 100nF | `EK:RevD_C10` BOTTOM SIDE; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C11 | 1 | 1uF | `EK:RevD_C11` ; Base geometry: Capacitor_SMD:C_0805_2012Metric |
| C12 | 1 | 10uF / 25V | `EK:RevD_C12` ; Base geometry: Capacitor_THT:CP_Radial_D5.0mm_P2.00mm |
| C13 | 1 | 10uF / 25V | `EK:RevD_C13` ; Base geometry: Capacitor_THT:CP_Radial_D5.0mm_P2.00mm |
| D1 | 1 | GREEN / POWER | `EK:RevD_D1` Footprint uses pin1 ANODE / pin2 CATHODE; Base geometry: EK:EK_LED_D3.0mm_A1K2 |
| D2 | 1 | YELLOW | `EK:RevD_D2` Footprint uses pin1 ANODE / pin2 CATHODE; Base geometry: EK:EK_LED_D3.0mm_A1K2 |
| F1 | 1 | 500mA FAST / 5x20mm | `EK:RevD_F1` Two Littelfuse 111-style clips plus 500mA fast 5x20mm fuse; verify class hardware; Base geometry: Fuse:Fuseholder_Clip-5x20mm_Littelfuse_111_Inline_P20.00x5.00mm_D1.05mm_Horizontal |
| J1 | 1 | PJ-102AH / 9V CENTER + | `EK:RevD_J1` ; Base geometry: Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal |
| J2 | 1 | MOTOR 1 ENCODER / SCREW | `EK:RevD_J2` ; Base geometry: TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-4-5.08_1x04_P5.08mm_Horizontal |
| J3 | 1 | MOTOR 2 ENCODER / SCREW | `EK:RevD_J3` ; Base geometry: TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-4-5.08_1x04_P5.08mm_Horizontal |
| J6 | 1 | 2x4 IDC / TEAM BUS | `EK:RevD_J6` ; Base geometry: Connector_IDC:IDC-Header_2x04_P2.54mm_Vertical |
| J7 | 1 | SPARE GPIO | `EK:RevD_J7` ; Base geometry: Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |
| JP1 | 1 | TX ENABLE | `EK:RevD_JP1` ; Base geometry: Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical |
| R1 | 1 | 1k | `EK:RevD_R1` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R2 | 1 | 10k | `EK:RevD_R2` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R3 | 1 | 1k | `EK:RevD_R3` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R6 | 1 | 10k | `EK:RevD_R6` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R7 | 1 | 1k | `EK:RevD_R7` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R10 | 1 | 10k | `EK:RevD_R10` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R11 | 1 | 1k | `EK:RevD_R11` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R14 | 1 | 10k | `EK:RevD_R14` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R15 | 1 | 1k | `EK:RevD_R15` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R18 | 1 | 1k | `EK:RevD_R18` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R19 | 1 | 10k | `EK:RevD_R19` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R20 | 1 | 10k | `EK:RevD_R20` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| R21 | 1 | 10k | `EK:RevD_R21` ; Base geometry: Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal |
| SW1 | 1 | DEBUG / N.O. | `EK:RevD_SW1` ; Base geometry: Button_Switch_THT:SW_PUSH_6mm |
| U1 | 1 | HTC LM7805 / TO-220 | `EK:RevD_U1` User marking HTC LM7805 317; verify TO-220 and heatsink; Base geometry: Package_TO_SOT_THT:TO-220-3_Vertical |
| U2 | 1 | MCP6004 | `EK:RevD_U2` ; Base geometry: Package_DIP:DIP-14_W7.62mm |
| U3 | 1 | SN74HC14N | `EK:RevD_U3` ; Base geometry: Package_DIP:DIP-14_W7.62mm |

</div>

## Assembly extras and fit checks

A1 needs two 1×28 female sockets plus the existing Nano. F1 needs two compatible clips and one cartridge fuse. JP1 needs a shunt. Add two encoder harnesses, the keyed 8-conductor team cable, mounting standoffs and any required regulator heatsink. J1 is selected as CUI PJ-102AH; the supplied adapter photo does not confirm voltage, polarity or 2.1 mm inner size. Verify the real class parts against the [1:1 print](../06-PCB-Design/Team103_Encoder_RevD_1to1_Fit_Check.pdf) before release. C8/C9/C10 are bottom-side 0805 capacitors. LEDs use custom pin 1 anode / pin 2 cathode footprints.
