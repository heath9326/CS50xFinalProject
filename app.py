import os

from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")
    

if __name__ == "__main__":
    app.run(debug=True)