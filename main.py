from flask import Flask, request
import requests

app = Flask(__name__)

BOT_ID = "677e433c8d5de31c9bbcdc6e1e"  # Replace this with your actual GroupMe Bot ID

def send_message(text):
    requests.post("https://api.groupme.com/v3/bots/post", json={
        "bot_id": BOT_ID,
        "text": text
    })

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    text = data.get("text")
    name = data.get("name")

    if text and text.strip() == "67":
        send_message(f"Hey {name}, you said 67!")

    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
