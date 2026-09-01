#!/usr/bin/env python3
"""Apply the profile's spectral palette to Metrics-generated SVGs.

Usage: style_metrics_svg.py <input.svg> <light|dark> <output.svg>

Replaces GitHub's default contribution-green ramp and neutral text colors
with the profile's spectral ramp (cyan -> purple -> orange on deep blue).
Input background is left transparent so the card adapts to the page; text
and accents are baked per theme variant.
"""
import re
import sys

# GitHub contribution levels -> spectral ramp shared with snake.yml
LIGHT = {
    "#ebedf0": "#E7EEF2",
    "#9be9a8": "#D8E9E7",
    "#40c463": "#A9EBD4",
    "#30a14e": "#55D9C0",
    "#216e39": "#7B2CBF",
    "#1f2328": "#1D3541",
    "#24292f": "#1D3541",
    "#57606a": "#4A6572",
    "#6e7781": "#4A6572",
    "#959da5": "#7A919C",
    "#777777": "#4A6572",
    "#0969da": "#345D68",
    "#0366d6": "#345D68",
    "#0a3069": "#1D3541",
}
DARK = {
    "#ebedf0": "#131D25",
    "#9be9a8": "#1D3541",
    "#40c463": "#345D68",
    "#30a14e": "#55D9C0",
    "#216e39": "#F3B36C",
    "#1f2328": "#E7EEF2",
    "#24292f": "#E7EEF2",
    "#57606a": "#9FB6C2",
    "#6e7781": "#9FB6C2",
    "#959da5": "#7A919C",
    "#777777": "#9FB6C2",
    "#0969da": "#55D9C0",
    "#0366d6": "#55D9C0",
    "#0a3069": "#E7EEF2",
}

# Any explicit page-colored background is stripped to transparent.
BACKGROUNDS = ("#ffffff", "#fff", "#0d1117")


def recolor(svg: str, palette: dict) -> str:
    if "<svg" not in svg or "</svg>" not in svg:
        raise ValueError("input is not a complete SVG")
    for source, target in sorted(palette.items(), key=lambda item: -len(item[0])):
        svg = re.sub(re.escape(source), target, svg, flags=re.IGNORECASE)
    for bg in BACKGROUNDS:
        svg = re.sub(
            r'(<rect[^>]*?fill=")' + re.escape(bg) + r'"',
            r"\1none\"", svg, flags=re.IGNORECASE)
    return svg


def main():
    src, variant, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    palette = LIGHT if variant == "light" else DARK
    with open(src, encoding="utf-8") as fh:
        out = recolor(fh.read(), palette)
    with open(dst, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    print(f"styled {src} -> {dst} ({variant})")


if __name__ == "__main__":
    main()
