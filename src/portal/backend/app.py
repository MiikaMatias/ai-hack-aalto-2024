from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__, static_folder='frontend/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.isfile("frontend/build/" + path):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')

@app.route('/upload_proposal', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    return get_proposals(file)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
