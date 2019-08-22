from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"test": True})

@app.route('/post', methods = ['POST'])
def predict():
    val = request.json['namequery']
    return jsonify({"yo_sent": val})

if __name__ == "__main__":
    app.run(debug=True)