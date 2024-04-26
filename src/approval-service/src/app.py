from flask import Flask, request, jsonify
from proposal_maker import get_proposals
import os

app = Flask(__name__)

@app.route('/')
def test():
    return get_proposals("./RFPs/rfp1.txt")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    return get_proposals(file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
