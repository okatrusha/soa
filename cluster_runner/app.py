from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/hello-world", methods=["GET"])
def hello_world():
    response = requests.get("http://greeting_service:5001/greet")
    greeting = response.json().get("message", "")
    return jsonify({"message": f"{greeting} World"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)