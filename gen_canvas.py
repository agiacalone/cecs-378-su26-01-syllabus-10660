#!/usr/bin/env python3
"""Render README.md → a Canvas-RCE-safe inline-styled HTML fragment.

Canvas's rich-content editor strips <head>, <style>, <script>, @font-face, and
class= attributes, but KEEPS inline style= on elements. So we pandoc the README
to an HTML fragment, then inject inline styles on the structural elements and
flatten the things Canvas can't render (frontmatter, comments, anchor nav,
<details>). Web-safe font stack; the Swiss vermilion accent is preserved inline.
"""
import re, subprocess, sys, pathlib

SRC = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "README.md")
OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "syllabus_canvas.html")

INK, ACCENT, MUTED, HAIR, PANEL = "#14130f", "#b22f12", "#6c675d", "#ddd8cb", "#f2efe6"
SANS = "'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'Courier New',monospace"

md = SRC.read_text(encoding="utf-8")

# extract serial from YAML frontmatter before stripping
serial_match = re.search(r"^serial:\s*(\S+)", md, re.MULTILINE)
SERIAL = serial_match.group(1) if serial_match else ""

# strip YAML frontmatter
md = re.sub(r"\A---\n.*?\n---\n", "", md, count=1, flags=re.DOTALL)
# strip HTML comments (template banner, term-var markers)
md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
# drop the "Jump to:" anchor-nav paragraph (Canvas heading ids differ)
md = re.sub(r"\*\*Jump to:\*\*.*?(?=\n##\s)", "", md, flags=re.DOTALL)
# flatten the <details> resources block → plain heading (Canvas support is spotty)
md = md.replace("<details>", "").replace("</details>", "")
md = re.sub(r"<summary>.*?</summary>", "", md, flags=re.DOTALL)

frag = subprocess.run(
    ["pandoc", "--from", "gfm", "--to", "html5"],
    input=md, capture_output=True, text=True, check=True,
).stdout

# h1
frag = re.sub(
    r"<h1[^>]*>(.*?)</h1>",
    rf'<h1 style="font-family:{SANS};font-size:2em;font-weight:800;color:{INK};'
    rf'border-top:5px solid {INK};padding-top:0.5em;margin:0 0 0.3em;letter-spacing:-0.02em;">\1</h1>',
    frag, flags=re.DOTALL,
)
# numbered h2 banners
_n = [0]
def _h2(m):
    _n[0] += 1
    return (f'<h2 style="font-family:{SANS};font-size:1.4em;font-weight:700;color:{INK};'
            f'border-top:2px solid {INK};padding-top:0.45em;margin:1.8em 0 0.7em;letter-spacing:-0.01em;">'
            f'<span style="font-family:{MONO};color:{ACCENT};font-size:0.7em;">{_n[0]:02d} / </span>{m.group(1)}</h2>')
frag = re.sub(r"<h2[^>]*>(.*?)</h2>", _h2, frag, flags=re.DOTALL)
# h3
frag = re.sub(
    r"<h3[^>]*>(.*?)</h3>",
    rf'<h3 style="font-family:{SANS};font-size:1.08em;font-weight:600;color:{INK};margin:1.3em 0 0.4em;">'
    rf'<span style="color:{ACCENT};">▪</span> \1</h3>',
    frag, flags=re.DOTALL,
)
# tables
frag = frag.replace("<table>", f'<table style="width:100%;border-collapse:collapse;margin:1em 0;font-family:{SANS};">')
frag = frag.replace("<th ", f'<th data-x ').replace("<th>", "<th>")
frag = re.sub(r"<th[^>]*>(.*?)</th>",
              rf'<th style="text-align:left;padding:6px 10px;border-bottom:2px solid {INK};'
              rf'font-family:{MONO};font-size:0.8em;text-transform:uppercase;color:{MUTED};">\1</th>',
              frag, flags=re.DOTALL)
frag = re.sub(r"<td[^>]*>(.*?)</td>",
              rf'<td style="padding:6px 10px;border-bottom:1px solid {HAIR};vertical-align:top;">\1</td>',
              frag, flags=re.DOTALL)
# blockquote (subtitle + any stray)
frag = frag.replace("<blockquote>",
                    f'<blockquote style="border-left:3px solid {ACCENT};margin:0.6em 0;padding:0.2em 0 0.2em 0.9em;color:{MUTED};font-family:{MONO};">')
# GitHub-alert divs → bordered callouts
ALERT = {"note":"#3b6ea5","tip":"#2e7d4f","important":ACCENT,"warning":"#a8740f","caution":"#a5281c"}
for kind, col in ALERT.items():
    frag = frag.replace(
        f'<div class="{kind}">',
        f'<div style="border-left:4px solid {col};background:{PANEL};padding:0.7em 1em;margin:1.1em 0;">')
frag = re.sub(r'<div class="title">\s*<p>(.*?)</p>\s*</div>',
              rf'<p style="font-family:{MONO};font-size:0.78em;text-transform:uppercase;letter-spacing:0.08em;'
              rf'font-weight:700;margin:0 0 0.3em;">\1</p>', frag, flags=re.DOTALL)

# serial footer (Canvas-safe inline styles; entity-escaped · to avoid charset issues)
serial_footer = (
    f'<footer style="margin-top:2rem;padding-top:0.7rem;border-top:1px solid #ddd8cb;'
    f'font-family:\'Courier New\',monospace;font-size:0.62rem;letter-spacing:0.18em;'
    f'text-transform:uppercase;color:#6c675d;text-align:right;">'
    f'Serial · {SERIAL}</footer>'
) if SERIAL else ""

wrapper = (f'<div style="font-family:{SANS};color:{INK};line-height:1.55;max-width:52rem;">\n'
           f'{frag}\n'
           f'{serial_footer}\n'
           f'</div>\n')
OUT.write_text(wrapper, encoding="utf-8")
print(f"wrote {OUT} ({len(wrapper)} bytes, {_n[0]} sections)")
