import os

from flask import Flask, flash, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

if __name__ == "__main__":
    DEBUG = True
    HOST = '0.0.0.0'
    app.run(debug=DEBUG, host=HOST)