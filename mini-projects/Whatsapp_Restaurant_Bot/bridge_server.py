import os
# Ensure Go's CGO uses the correct GCC toolchain from msys64.
# Anaconda installs incompatible assembler/linker tools (as.exe, ld.exe) earlier
# in PATH, which causes cgo.exe to fail when building the Go bridge.
# os.environ["PATH"] = r"C:\msys64\ucrt64\bin;" + os.environ.get("PATH", "")

import logging
import threading
import requests
from flask import Flask, request, jsonify
from whatsapp_bridge.bot import ApplicationBuilder, MessageHandler, TypeHandler
from whatsapp_bridge.bot import TextFilter

# ── Config ──────────────────────────────────────
N8N_WEBHOOK_URL = "https://n8n.srv1497935.hstgr.cloud/webhook/whatsapp-incoming"
BRIDGE_PORT = 5000
# ────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

flask_app = Flask(__name__)
application = None  # set after build

# n8n calls this endpoint to SEND a reply back to the customer
@flask_app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    phone = data.get("to")       # e.g. "919876543210"
    message = data.get("message")
    chat_jid = f"{phone}@s.whatsapp.net"
    application.bot.send_message(chat_jid, message)
    return jsonify({"status": "sent"})

# Called for every incoming WhatsApp message → forward to n8n
async def handle_message(update, context):
    msg = update.message
    if not msg:
        return
    payload = {
        "from": msg.get("sender", "").replace("@s.whatsapp.net", ""),
        "message": msg.get("content", "")
    }
    if payload["message"]:
        requests.post(N8N_WEBHOOK_URL, json=payload)
        logging.info(f"Forwarded to n8n: {payload}")

def run_flask():
    flask_app.run(host="0.0.0.0", port=BRIDGE_PORT)

def main():
    global application

    # Build the WhatsApp bot application
    application = ApplicationBuilder().build()

    # Register handler for all incoming text messages
    application.add_handler(MessageHandler(TextFilter(), handle_message))

    # Start Flask in background thread so n8n can call /send
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logging.info(f"Flask /send endpoint running on port {BRIDGE_PORT}")

    # Start polling WhatsApp (this is blocking — keeps script alive)
    logging.info("Starting WhatsApp polling... QR code will appear if needed.")
    application.run_polling()

if __name__ == "__main__":
    main()