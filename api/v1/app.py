#!/usr/bin/python3
"""get api"""
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.pages import app_pages


app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_pages)


@app.errorhandler(404)
def error(error):
    """return a 404 when resource not found"""
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    """runs api app"""
    app.run(host="0.0.0.0", port=5001, debug=True, threaded=True)
