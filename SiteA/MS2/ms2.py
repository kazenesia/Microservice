from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Set logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

@app.route("/db-a-and-db-b", methods=["GET"])
def access_db_a_and_db_b():
    db_a_data, db_b_data = None, None

    # Akses DB-A
    try:
        db_a_response = requests.get("http://localhost:5051/db-a", timeout=10)
        db_a_response.raise_for_status()
        db_a_data = db_a_response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error accessing DB-A: {e}")
        db_a_data = {"error": str(e)}

    # Akses DB-B
    try:
        db_b_response = requests.get("http://localhost:5053/db-b", timeout=10)
        db_b_response.raise_for_status()
        db_b_data = db_b_response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error accessing DB-B: {e}")
        db_b_data = {"error": str(e)}

    return jsonify({
        "message": "Accessed DB-A and DB-B from MS2",
        "db_a": db_a_data,
        "db_b": db_b_data
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5052)
