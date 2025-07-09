from flask import Flask, jsonify

app = Flask(_name__)

@app.route("/")
def home():
    return jsonify({"message":"Bienvenue dans l'API Flask !"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)