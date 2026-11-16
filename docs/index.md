---
title: Motor Encoder Subsystem
---


<div class="hero" markdown>
<div class="eyebrow">RAS304 · Fall 2026 · Team 103</div>

# Giving ordinary motors a sense of position.

Elijah Koiki's motor encoder subsystem for the **2 DOF Smart Robot Arm Joint Showcase**. Four magnetic encoder channels turn the motion of two DC motor shafts into position and direction feedback for a distributed embedded control system.

<a class="button" href="04-Schematic/schematic/">Explore the schematic →</a>
<a class="button secondary" href="01-Block-Diagram/Block-Diagram/">Follow the signal path</a>
</div>

<div class="meta"><span>Elijah Koiki</span><span>Team 103</span><span>Arizona State University</span><span>Updated November 15, 2026</span></div>

## Project summary

Team 103 is developing a modular, computer-connected control system for a two-degree-of-freedom robotic arm. Custom PCBs add sensing, communication and motor control to basic DC motors rated no higher than 12 V. My board measures both shafts using the teacher-supplied integrated magnetic quadrature encoders, conditions their signals, and uses a PIC18F57Q43 Curiosity Nano to prepare feedback for the main controller. This feedback is intended to support the team's closed-loop motion control and telemetry. See the [Team 103 report](https://ras304-f26-103.github.io/) for the wider system.

<div class="stat-grid"><div class="stat"><b>2</b><span>Motor shafts monitored</span></div><div class="stat"><b>4</b><span>Encoder A/B channels</span></div><div class="stat"><b>5 V</b><span>Local logic supply</span></div><div class="stat"><b>Rev D</b><span>Routed review design</span></div></div>

## My contribution

I am responsible for the **motor encoder subsystem**: shaft sensing, RC filtering and op-amp buffering, digital edge conditioning, local power regulation, and the encoder PIC's connection to the main board. Connor's main board receives the proposed feedback link; Walker's motor driver board controls motor power. Encoder firmware and physical integration are the next implementation steps.

![Updated two-motor encoder block diagram](01-Block-Diagram/encoder-revd.svg)

## Explore the design

<div class="cards" markdown>
<div class="card" markdown><div class="number">01 / ARCHITECTURE</div>
### [Block diagram](01-Block-Diagram/Block-Diagram.md)
Trace motion through magnetic sensing, conditioning, the PIC and the proposed team connection.
</div>
<div class="card" markdown><div class="number">02 / DESIGN CHOICES</div>
### [Component selection](02-Component-Selection/Component-Selection.md)
Compare sensing and circuit options, then review the PIC pin and peripheral plan.
</div>
<div class="card" markdown><div class="number">03 / MATERIALS</div>
### [Bill of materials](03-BOM/BOM.md)
Review the parts extracted from the current Revision D schematic, including encoder harnesses.
</div>
<div class="card" markdown><div class="number">04 / CIRCUIT DESIGN</div>
### [Schematic](04-Schematic/schematic.md)
Inspect the embedded schematic and download its high-resolution PDF; editable files are on the PCB page.
</div>
<div class="card" markdown><div class="number">05 / POWER</div>
### [Power budget](05-Power-Budget/Power-Budget.md)
Review a transparent planning estimate, the 25% margin, and the regulator's thermal limits.
</div>
<div class="card" markdown><div class="number">06 / PCB LAYOUT</div>
### [PCB Design](06-PCB-Design/PCB-Design.md)
Review the routed board, Gerbers, KiCad package and submission requirements.
</div>
<div class="card" markdown><div class="number">07 / DESIGN REVIEW</div>
### [Review & resources](Appendix/index.md)
Find verification evidence, outstanding decisions, primary references and the review walkthrough.
</div>
</div>

<div class="status" markdown>
**Current maturity:** Revision D is an engineering review design. Electrical bench tests and component fit checks remain pending. KiCad checks do not prove a working physical board. No order has been placed. The new [PCB Design page](06-PCB-Design/PCB-Design.md) holds the current fabrication and review files.
</div>
