import os

from flask import Flask, flash, redirect, render_template, request, session
import sqlite3
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Establishing connection with the database
#Creating insider function
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('database.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/")
def index():
    return render_template("index.html")
    