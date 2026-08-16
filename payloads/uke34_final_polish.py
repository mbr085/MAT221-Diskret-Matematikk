#!/usr/bin/env python3
from pathlib import Path
import sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else "notes/uke34.qmd")
s = path.read_text(encoding="utf-8")

replacements = [
    (
        """Til slutt skal vi kunne skille mellom fire grunnsituasjoner:

- **Rekkefølgen teller, uten repetisjon:**""",
        """Til slutt skal vi kunne skille mellom fire grunnsituasjoner:

Her er $n$ antallet tilgjengelige objekter eller objekttyper, og $r$ antallet valg vi gjør.

- **Rekkefølgen teller, uten repetisjon:**""",
    ),
    (
        r"""$$
n(n-1)\cdots(n-r+1)=\frac{n!}{(n-r)!}.
$$
:::

Her er to ting avgjørende:""",
        r"""$$
n(n-1)\cdots(n-r+1)=\frac{n!}{(n-r)!}.
$$

Når $r=0$, tolker vi produktet på venstresiden som det tomme produktet $1$.
:::

Her er to ting avgjørende:""",
    ),
    (
        "De samme fire studentene gir altså $4!$ forskjellige resultat når rollene skiller dem fra hverandre.",
        "De samme fire studentene gir altså $4!$ forskjellige resultater når rollene skiller dem fra hverandre.",
    ),
    (
        r"""For $0\le r\le n$ gjelder

1. $\displaystyle \binom nr=\binom n{n-r}$,
2. $\displaystyle \binom{n+1}r=\binom nr+\binom n{r-1}$.""",
        r"""Vi bruker følgende to identiteter:

1. For $0\le r\le n$ gjelder $\displaystyle \binom nr=\binom n{n-r}$.
2. For $1\le r\le n$ gjelder $\displaystyle \binom{n+1}r=\binom nr+\binom n{r-1}$.""",
    ),
    (
        "1. Tre forskjellige medaljer skal fordeles blant $10$ deltakere.",
        "1. Gull, sølv og bronse skal fordeles til tre forskjellige deltakere blant $10$.",
    ),
]

for old, new in replacements:
    count = s.count(old)
    if count != 1:
        raise SystemExit(
            f"Stoppet: forventet nøyaktig ett treff, fant {count}.\n\n"
            f"Starten på teksten som ikke matchet:\n{old[:160]}"
        )
    s = s.replace(old, new)

path.write_text(s, encoding="utf-8")
print(f"Oppdatert: {path}")
