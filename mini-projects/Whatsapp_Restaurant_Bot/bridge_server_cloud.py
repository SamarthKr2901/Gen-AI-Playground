import os
os.environ["PATH"] = "/usr/local/go/bin:" + os.environ.get("PATH", "")

import logging
import threading
import requests
from flask import Flask, request, jsonify
from whatsapp_bridge.bot import ApplicationBuilder, MessageHandler
from whatsapp_bridge.bot import TextFilter

N8N_WEBHOOK_URL = "https://n8n.srv1497935.hstgr.cloud/webhook-test/whatsapp-incoming"
BRIDGE_PORT = 5000

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

flask_app = Flask(__name__)
application = None

@flask_app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    phone = data.get("to", "")
    message = data.get("message", "")
    logging.info(f"Send request: to={phone}, message={message[:60]}")
    if not phone or not message:
        return jsonify({"status": "error", "reason": "missing phone or message"}), 400
    chat_jid = f"{phone}@s.whatsapp.net"
    try:
        result = application.listener.client.send_message(chat_jid, message)
        logging.info(f"Send result: {result}")
        return jsonify({"status": "sent"})
    except Exception as e:
        logging.error(f"Send failed: {e}", exc_info=True)
        return jsonify({"status": "error", "reason": str(e)}), 500

async def handle_message(update, context):
    msg = update.message
    if not msg:
        return
    # Log the FULL message object so we can see all fields
    logging.info(f"FULL MESSAGE OBJECT: {msg}")
    payload = {
        "from": msg.get("chat_jid", "").replace("@s.whatsapp.net", ""),
        "message": msg.get("content", "")
    }
    logging.info(f"Payload being sent to n8n: {payload}")
    if payload["message"]:
        requests.post(N8N_WEBHOOK_URL, json=payload)
        logging.info(f"Forwarded to n8n: {payload}")

def run_flask():
    flask_app.run(host="0.0.0.0", port=BRIDGE_PORT)

def main():
    global application
    application = ApplicationBuilder().build()
    application.add_handler(MessageHandler(TextFilter(), handle_message))
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logging.info(f"Flask /send endpoint running on port {BRIDGE_PORT}")
    logging.info("Starting WhatsApp polling...")
    application.run_polling()

if __name__ == "__main__":
    main()
