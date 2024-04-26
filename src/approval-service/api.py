from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<path:path>')
def serve(path):
    return send_from_directory('proposals', path)

@app.route('/getpaths')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)
