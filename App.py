from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola Flask en Docker</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
