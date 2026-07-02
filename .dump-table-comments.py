import re, os
from pathlib import Path
ch = Path('chapters')
for f in sorted(ch.glob('*.md')):
    t = f.read_text()
    matches = list(re.finditer(r'<!--\s*→\s*\[TABLE:([^]]*?)(?:\]\s*-->|-->)', t, re.DOTALL))
    for m in matches:
        line = t[:m.start()].count('\n') + 1
        desc = m.group(1).strip()
        print(f"\n=== {f.name} L{line} ===")
        print(desc)
