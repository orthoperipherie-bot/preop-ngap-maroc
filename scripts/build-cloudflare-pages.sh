#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-dist}"
OUT="$(mkdir -p "$OUT" && cd "$OUT" && pwd)"

rm -rf "$OUT"
mkdir -p "$OUT"

# Root application and data files used by the NGAP calculator.
for file in index.html manifest.webmanifest sw.js acts.json orthopedie-actes.json market-prices.json; do
  if [[ -f "$ROOT/$file" ]]; then cp "$ROOT/$file" "$OUT/$file"; fi
done

# Static applications. Copy complete folders so future assets are not silently omitted.
for app in simulateur-honoraires orthoos-ebot orthoscores suivi-patients ortho-clair pharmacie-garde-maroc orthovisu ortho-suite; do
  if [[ -d "$ROOT/$app" ]]; then
    mkdir -p "$OUT/$app"
    cp -a "$ROOT/$app/." "$OUT/$app/"
  fi
done

touch "$OUT/.nojekyll"
echo "Cloudflare Pages static site prepared in: $OUT"