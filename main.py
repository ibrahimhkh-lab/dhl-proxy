from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ DHL Proxy يعمل"

@app.route("/invoices")
def invoices():
    key = request.args.get("api_key","")
    r = requests.get(
        "https://app.daftra.com/api2/invoices",
        headers={"APIKEY": key},
        params={
            "date_from": request.args.get("date_from",""),
            "date_to":   request.args.get("date_to",""),
            "limit":     request.args.get("limit","200")
        }, timeout=20)
    return jsonify(r.json()), r.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
