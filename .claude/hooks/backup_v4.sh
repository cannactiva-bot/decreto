#!/usr/bin/env bash
# PreToolUse hook: backup de v4.docx antes de ejecutar cualquier _apply_*.py en cnmc/
# Recibe JSON en stdin con tool_name + tool_input.command.
# Solo actua si el comando contiene "_apply_" Y "cnmc".

input=$(cat)
if echo "$input" | grep -q "_apply_" && echo "$input" | grep -q "cnmc"; then
  ts=$(date +%Y%m%d_%H%M%S)
  mkdir -p "/c/Users/micro/Desktop/cnmc/_backups" 2>/dev/null
  if [ -f "/c/Users/micro/Desktop/cnmc/Dossier_CNMC_AECANI_v4.docx" ]; then
    cp "/c/Users/micro/Desktop/cnmc/Dossier_CNMC_AECANI_v4.docx" \
       "/c/Users/micro/Desktop/cnmc/_backups/Dossier_CNMC_AECANI_v4_${ts}.docx" 2>/dev/null
  fi
fi
exit 0
