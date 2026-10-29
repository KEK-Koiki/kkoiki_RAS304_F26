---
title: Bill of Materials
---

# Bill of Materials

The purchasing examples below translate the **Revision B encoder schematic** into a priced parts list for one two-motor encoder subsystem. They include four off-board optical sensors, and count each multi-unit IC as one physical package. Fuse/holder and jumper/shunt are listed separately so those small but necessary pieces are not missed.

<div class="meta"><span>1 encoder subsystem</span><span>USD · quantity-one reference prices</span><span>Sources reviewed October 28, 2026</span></div>

## Cost at a glance

<div class="stat-grid"><div class="stat"><b>${{SUBTOTAL}}</b><span>Sourced parts subtotal</span></div><div class="stat"><b>${{CORE_TOTAL}}</b><span>Controller + sensors + ICs</span></div><div class="stat"><b>${{PASSIVE_TOTAL}}</b><span>Resistors + capacitors</span></div><div class="stat"><b>${{INTERFACE_TOTAL}}</b><span>Connectors + protection + debug</span></div></div>

Each line uses the supplier page's **one-piece unit price multiplied by the quantity needed**, without assuming volume discounts. These are dated reference prices, not a checkout quotation. Shipping, taxes, tariffs, custom PCBs, assembly, Nano sockets, mating cables, disk/bracket fabrication and thermal hardware are excluded. The optional adapter is listed separately below.

[Download priced BOM CSV](encoder-revb-bom.csv){.download} [Download sourcing record](encoder-parts-sources.json){.download} [Download KiCad project](../04-Schematic/Team103_Encoder_EK_Project.zip){.download}

## Core electronics

{{CORE_TABLE}}

## Resistors and capacitors

{{PASSIVE_TABLE}}

*Resistor photos are representative of the YAGEO CFR axial family; band colors vary with resistance. Supplier capacitor images can also represent a family. The printed MPN, electrical value and dimensional drawing govern selection.*

## Connectors, protection and debug

{{INTERFACE_TABLE}}

## External power example

{{ADAPTER_TABLE}}

Adding this adapter gives an illustrative **${{WITH_ADAPTER}} parts-plus-adapter subtotal**, before the exclusions above. Its AC input cord is sold separately. Check its 5.5 × 2.1 mm center-positive plug against the chosen jack and confirm the mains cord needed locally. This adapter's 2 A rating is available capacity; it does not mean the encoder consumes 2 A or resolves regulator heating.

## Fit, sourcing and assembly notes

{{FIT_NOTES}}

## Items still requiring a quote or team decision

| Item | Quantity / scope | Why it is outside the priced subtotal |
| --- | --- | --- |
| Nano carrier sockets | Two 1 × 28 receptacles; example Sullins PPPC281LFBN-RC | Confirm stack height, footprint and current small-quantity quote. |
| Sensor cables and mates | Four three-conductor assemblies | Length, strain relief, connector polarization and motor placement remain open. |
| Ribbon cable and IDC mate | Team cable assembly | Final connector orientation, length and signal allocation are deferred. |
| Encoder disks and brackets | Two disks / four sensor mounts | Shaft diameter, slots and clearances depend on the selected motors. |
| Regulator heatsink / hardware | As required by thermal measurements | TO-220 fit, airflow and temperature rise must be checked. |
| Custom encoder PCB and mounting hardware | One board | Layout is not yet complete; obtain fabrication/assembly pricing later. |
| Motors | Two, on the driver subsystem | Team-selected actuation hardware; excluded from this individual encoder BOM. |

## Photo credits and selection status

Reference product images are supplied by the linked manufacturers through DigiKey; attribution and original image URLs are retained in the sourcing record. Images are hosted locally for reliable display. Photographs show purchasing examples, not parts already owned or assembled. New support-component MPNs are **fit-check candidates**; they do not imply assigned or verified PCB footprints.

**Revision B consistency:** C11 is 100 nF in the exported netlist. With R19 = 10 kΩ, the nominal time constant is 1 ms. Resolve the older 10 ms annotation before fabrication. No schematic electrical values were changed during this website refinement.
