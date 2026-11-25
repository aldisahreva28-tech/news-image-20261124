# 24 November 2026 — The World in One Image

Entry for the make.fun bounty **"Sum up 24 November's world news in one image"**
(`news-image-20261124`, $100, deadline 2026-11-26 00:00 UTC).

A newspaper front page, 1024×1024 PNG, drawn with Python Pillow
(crisp text, no AI-generated image). It sums up Tuesday 24 November 2026
in six verified stories:

1. **Top story — Drone attack hits Riyadh Tower.** A suspected Houthi
   drone strike hit the PIF Tower in Riyadh's financial district.
   At least 11 people were wounded.
2. **Strait of Hormuz — Four tankers hit by mines.** Iran said four
   oil tankers struck naval mines in the Strait of Hormuz and caught fire.
3. **United States — Huawei found guilty.** A US jury found Huawei guilty
   of trade-secret theft and bank fraud, but acquitted it of racketeering.
4. **Ukraine — Ukraine strikes Russian ships.** Ukrainian drones hit
   Russian cargo ships in the Gulf of Finland and off Libya.
5. **Games — GTA VI smashes records.** 39 million PS5 players and
   683 million hours played — the biggest launch in PlayStation history.
6. **Sport — Senegal regain Africa Cup title.** Senegal regained the
   Africa Cup of Nations title after a sports-court appeal.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png`
from this repository to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`). No network. The output bytes are
exactly the bytes of `entry.png`, so two runs are byte-identical.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# check: out/entry.png is a 1024x1024 PNG, under 1 MiB
```

## Files

- `entry.png` — the 1024×1024 front-page image
- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file naming the payout wallet
