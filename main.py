"""Entry for make.fun bounty news-image-20261124.

Copies the pre-built image entry.png (in this repository) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only, no network, deterministic: the output bytes
are exactly the bytes of entry.png, so two runs are identical.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
