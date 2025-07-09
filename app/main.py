from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"anachi said": "I love You mimisou!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
