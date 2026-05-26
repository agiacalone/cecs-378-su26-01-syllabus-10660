#!/bin/bash
set -euo pipefail

# ── Term variables (edit each term; keep in sync with README.md) ──
COURSE=378
TYEAR=SU26
CLASS=01
SECTION=10660          # MyCSULB class number
NAME=Giacalone_Anthony
TITLE="CECS ${COURSE} · Section ${CLASS} · Summer 2026 — Syllabus"
SERIAL=$(awk -F': ' '/^serial:/{print $2; exit}' README.md)   # visible-but-unexplained build hash

OUT_HTML="cecs-${COURSE}-${TYEAR}-${CLASS}-syllabus-${SECTION}.html"
OUT_PDF="CECS ${COURSE}_${CLASS}_${TYEAR}_${NAME}.pdf"

# ── Primary output: styled, self-contained HTML (Swiss/grid theme) ──
# --embed-resources inlines syllabus.css so the file is portable;
# the @media print block in syllabus.css drives a clean PDF.
pandoc README.md \
  --from gfm \
  --to html5 \
  --standalone \
  --embed-resources \
  --css syllabus.css \
  --metadata title="${TITLE}" \
  --metadata lang=en \
  --include-after-body=<(printf '<footer class="serial">Serial · %s</footer>' "${SERIAL:-—}") \
  -o "${OUT_HTML}"
echo "→ ${OUT_HTML}"

# ── PDF for Canvas distribution ──
# Easiest: open the HTML in a browser and Print → Save as PDF
#   (uses the @media print rules in syllabus.css).
# Or one-shot, if a renderer is installed:
if command -v weasyprint >/dev/null 2>&1; then
  weasyprint "${OUT_HTML}" "${OUT_PDF}" && echo "→ ${OUT_PDF} (weasyprint)"
elif command -v chromium >/dev/null 2>&1; then
  chromium --headless --no-pdf-header-footer --print-to-pdf="${OUT_PDF}" "${OUT_HTML}" \
    && echo "→ ${OUT_PDF} (chromium)"
else
  echo "  (no weasyprint/chromium found — print ${OUT_HTML} from a browser for the PDF)"
fi
