from flask import Flask, jsonify, redirect, url_for
import json

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
    app.run(debug=True)
