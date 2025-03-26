from flask import Flask, request, jsonify, render_template
from word_filter import find_matching_words
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("tezaurs_words.txt", encoding="utf-8") as f:
    WORDS = set(line.strip() for line in f if line.strip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find", methods=["POST"])
def find_words():
    data = request.get_json()
    letters = data.get("letters")
    pattern = data.get("pattern")
    matches = find_matching_words(letters, pattern, WORDS)
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
