from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import matplotlib.pyplot as plt, mpld3

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"test": True})

@app.route('/post', methods = ['POST'])
def predict():
    val = request.json['namequery']
    return jsonify({"yo_sent": val})

@app.route('/graph')
def graph():
    plot_name = "plot1"
    plt.clf()
    plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
    plt.savefig("static/"+ plot_name +".png")
    # plt.show()
    # mpld3.show()
    return send_file("static/plot1.png")
    # return jsonify({"uri": "localhost:5000/static/" + plot_name + ".png"})


@app.route('/graph2')
def graph2():
    plot_name = "plot2"
    plt.clf()
    plt.plot([2,7,2,3,8.9,11], 'ks-', mec='w', mew=5, ms=20)
    plt.savefig("static/"+ plot_name +".png")
    # plt.show()
    # mpld3.show()
    return jsonify({"uri": "localhost:5000/static/" + plot_name + ".png"})

if __name__ == "__main__":
    app.run(debug=True)