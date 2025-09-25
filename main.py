from flask import Flask, request
import time
import requests

app = Flask(__name__)

BOT_ID = "	677e433c8d5de31c9bbcdc6e1e"        # Replace with your GroupMe bot ID
BOT_USER_ID = "TEMP"          # You'll update this after deployment

muted_users = {}
MUTE_DURATION = 60 * 60  # 1 hour

def send_message(text):
    requests.post("https://api.groupme.com/v3/bots/post", json={
        "bot_id": BOT_ID,
        "text": text
    })

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    sender_id = data.get("sender_id")
    name = data.get("name")
    text = data.get("text")

    if sender_id == BOT_USER_ID:
        return "OK", 200

    now = time.time()
    if sender_id in muted_users:
        if now < muted_users[sender_id]:
            print(f"{name} is muted.")
            return "Muted", 200
        else:
            del muted_users[sender_id]

    if text.strip() == "67":
        muted_users[sender_id] = now + MUTE_DURATION
        send_message(f"{name} has been muted for 1 hour for saying 67.")
        return "Muted", 200

    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
