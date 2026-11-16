---
title: Review & Resources
---

# Review & Resources

## Current design record

The current design is Revision D. Earlier optical-sensor artwork and prices are superseded. The [schematic](../04-Schematic/schematic.md) and [PCB Design](../06-PCB-Design/PCB-Design.md) pages identify the current electrical and fabrication files.

## Before release

- Check the actual parts against the 1:1 print, especially jack, fuse clips, Nano sockets and regulator.
- Confirm teacher approval scope for the integrated encoder and unity-buffer analog path, and the instructor's manufacturing stackup.
- Review real KiCad and JLCDFM evidence for this exact Gerber ZIP.
- Verify 5 V UART compatibility and physical IDC numbering with the main-board owner.
- Measure 5 V regulation, current and regulator temperature before connecting the Nano and encoders.
- Verify both motors' encoder wire functions and pulses per revolution; check clean A/B transitions and firmware direction.
- Review costs with class-stock exclusions and approve the order explicitly.

## Primary references

- [Teacher's exact motor](https://www.robotshop.com/products/e-s-motor-25dx54l-12v-gear-motor-with-magnetic-encoder-108-rpm)
- [Supplier encoder wiring attachment](https://cdn.robotshop.com/rbm/a00a7635-653b-4220-aac9-b0c23c5c5e2c/7/7ef8b36b-a206-40b0-a32b-885875d30965/ba82ad34_25SG-370CA-encoder.pdf) — contains conflicting pulse-count information relative to the listing.
- [Microchip Nano hardware guide](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/UserGuides/PIC18F57Q43-Curiosity-Nano-HW-UserGuide-DS40002186B.pdf)
- [TI HC14 datasheet](https://www.ti.com/lit/ds/symlink/sn74hc14.pdf)
- [MCP6004 datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP6001-1R-1U-2-4-1-MHz-Low-Power-Op-Amp-DS20001733L.pdf)

Revision D is an engineering review design. Electrical bench tests and component fit checks remain pending. KiCad checks do not prove a working physical board. No order has been placed.
