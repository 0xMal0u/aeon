#!/usr/bin/env bash
set -euo pipefail
./notify "Your Telegram Chat ID: \`${TELEGRAM_CHAT_ID:-not configured}\`"
