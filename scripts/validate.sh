#!/usr/bin/env bash
# Structural acceptance checks for Marvin skills and host adapters.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

fail=0
skills=(marvin bound-the-ask pack-light prove-it find-the-fault subtract)
# Symlink adapters (identical bytes to canonical).
host_skill_roots=(.agents/skills .cursor/skills .windsurf/skills)

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

echo "== versions =="
want="$(awk -F'"' '/"version"/{print $4; exit}' plugin.json)"
if [[ -z "$want" ]]; then
  echo "MISSING version in plugin.json"; fail=1
  want="MISSING"
else
  echo "OK plugin.json version $want"
fi
for f in .codex-plugin/plugin.json .claude-plugin/plugin.json; do
  got="$(awk -F'"' '/"version"/{print $4; exit}' "$f")"
  if [[ "$got" != "$want" ]]; then
    echo "VERSION DRIFT $f (got '$got' want '$want')"; fail=1
  else
    echo "OK $f version $got"
  fi
done
for s in "${skills[@]}"; do
  f="skills/$s/SKILL.md"
  got="$(awk '/^  version:/{gsub(/"/,"",$2); print $2; exit}' "$f")"
  if [[ "$got" != "$want" ]]; then
    echo "VERSION DRIFT $f (got '$got' want '$want')"; fail=1
  else
    echo "OK $f version $got"
  fi
done
prompts="$(python3 -c 'import json; print(len(json.load(open(".codex-plugin/plugin.json")).get("interface",{}).get("defaultPrompt") or []))' 2>/dev/null || echo "?")"
if [[ "$prompts" == "?" ]]; then
  echo "SKIP defaultPrompt count (python3 unavailable)"
elif (( prompts > 3 )); then
  echo "TOO MANY defaultPrompt entries ($prompts; Codex keeps at most 3)"; fail=1
else
  echo "OK .codex-plugin defaultPrompt count $prompts"
fi

echo "== AGENTS.md =="
alines="$(wc -l < AGENTS.md | tr -d ' ')"
if (( alines > 40 )); then
  echo "AGENTS.md too long ($alines)"; fail=1
else
  echo "OK AGENTS.md ($alines lines)"
fi

echo "== manifests =="
for f in \
  plugin.json \
  .codex-plugin/plugin.json \
  .grok-plugin/marketplace.json \
  .agents/plugins/marketplace.json \
  .claude-plugin/plugin.json \
  .claude-plugin/marketplace.json
do
  if [[ ! -f "$f" ]]; then
    echo "MISSING $f"; fail=1
  else
    echo "OK $f"
  fi
done

echo "== host skill adapters =="
for root in "${host_skill_roots[@]}"; do
  if [[ ! -d "$root" ]]; then
    echo "MISSING DIR $root"; fail=1
    continue
  fi
  for s in "${skills[@]}"; do
    link="$root/$s"
    if [[ ! -L "$link" ]]; then
      echo "NOT SYMLINK $link"; fail=1
      continue
    fi
    target="$(readlink "$link")"
    if [[ "$target" != "../../skills/$s" ]]; then
      echo "BAD TARGET $link -> $target (want ../../skills/$s)"; fail=1
      continue
    fi
    if [[ ! -f "$link/SKILL.md" ]]; then
      echo "BROKEN LINK $link (SKILL.md missing)"; fail=1
      continue
    fi
    # identical bytes to canonical
    if ! cmp -s "skills/$s/SKILL.md" "$link/SKILL.md"; then
      echo "DRIFT $link/SKILL.md vs skills/$s/SKILL.md"; fail=1
      continue
    fi
    echo "OK $link -> ../../skills/$s"
  done
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
