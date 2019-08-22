from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"test": True})

@app.route('/predict', methods = ['POST'])
def predict():
    val = request.json['namequery']
    return jsonify({"yo_sent": val})

if __name__ == "__main__":
    app.run(debug=True)