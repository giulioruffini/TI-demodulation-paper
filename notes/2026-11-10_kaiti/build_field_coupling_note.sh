#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "$0")/../.." && pwd)"
cd "$project_dir"
build_dir="$project_dir/build/field_coupling_note"
mkdir -p "$build_dir" "$project_dir/output/pdf"
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$build_dir" "$project_dir/notes/2026-11-10_kaiti/field_coupling_note.tex" \
  > "$build_dir/build_console.log" 2>&1
cp "$build_dir/field_coupling_note.pdf" "$project_dir/output/pdf/TN0484_field_coupling_note.pdf"
