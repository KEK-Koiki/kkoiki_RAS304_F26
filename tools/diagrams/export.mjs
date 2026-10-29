/** Render the editable SVG; never overwrite page text. */
import fs from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import sharp from 'sharp';

const root=new URL('../../',import.meta.url);
const source=new URL('design/diagrams/encoder.svg',root);
const destination=new URL('docs/01-Block-Diagram/',root);
const svg=await fs.readFile(source);
const png=await sharp(svg,{density:144}).png().toBuffer();
const check=process.argv.includes('--check');
if(check){
  const existing=await fs.readFile(new URL('encoder-detailed-block-diagram.png',destination));
  const a=await sharp(png).raw().toBuffer();
  const b=await sharp(existing).raw().toBuffer();
  if(!a.equals(b))throw new Error('SVG master and published PNG differ. Run npm run diagram:export after reviewing the master.');
  console.log('SVG master matches the published diagram pixels.');
}else{
  for(const name of ['encoder-block-diagram','encoder-detailed-block-diagram']){
    await fs.writeFile(new URL(name+'.svg',destination),svg);
    await fs.writeFile(new URL(name+'.png',destination),png);
  }
  const python=process.env.PYTHON||'python';
  execFileSync(python,[fileURLToPath(new URL('tools/diagrams/package.py',root))],{stdio:'inherit'});
  console.log('Exported diagram images and source ZIP.');
}
