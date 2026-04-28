#!/usr/bin/env bash
# PostToolUse hook: tras ejecutar un _apply_*.py en cnmc/, regenera PDF y ZIP.
# Solo actua si el comando contiene "_apply_" Y "cnmc".

input=$(cat)
if echo "$input" | grep -q "_apply_" && echo "$input" | grep -q "cnmc"; then
  echo "[hook post_apply] Convirtiendo a PDF..."
  python "C:/Users/micro/Desktop/cnmc/_convert_v4.py" 2>&1 | tail -3
  echo "[hook post_apply] Reconstruyendo ZIP..."
  python "C:/Users/micro/Desktop/cnmc/_build_entrega.py" 2>&1 | tail -3
fi
exit 0
