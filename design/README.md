# Editable engineering sources

- `diagrams/encoder.svg`: the readable, editable master for the approved simple connection diagram. Open it in Inkscape or another SVG editor; labels and geometry can also be edited as XML.
- `ecad/encoder-revb/Team103_Encoder_EK.kicad_pro`: open in KiCad with the neighboring symbol library and library table. The reviewed electrical source has not been altered by repository organization.
- Published PNG/PDF/ZIP exports remain beside their assignment pages in `docs/` to preserve existing URLs.

After editing the diagram, run `npm run diagram:export`. It refreshes both existing public image aliases and the source ZIP. No web page text is overwritten. See `EDITING.md` for schematic export instructions.
