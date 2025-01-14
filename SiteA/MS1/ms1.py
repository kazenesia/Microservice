from flask import Flask, jsonify
import requests
import logging

app = Flask(__name__)

# Set logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

@app.route("/db-a", methods=["GET"])
def access_db_a():
    try:
        # Simulasi akses ke DB-A
        db_a_data = {"db_a": "Data retrieved from DB-A"}
        return jsonify(db_a_data), 200
    except Exception as e:
        logging.error(f"Error accessing DB-A: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
