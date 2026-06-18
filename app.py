from flask import Flask, jsonify
from flask_cors import CORS
from steamScraper import scrape_steam

app = Flask(__name__)
CORS(app) #allows html frontend to call api

@app.route("/")
def index():
    return "Steam Scraper API is running. Hit /deals to fetch data"

@app.route("/deals")
def get_deals():
    data = scrape_steam()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)