#!/usr/bin/env bash
# Generate .openclaw/skills/ from canonical skills/ with short descriptions.
# OpenClaw discovery prefers description under 160 chars. Bodies stay identical.
# Run: ./scripts/build-openclaw-skills.sh [out-dir]
# Default out-dir: .openclaw/skills
# validate.sh fails if committed copies are stale.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT_DIR="${1:-.openclaw/skills}"
HOMEPAGE="https://github.com/tony-sappe/marvin"

# name|short description (<160 chars, one line, no double quotes)
DESCRIPTIONS=(
  "marvin|Set Marvin intensity (shrug/paranoid/big-brain) and show the skill map. Use for marvin or how to use this collection. Not a job-skill substitute."
  "bound-the-ask|Turn a request into a bounded contract before material work. Use for ambiguous asks, specs, briefs, multi-file or long work. Not for typos or known-bug fixes."
  "pack-light|Pack light. Build the smallest complete system you can trust. Use for design, new parts, YAGNI, vibe coding. Not for cleanup — use subtract."
  "prove-it|Refuse done without named evidence. Use when implementing, fixing, opening a PR, or verifying. Not a design skill; prefer the cheapest decisive proof."
  "find-the-fault|Debug with observe, one hypothesis, one experiment. Use for bugs, incidents, regressions, flaky tests, root cause. Not for greenfield or cleanup."
  "subtract|Reduce an existing system while preserving behavior. Use for refactor, delete dead code, drop deps, tech debt. Not for greenfield design."
)

body_of() {
  local src="skills/$1/SKILL.md"
  awk '
    BEGIN { n = 0 }
    /^---$/ {
      n++
      if (n <= 2) next
    }
    n >= 2 { print }
  ' "$src"
}

render() {
  local name="$1" desc="$2"
  local len="${#desc}"
  if (( len >= 160 )); then
    echo "description for $name is $len chars (want <160)" >&2
    exit 1
  fi
  if [[ "$desc" == *$'\n'* || "$desc" == *'"'* ]]; then
    echo "description for $name must be one line with no double quotes" >&2
    exit 1
  fi
  printf '%s\n' "---"
  printf '%s\n' "name: $name"
  printf '%s\n' "description: \"$desc\""
  printf '%s\n' "homepage: $HOMEPAGE"
  printf '%s\n' "license: MIT"
  printf '%s\n' "metadata:"
  printf '%s\n' "  collection: marvin"
  printf '%s\n' "  version: \"1.1.1\""
  printf '%s\n' "---"
  printf '\n'
  body_of "$name"
}

rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

for entry in "${DESCRIPTIONS[@]}"; do
  name="${entry%%|*}"
  desc="${entry#*|}"
  outdir="$OUT_DIR/$name"
  mkdir -p "$outdir"
  render "$name" "$desc" >"$outdir/SKILL.md"
  if [[ -d "skills/$name/references" ]]; then
    # Prefer a relative symlink when OUT_DIR is the repo default.
    if [[ "$OUT_DIR" == ".openclaw/skills" ]]; then
      ln -sfn "../../../skills/$name/references" "$outdir/references"
    else
      # Absolute for temp validation trees
      ln -sfn "$ROOT/skills/$name/references" "$outdir/references"
    fi
  fi
  echo "wrote $outdir/SKILL.md (${#desc} chars desc)"
done
