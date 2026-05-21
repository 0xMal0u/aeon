#!/usr/bin/env bash
set -euo pipefail
CHAT="${TELEGRAM_CHAT_ID:-unknown}"
MSG="ID: $CHAT"
./notify "$MSG"
