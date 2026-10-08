# omarchy-theme-from-image

Turn any wallpaper into a complete [Omarchy](https://omarchy.org) theme with one command.

```bash
omarchy-theme-from-image ~/Pictures/wallpaper.jpg
omarchy theme set wallpaper
```

No install? Try it in your browser: https://theme-from-image.fransozzan.workers.dev (runs locally, your image never leaves your computer).

- Extracts the dominant colors and maps them to all 26 keys of an Omarchy `colors.toml`
- **Readable by design:** foreground ≥ 7:1 and every terminal color ≥ 4.5:1 contrast (WCAG AA), adjusted automatically
- Terminal colors stay recognizable (red is still red) but are tinted toward your image
- Dark by default, `--light` for a light theme
- Sets the wallpaper and a matching Yaru icon color
- No pip installs: Python 3.11+ and ImageMagick, both already on Omarchy

## Install
```bash
git clone https://github.com/FranElfers/omarchy-theme-from-image
install -Dm755 omarchy-theme-from-image/omarchy-theme-from-image ~/.local/bin/omarchy-theme-from-image
```

## Usage
```
omarchy-theme-from-image <image> [--name NAME] [--light] [--out DIR]
```
Writes to `~/.config/omarchy/themes/<name>` (the name defaults to the file name).

## Pro version
**omarchy-theme-from-image PRO** goes further:
- Dark **and** light theme from every image
- 2 extra matching 4K wallpapers per theme
- A `preview.png` for the theme picker
- Batch mode: a whole folder of wallpapers → a theme for each one

→ [Get PRO](https://francadev.gumroad.com/l/theme-from-image-pro)

## Support
[Sponsor on GitHub](https://github.com/sponsors/FranElfers) or [buy me a cafecito](https://cafecito.app/francadev) ☕

## License
MIT
