// lift-captions.mjs — fix caption/chart vertical collisions by lifting the long
// tspan-wrapped caption up under the title and tightening its line spacing so all
// lines clear the chart (plot rect top ~y=102). Touches ONLY the caption <text>.
// Usage: node SCRIPTS/lift-captions.mjs <file.svg> ...
import { readFileSync, writeFileSync } from 'fs';

let changed = 0;
for (const file of process.argv.slice(2)) {
  let svg = readFileSync(file, 'utf8');
  let did = false;
  svg = svg.replace(/<text\b([^>]*)>([\s\S]*?)<\/text>/g, (full, attrs, inner) => {
    const plain = inner.replace(/<[^>]*>/g, '').trim();
    if (plain.length < 118) return full;            // captions only
    if (!/<tspan/i.test(inner)) return full;         // only tspan-wrapped ones (single-line handled by wrap-captions)
    const y = parseFloat((attrs.match(/\by="([^"]*)"/) || [])[1]);
    if (!(y >= 70 && y <= 90)) return full;          // only the y≈78 colliding template
    // lift caption up under the title, shrink font, tighten line spacing
    let a = attrs.replace(/\by="[^"]*"/, 'y="64"');
    if (/font-size="[^"]*"/.test(a)) a = a.replace(/font-size="[^"]*"/, 'font-size="9"');
    else a = a + ' font-size="9"';
    const inner2 = inner.replace(/dy="(\d+(?:\.\d+)?)"/g, (m, n) => (parseFloat(n) >= 13 ? 'dy="11"' : m));
    did = true;
    return `<text${a}>${inner2}</text>`;
  });
  if (did) { writeFileSync(file, svg, 'utf8'); changed++; console.log('lifted: ' + file.split('/').pop()); }
  else console.log('no change: ' + file.split('/').pop());
}
console.log(`\nlifted ${changed} file(s).`);
