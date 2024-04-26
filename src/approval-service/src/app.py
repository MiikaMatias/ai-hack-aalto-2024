from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def test():
    return "Hello world"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and file.filename.endswith('.txt'):
        filepath = os.path.join('/path/to/save', file.filename)
        file.save(filepath)
        return jsonify({"message": "File successfully uploaded"}), 200
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
