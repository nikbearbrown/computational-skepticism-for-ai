// wrap-captions.mjs — split overflowing single-line caption <text> elements into
// multiple separate <text> lines that fit the canvas width. Uses the SAME width
// metric as svg-visual-audit.mjs so wrapped output passes the static scan.
// Usage: node SCRIPTS/wrap-captions.mjs <file1.svg> <file2.svg> ...
import { readFileSync, writeFileSync } from 'fs';

const NARROW = new Set("iIl.,:;'|!ftrj()[]-/ ");
const WIDE   = new Set("mwMW@");
const UPPER  = new Set("ABCDEFGHJKLNOPQRSTUVXYZ");
const charEm = c => NARROW.has(c) ? 0.30 : WIDE.has(c) ? 0.88 : UPPER.has(c) ? 0.66 : /[0-9]/.test(c) ? 0.55 : 0.52;
const textW  = (s, fs, ls = 0) => [...s].reduce((a, c) => a + charEm(c) * fs, 0) + Math.max(0, s.length - 1) * ls;
const decode = s => s.replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&#39;/g,"'").replace(/&#8217;/g,"’").replace(/&#8212;/g,'—').replace(/&#8211;/g,'–').replace(/&#8220;/g,'“').replace(/&#8221;/g,'”').replace(/&amp;/g,'&');
const num = (v,d=0)=>{const n=parseFloat(String(v??'').replace(/[a-z%]+$/i,''));return Number.isFinite(n)?n:d;};
const attr = (tag,name)=>{const m=tag.match(new RegExp(`${name}\\s*=\\s*"([^"]*)"`));return m?m[1]:null;};

const MIN_LEN = 118;   // only wrap genuinely-long caption text
const RIGHT_PAD = 10;  // px of right margin to keep

let changed = 0;
for (const file of process.argv.slice(2)) {
  let svg = readFileSync(file, 'utf8');
  const vw = num((attr(svg.match(/<svg[^>]*>/i)?.[0]||'','viewBox')||'0 0 700 420').trim().split(/\s+/)[2], 700);
  let fileChanged = false;
  svg = svg.replace(/<text\b([^>]*)>([\s\S]*?)<\/text>/g, (full, attrs, inner) => {
    if (/transform\s*=/.test(attrs)) return full;
    if (/<tspan/i.test(inner)) return full;           // skip already-structured text
    const plain = decode(inner.replace(/<[^>]*>/g,'')).trim();
    if (plain.length < MIN_LEN) return full;
    const fs = num(attr('<t '+attrs+'>','font-size'), 12);
    const x  = num(attr('<t '+attrs+'>','x'), 0);
    const ls = num(attr('<t '+attrs+'>','letter-spacing'), 0);
    const maxW = vw - x - RIGHT_PAD;
    if (textW(plain, fs, ls) <= maxW) return full;     // already fits
    // greedy word wrap on the RAW inner (preserve entities), measure on decoded
    const tokens = inner.replace(/<[^>]*>/g,'').trim().split(/ +/);
    const lines = []; let cur = '';
    for (const t of tokens) {
      const cand = cur ? cur + ' ' + t : t;
      if (textW(decode(cand), fs, ls) <= maxW || !cur) cur = cand;
      else { lines.push(cur); cur = t; }
    }
    if (cur) lines.push(cur);
    if (lines.length < 2) return full;
    const y  = num(attr('<t '+attrs+'>','y'), 0);
    const lh = Math.round(fs * 1.4);
    fileChanged = true;
    return lines.map((ln, i) => {
      const a = attrs.replace(/\by="[^"]*"/, `y="${y + i*lh}"`);
      return `<text${a}>${ln}</text>`;
    }).join('\n  ');
  });
  if (fileChanged) { writeFileSync(file, svg, 'utf8'); changed++; console.log('wrapped: ' + file.split('/').pop()); }
  else console.log('no change: ' + file.split('/').pop());
}
console.log(`\nwrapped ${changed} file(s).`);
