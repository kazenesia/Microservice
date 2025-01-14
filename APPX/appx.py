from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Microservice Demo Architecture",
        "routes": {
            "MS1": "http://localhost:5051/db-a",
            "MS2": "http://localhost:5052/db-a-and-db-b",
            "MS3": "http://localhost:5053/db-b-and-db-a"
        }
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
