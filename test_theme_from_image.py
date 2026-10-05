"""Test mínimo: python3 test_theme_from_image.py (requiere magick)."""
import importlib.machinery, importlib.util, subprocess, sys, tempfile, tomllib
from pathlib import Path

here = Path(__file__).parent
loader = importlib.machinery.SourceFileLoader("tfi", str(here / "omarchy-theme-from-image"))
spec = importlib.util.spec_from_loader("tfi", loader)
tfi = importlib.util.module_from_spec(spec)
loader.exec_module(tfi)

with tempfile.TemporaryDirectory() as t:
    img = Path(t) / "wall.png"
    # imagen con violeta, naranja y azul: obliga a teñir varios colores ANSI
    subprocess.run(["magick", "-size", "300x100", "xc:#7a3fb0", "xc:#e08a3c", "xc:#1d2b4a", "+append", str(img)], check=True)
    for light in (False, True):
        out = Path(t) / ("light" if light else "dark")
        tfi.main([str(img), "--out", str(out)] + (["--light"] if light else []))
        c = tomllib.loads((out / "colors.toml").read_text())
        assert c["mode"] == ("light" if light else "dark")
        assert (out / "backgrounds" / "1-wall.png").exists() and (out / "icons.theme").read_text().strip()
        for k in ("foreground", "bright_foreground", "light_foreground"):
            assert tfi.ratio(c[k], c["background"]) >= 7, k
        for k in [*tfi.HUES, *("bright_" + n for n in tfi.HUES if n != "orange"), "accent"]:
            assert tfi.ratio(c[k], c["background"]) >= 4.5, k
        for name, target in tfi.HUES.items():  # cada color ANSI sigue pareciéndose a su tono
            assert abs((tfi.hls(c[name])[0] - target + 180) % 360 - 180) <= 30, (name, c[name])
print("OK")
