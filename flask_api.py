from flask import Flask, jsonify
import json
import threading
import subprocess
import time

app = Flask(__name__)

DATA_FILE = "latest_fashion.json"

def run_scraper():
    """Runs the app.py scraper every 24 hours"""
    while True:
        subprocess.run(["python", "app.py"])    
        time.sleep(86400) 

threading.Thread(target=run_scraper, daemon=True).start()

@app.route('/fashion-trends', methods=['GET'])
def get_fashion_trends():
    """Returns the latest scraped fashion trends as JSON"""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "No data available yet"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
