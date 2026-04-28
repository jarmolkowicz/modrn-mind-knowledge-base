#!/usr/bin/env bash
#
# Builds a single concatenated markdown file from the Knowledge Base.
# Output: dist/modern-mind-kb.md
#
set -euo pipefail

OUTDIR="dist"
OUTFILE="$OUTDIR/modern-mind-kb.md"

mkdir -p "$OUTDIR"

# Sections to include (order matters)
SECTIONS=("concepts" "frameworks" "practices" "sources")
LABELS=("Concepts" "Frameworks" "Practices" "Sources")

# --- Header ---
cat > "$OUTFILE" << 'HEADER'
# Modern Mind — Knowledge Base for the AI Age

Research, practice, and professional insight translated into concepts you can teach from, apply, and verify.

Not anti-AI. Not blindly pro-AI. Pro-human.

> This file is auto-generated from the Modern Mind Knowledge Base.
> Source: https://github.com/jarmolkowicz/modern-mind-knowledge-base
> Website: https://modrnmind.com

---

HEADER

# --- Table of Contents ---
echo "## Table of Contents" >> "$OUTFILE"
echo "" >> "$OUTFILE"

for i in "${!SECTIONS[@]}"; do
  section="${SECTIONS[$i]}"
  label="${LABELS[$i]}"
  echo "### ${label}" >> "$OUTFILE"
  echo "" >> "$OUTFILE"

  for file in "$section"/*.md; do
    [ -f "$file" ] || continue
    # Extract the H1 title from the file, fall back to filename
    title=$(grep -m1 '^# ' "$file" | sed 's/^# //' || true)
    if [ -z "$title" ]; then
      title=$(basename "$file" .md | tr '-' ' ')
    fi
    # Create anchor from filename
    anchor="${section}-$(basename "$file" .md)"
    echo "- [${title}](#${anchor})" >> "$OUTFILE"
  done
  echo "" >> "$OUTFILE"
done

echo "---" >> "$OUTFILE"
echo "" >> "$OUTFILE"

# --- Content ---
for i in "${!SECTIONS[@]}"; do
  section="${SECTIONS[$i]}"
  label="${LABELS[$i]}"

  echo "## ${label}" >> "$OUTFILE"
  echo "" >> "$OUTFILE"

  for file in "$section"/*.md; do
    [ -f "$file" ] || continue

    anchor="${section}-$(basename "$file" .md)"

    # Add anchor-compatible heading
    echo "<a id=\"${anchor}\"></a>" >> "$OUTFILE"
    echo "" >> "$OUTFILE"

    # Include file content (strip YAML frontmatter)
    awk '
      BEGIN { in_frontmatter=0; frontmatter_done=0 }
      /^---$/ && !frontmatter_done {
        if (in_frontmatter) { frontmatter_done=1; next }
        else { in_frontmatter=1; next }
      }
      frontmatter_done || !in_frontmatter { print }
    ' "$file" >> "$OUTFILE"

    echo "" >> "$OUTFILE"
    echo "---" >> "$OUTFILE"
    echo "" >> "$OUTFILE"
  done
done

# --- Stats ---
TOTAL=0
for section in "${SECTIONS[@]}"; do
  COUNT=$(ls "$section"/*.md 2>/dev/null | wc -l | tr -d ' ')
  TOTAL=$((TOTAL + COUNT))
done

echo "Bundle built: $OUTFILE ($TOTAL entries)"
