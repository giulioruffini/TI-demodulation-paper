#!/bin/sh
set -eu
repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$repo_dir"
build_dir="build/main_results"
mkdir -p "$build_dir" output/pdf
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
    -output-directory="$build_dir" -jobname=TN0484_main_results \
    presentations/tn0484_main_results.tex > "$build_dir/pass${pass}.txt" 2>&1
done
cp "$build_dir/TN0484_main_results.pdf" output/pdf/TN0484_main_results.pdf
printf '%s\n' 'Built output/pdf/TN0484_main_results.pdf'
