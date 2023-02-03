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
    #Establish db connection:
    conn = db_connection()
    #Grab cursor:
    cursor = conn.cursor()

    #Example of creating a select through cursor
    cursor = conn.execute("SELECT * FROM database")
    #Now sort the selection into a dictionary
    books = [
        dict(id=row[0], author=row[1], language=row[2], title=row[3])
        for row in cursor.fetchall()
    ]
    if books is not None:
        return jsonify(books)

    #Establish the query you want performed
    sql = """INSERT INTO book (author, language, title)
             VALUES (?, ?, ?)"""
    cursor = cur.execute(sql, (new_autor, new_lang, new_title))    
    conn.commit()
    return f"Book with the id {cursor.lastrowid} created successfully", 201
    
    return render_template("layout.html")
    