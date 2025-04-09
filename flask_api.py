from flask import Flask, jsonify, redirect, url_for
import json
import os

app = Flask(__name__)

@app.route('/latest-trends', methods=['GET'])
def get_latest_trends():
    try:
        with open("latest_batch.json", "r") as f:
            data = json.load(f)
        
        return jsonify(data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return redirect(url_for('get_latest_trends'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
