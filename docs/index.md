---
title: Motor Encoder Subsystem
---


<div class="hero" markdown>
<div class="eyebrow">RAS304 · Fall 2026 · Team 103</div>

# Giving ordinary motors a sense of position.

Elijah Koiki's motor encoder subsystem for the **2 DOF Smart Robot Arm Joint Showcase**. Four optical channels turn the motion of two DC motor shafts into position and direction feedback for a distributed embedded control system.

<a class="button" href="04-Schematic/schematic/">Explore the schematic →</a>
<a class="button secondary" href="01-Block-Diagram/Block-Diagram/">Follow the signal path</a>
</div>

<div class="meta"><span>Elijah Koiki</span><span>Team 103</span><span>Arizona State University</span><span>Updated October 28, 2026</span></div>

## Project summary

Team 103 is developing a modular, computer-connected control system for a two-degree-of-freedom robotic arm. Custom PCBs add sensing, communication and motor control to basic DC motors rated no higher than 12 V. My board measures both shafts using optical quadrature encoders, conditions their signals, and uses a PIC18F57Q43 Curiosity Nano to prepare feedback for the main controller. This feedback is intended to support the team's closed-loop motion control and telemetry. See the [Team 103 report](https://ras304-f26-103.github.io/) for the wider system.

<div class="stat-grid"><div class="stat"><b>2</b><span>Motor shafts monitored</span></div><div class="stat"><b>4</b><span>Optical A/B channels</span></div><div class="stat"><b>5 V</b><span>Local logic supply</span></div><div class="stat"><b>Rev B</b><span>ERC-reviewed schematic</span></div></div>

## My contribution

I am responsible for the **motor encoder subsystem**: shaft sensing, analog filtering and amplification, digital edge conditioning, local power regulation, and the encoder PIC's connection to the main board. Connor's main board receives the proposed feedback link; Walker's motor driver board controls motor power. Encoder firmware and physical integration are the next implementation steps.

![Updated two-motor encoder block diagram](01-Block-Diagram/encoder-block-diagram.png)

## Explore the design

<div class="cards" markdown>
<div class="card" markdown><div class="number">01 / ARCHITECTURE</div>
### [Block diagram](01-Block-Diagram/Block-Diagram.md)
Trace motion through optical sensing, conditioning, the PIC and the proposed team connection.
</div>
<div class="card" markdown><div class="number">02 / DESIGN CHOICES</div>
### [Component selection](02-Component-Selection/Component-Selection.md)
Compare sensing and circuit options, then review the PIC pin and peripheral plan.
</div>
<div class="card" markdown><div class="number">03 / MATERIALS</div>
### [Bill of materials](03-BOM/BOM.md)
Review the parts extracted from the actual Revision B schematic, including off-board sensors.
</div>
<div class="card" markdown><div class="number">04 / CIRCUIT DESIGN</div>
### [Schematic](04-Schematic/schematic.md)
Inspect the embedded schematic and download its high-resolution PDF and editable KiCad project.
</div>
<div class="card" markdown><div class="number">05 / POWER</div>
### [Power budget](05-Power-Budget/Power-Budget.md)
Review a transparent planning estimate, the 25% margin, and the regulator's thermal limits.
</div>
<div class="card" markdown><div class="number">06 / DESIGN REVIEW</div>
### [Review & resources](Appendix/index.md)
Find verification evidence, outstanding decisions, primary references and the review walkthrough.
</div>
</div>

<div class="status" markdown>
**Current maturity:** Revision B passed KiCad 10.0.7 ERC with zero reported errors and warnings on October 27. Motor mounting, optical performance, firmware, final ribbon agreement and hardware tests remain open. This site presents the documented design and its limits; fabrication approval is pending.
</div>
