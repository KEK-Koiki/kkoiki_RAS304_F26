# Team 103 encoder PCB — Revision D

Engineering review design, November 15, 2026. Not approved for fabrication or purchase.
Open Team103_Encoder_RevD_EK.kicad_pro in KiCad 10.0.7. Custom libraries are included.

Changes: two integrated motor encoders replace four optical interrupters; four RC/MCP6004/HC14 channels; HTC LM7805 with three pins on one side; unused HC14 inputs each pulled down; keyed 2x4 IDC, pin 1 TX, 2 RX, 8 common GND, 3–7 NC; PJ-102AH barrel input; 0.9/0.5 mm vias; inch Excellon drills.

Motor interface J2/J3: 1 +5V (blue), 2 common GND (green), 3 A (yellow), 4 B (white), according to the attachment on the teacher's exact RobotShop motor listing. Red/black motor winding wires go only to the motor driver. Confirm actual harness against sensor PCB before energizing. Attachment states 3.5–20V and <=10mA per encoder, 0-to-Vcc outputs. Its 64 counts/rev description conflicts with listing's 11PPR; calibrate firmware.

Nano: edge51 VTG=5V, edge55 VOFF=GND, edge56 VBUS=NC. USB debug/programming can be used with external power. Remove module from carrier for USB-only use. Never put input-adapter voltage onto VTG.

Verification: ERC 0 errors/0 warnings; CLI DRC 0 violations/0 unrouted/0 schematic parity; GUI DRC 0 errors/0 warnings/0 unconnected (GUI parity not run; CLI parity checked). 219 static design checks passed. Five default ignored DRC categories remain: missing courtyard, track endpoint not centered on via, tuning geometry, footprint filters, and component type mismatch. No individual DRC exclusions were used. These software checks do not establish correct physical fit, thermal performance, firmware or functional hardware.

Pending before release:
- Actual adapter label is unreadable in supplied photo. Verify 9V regulated DC, center positive and 5.5/2.1mm plug; selected PJ-102AH fit is provisional.
- Print 1:1 PDF at Actual Size and fit actual jack, fuse clips, TO220 regulator, Nano sockets, IDC, terminals and other components. Selected footprints are explicit parts, not a guarantee class inventory matches.
- General course analog rubric requires gain >1 and excludes Hall devices needing no extra conditioning. Teacher approved integrated motors, but scope of that exception for unity buffers needs confirmation. Do not claim unity gain satisfies gain >1.
- Confirm course batch-order stackup: assignment 0.5oz per side and Peralta .059in versus common JLC 1.6mm/1oz outer copper. CAD currently records 1.6mm/0.5oz.
- JLCDFM requires account login. No successful analysis or DFM proof exists yet. Do not substitute an unrelated screenshot.
- Review 5V UART compatibility, IDC orientation, encoder phase/direction and counts/rev. Firmware remains unimplemented/unverified.
- Measure regulator rail current/temperature and breadboard/bench operation. 500mA fast fuse is provisional; confirm real load and supplied clips/fuse fit.
- Update purchasing quote after class-stock inventory. Old optical BOM prices are superseded. Course budget is $60/member with class exclusions; no delivered-cost/budget pass established.
- Obtain student approval before any order. Instructor batch-order process applies. No Canvas submission or order has been made.

Submission folder contains Gerber ZIP and real KiCad screenshot. DFM screenshot is deliberately absent until actually obtained. Canvas also requires schematic and PCB URLs as comments.

Assisted design uses explicitly prescribed individual routes in routes.py; no autorouter. Student should review and understand the design before submitting coursework. Original Revision B and Revision C are preserved separately.
