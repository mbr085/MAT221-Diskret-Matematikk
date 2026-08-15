#!/usr/bin/env bash
set -euo pipefail

manifest="${1:-colab-files.txt}"

if [[ ! -f "$manifest" ]]; then
  echo "Fant ikke manifestet: $manifest" >&2
  exit 1
fi

mkdir -p colab

while IFS= read -r src || [[ -n "$src" ]]; do
  src="${src%%#*}"
  src="${src#"${src%%[![:space:]]*}"}"
  src="${src%"${src##*[![:space:]]}"}"

  [[ -z "$src" ]] && continue

  if [[ ! -f "$src" ]]; then
    echo "Fant ikke kildefilen: $src" >&2
    exit 1
  fi

  rel="${src#notes/}"
  out="colab/${rel%.qmd}.ipynb"
  mkdir -p "$(dirname "$out")"

  echo "$src -> $out"
  quarto convert "$src" --output "$out"
done < "$manifest"
