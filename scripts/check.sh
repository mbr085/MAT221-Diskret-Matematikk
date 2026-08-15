#!/usr/bin/env bash
set -euo pipefail

echo "== Quarto =="
quarto --version

echo
echo "== Python =="
python --version

echo
echo "== QUARTO_PYTHON =="
printf '%s\n' "${QUARTO_PYTHON:-<not set>}"

echo
echo "== Quarto/Jupyter check =="
quarto check jupyter

echo
echo "== Python imports =="
python - <<'PY'
import matplotlib
import networkx
import numpy
import sympy

print("numpy:", numpy.__version__)
print("sympy:", sympy.__version__)
print("matplotlib:", matplotlib.__version__)
print("networkx:", networkx.__version__)
PY

echo
echo "== Render book (HTML + PDF) =="
quarto render

echo
echo "== Export Colab notebooks =="
./scripts/export-colab.sh

echo
echo "All checks passed."
