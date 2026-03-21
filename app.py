from flask import Flask, jsonify
from steamScraper import scrape_steam

app = Flask(__name__)

@app.route("/deals")
def get_deals():
    data = scrape_steam()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)