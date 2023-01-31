import os

from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return "Set up a DB first"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)