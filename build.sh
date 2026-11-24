#!/usr/bin/env bash
# Build TN0484 in either of its two forms from the single source.
#
#   ./build.sh          JNE working article   -> TN0484_jne.pdf
#   ./build.sh jne      same working article  -> TN0484_jne.pdf
#   ./build.sh tn       Technical Note        -> TN0484_envelope_demodulation.pdf
#   ./build.sh supp     JNE supplement         -> TN0484_jne_supplement.pdf
#   ./build.sh journal  JNE article + supplement with settled cross-references
#   ./build.sh both     TN + JNE
#   ./build.sh all      TN + JNE + supplement
# Routine edits update the JNE article. Regenerate TN and supplement for an
# authorized archive cut; do not create per-edit versioned reading copies.
#
# JNE retains notation and compact model derivations as article appendices.
# `supp` emits additional material organized by topic. The TN keeps all material.
#
# The two differ only by the \ifjne switch in the preamble: the TN keeps the
# Neuroelectrics/BCOM furniture and the prose abstract, the JNE build strips the
# furniture and uses the structured abstract plus the declarations IOP requires.

set -euo pipefail
cd "$(dirname "$0")"

SRC=TN0484_envelope_demodulation
TN_ROOT=$(pwd)

build() {
  local jobname="$1" prelude="$2" label="$3" mode="${4:-publish}"
  local stage_dir
  mkdir -p build
  stage_dir=$(mktemp -d "build/.latex-${jobname}.XXXXXX")
  echo "==> building ${label} (${jobname}.pdf)"
  # Keep the last complete PDF visible to Preview and the review-shelf watcher.
  # A failed build leaves its diagnostic files in stage_dir.
  # Three passes plus bibtex: refs, then bibliography, then two to settle.
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="${stage_dir}" -jobname="${jobname}" "${prelude}\\input{${SRC}}" >"${stage_dir}/build.txt" 2>&1
  (cd "${stage_dir}" && BIBINPUTS="${TN_ROOT}:${BIBINPUTS:-}" BSTINPUTS="${TN_ROOT}:${BSTINPUTS:-}" bibtex "${jobname}") >>"${stage_dir}/build.txt" 2>&1
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="${stage_dir}" -jobname="${jobname}" "${prelude}\\input{${SRC}}" >>"${stage_dir}/build.txt" 2>&1
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory="${stage_dir}" -jobname="${jobname}" "${prelude}\\input{${SRC}}" >>"${stage_dir}/build.txt" 2>&1

  local pages errors undef
  pages=$(grep -o '([0-9]* pages' "${stage_dir}/${jobname}.log" | tail -1 | tr -d '(' || echo "?")
  errors=$(grep -c '^!' "${stage_dir}/${jobname}.log" || true)
  undef=$(grep -c 'undefined' "${stage_dir}/${jobname}.log" || true)
  echo "    ${pages}, ${errors} errors, ${undef} undefined"
  if [ "${errors}" -ne 0 ] || { [ "${undef}" -ne 0 ] && [ "$mode" != "labels" ]; }; then
    echo "    FAILED -- see ${stage_dir}/${jobname}.log"
    return 1
  fi
  if [ "$mode" = "labels" ]; then
    # Bootstrap cross-document labels without exposing an incomplete PDF.
    mv -f "${stage_dir}/${jobname}.aux" .
    return 0
  fi
  test -s "${stage_dir}/${jobname}.pdf"
  # Stage and destination share a filesystem: mv publishes each complete file
  # with a rename rather than exposing a PDF while it is being written.
  local product
  for product in "${stage_dir}/${jobname}."*; do
    mv -f "$product" .
  done
  mv -f "${stage_dir}/build.txt" "build/${jobname}_build.txt"
  rmdir "${stage_dir}"
}

case "${1:-jne}" in
  tn)   build "${SRC}" "\\def\\tnbuild{}" "Technical Note" ;;
  jne)  build "TN0484_jne" "\\def\\jnebuild{}" "JNE article" ;;
  supp) build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement" ;;
  journal) build "TN0484_jne" "\\def\\jnebuild{}" "JNE cross-reference labels" labels
        build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement labels" labels
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE article"
        build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement (settled references)" ;;
  both) build "${SRC}" "\\def\\tnbuild{}" "Technical Note"
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE article" ;;
  all)  build "${SRC}" "\\def\\tnbuild{}" "Technical Note"
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE cross-reference labels" labels
        build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement"
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE article"
        build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement (settled references)" ;;
  *)    echo "usage: $0 [tn|jne|supp|journal|both|all]" >&2; exit 2 ;;
esac
