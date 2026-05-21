#!/usr/bin/env python3
import os
import json
import urllib.request

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")

if not bot_token or not chat_id:
    print("Telegram not configured")
    exit(0)

msg = f"Your Telegram Chat ID: `{chat_id}`"
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
data = json.dumps({"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}).encode()
req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req) as resp:
        print("Sent:", resp.status)
except Exception as e:
    print("Error:", e)
