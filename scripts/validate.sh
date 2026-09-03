#!/usr/bin/env bash
# Structural acceptance checks for Don't Panic skills.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail=0
skills=(dont-panic bound-the-ask smallest-trusted prove-it find-the-fault subtract)

echo "== skill folders =="
for s in "${skills[@]}"; do
  f="skills/$s/SKILL.md"
  if [[ ! -f "$f" ]]; then
    echo "MISSING $f"; fail=1; continue
  fi
  name="$(awk '/^name:/{print $2; exit}' "$f")"
  if [[ "$name" != "$s" ]]; then
    echo "NAME MISMATCH $f (got '$name')"; fail=1
  fi
  lines="$(wc -l < "$f" | tr -d ' ')"
  if (( lines > 200 )); then
    echo "TOO LONG $f ($lines lines)"; fail=1
  else
    echo "OK $f ($lines lines)"
  fi
  # description must be a single line and must not contain colon-space
  desc_line="$(awk '/^description:/{print; exit}' "$f")"
  if [[ "$desc_line" == *": "*": "* ]]; then
    # crude: after the first "description: " any further ": " is illegal
    rest="${desc_line#description: }"
    if [[ "$rest" == *": "* ]]; then
      echo "COLON-SPACE IN DESCRIPTION $f"; fail=1
    fi
  fi
  if grep -qE '^description:.*[<>]' "$f"; then
    echo "ANGLE BRACKETS IN DESCRIPTION $f"; fail=1
  fi
done

echo "== AGENTS.md =="
alines="$(wc -l < AGENTS.md | tr -d ' ')"
if (( alines > 40 )); then
  echo "AGENTS.md too long ($alines)"; fail=1
else
  echo "OK AGENTS.md ($alines lines)"
fi

echo "== manifests =="
for f in plugin.json .codex-plugin/plugin.json .grok-plugin/marketplace.json .agents/plugins/marketplace.json; do
  if [[ ! -f "$f" ]]; then echo "MISSING $f"; fail=1; else echo "OK $f"; fi
done

echo "== hooks ban =="
if find . -name 'hooks.json' -o -path './hooks/*' 2>/dev/null | grep -q .; then
  echo "HOOKS PRESENT (v1 forbids hooks)"; fail=1
else
  echo "OK no hooks"
fi

if (( fail )); then
  echo "FAIL"
  exit 1
fi
echo "PASS"
