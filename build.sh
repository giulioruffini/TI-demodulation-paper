#!/usr/bin/env bash
# Build TN0484 in either of its two forms from the single source.
#
#   ./build.sh          Technical Note        -> TN0484_envelope_demodulation.pdf
#   ./build.sh jne      JNE article (no apps)  -> TN0484_jne.pdf
#   ./build.sh supp     JNE supplement         -> TN0484_jne_supplement.pdf
#   ./build.sh both     TN + JNE
#   ./build.sh all      TN + JNE + supplement
#
# JNE counts the article against a ~12,000-word guideline, so the JNE build drops
# the appendices and supplementary figures and `supp` emits them as a companion
# file. The TN build keeps everything in one PDF.
#
# The two differ only by the \ifjne switch in the preamble: the TN keeps the
# Neuroelectrics/BCOM furniture and the prose abstract, the JNE build strips the
# furniture and uses the structured abstract plus the declarations IOP requires.

set -euo pipefail
cd "$(dirname "$0")"

SRC=TN0484_envelope_demodulation

build() {
  local jobname="$1" prelude="$2" label="$3"
  echo "==> building ${label} (${jobname}.pdf)"
  # Three passes plus bibtex: refs, then bibliography, then two to settle.
  pdflatex -interaction=nonstopmode -jobname="${jobname}" "${prelude}\\input{${SRC}}" >/dev/null 2>&1 || true
  bibtex "${jobname}" >/dev/null 2>&1 || true
  pdflatex -interaction=nonstopmode -jobname="${jobname}" "${prelude}\\input{${SRC}}" >/dev/null 2>&1 || true
  pdflatex -interaction=nonstopmode -jobname="${jobname}" "${prelude}\\input{${SRC}}" >/dev/null 2>&1 || true

  local pages errors undef
  pages=$(grep -o '([0-9]* pages' "${jobname}.log" | tail -1 | tr -d '(' || echo "?")
  errors=$(grep -c '^!' "${jobname}.log" || true)
  undef=$(grep -c 'undefined' "${jobname}.log" || true)
  echo "    ${pages}, ${errors} errors, ${undef} undefined"
  if [ "${errors}" -ne 0 ]; then
    echo "    FAILED -- see ${jobname}.log"
    grep -A3 '^!' "${jobname}.log" | head -20
    return 1
  fi
}

case "${1:-tn}" in
  tn)   build "${SRC}" ""              "Technical Note" ;;
  jne)  build "TN0484_jne" "\\def\\jnebuild{}" "JNE article" ;;
  supp) build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement" ;;
  both) build "${SRC}" ""              "Technical Note"
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE article" ;;
  all)  build "${SRC}" ""              "Technical Note"
        build "TN0484_jne" "\\def\\jnebuild{}" "JNE article"
        build "TN0484_jne_supplement" "\\def\\suppbuild{}" "JNE supplement" ;;
  *)    echo "usage: $0 [tn|jne|supp|both|all]" >&2; exit 2 ;;
esac
