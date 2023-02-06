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


@app.route("/", methods=["GET", "POST"])
def index():
    # region
    # Variables, lists and dicts:
    months = [{'name': 'January', 'number': '1'}, 
                {'name': 'February', 'number': '2'},
                {'name': 'March', 'number': '3'},
                {'name': 'April', 'number': '4'}, 
                {'name': 'May', 'number': '5'},
                {'name': 'June', 'number': '6'},
                {'name': 'July', 'number': '7'},
                {'name': 'August', 'number': '8'},
                {'name': 'September', 'number': '9'},
                {'name': 'October', 'number': '10'},
                {'name': 'November', 'number': '11'},
                {'name': 'December', 'number': '12'}]
    
    row_count = 1
    # endregion

    #First need to add correct buttons
    if request.method == "POST":
        if request.form.get('yearly_budget_add'):
            row_count = row_count + 1
        return render_template("index.html", months=months, row_count=row_count)
            #pass # do something
            #For add button
            #Check how many rows are alredy in
            #add one to their index
            #incert row into table 
            #and database (which one is better to do first?)
            #maybe incerting row and incerting info into database are two diferent movements


        #elif  request.form.get('action2') == 'VALUE2':
            #pass # do something else
            #For delete button
            #get the id of the row
            #detele that row from the list of rows
            #splice the list back together
            #delete should be next to each column
            #as well as edit button
    return render_template("index.html", months=months, row_count=row_count)
    