from flask import Flask, render_template, jsonify
import os
from simulator import get_next_prediction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/brain")
def brain():
    return jsonify(get_next_prediction())

if __name__ == "__main__":
    app.run(debug=True)