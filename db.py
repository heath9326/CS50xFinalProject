import sqlite3

conn = sqlite3.connect("database.sqlite")

#create cursor using established connection
cursor = conn.cursor()

#Write query to create a table
#sql_query = """ CREATE TABLE category_list (
        #category_id integer PRIMARY KEY AUTOINCREMENT,
        #category_name text NOT NULL
#)""" 

#sql_query = """ CREATE TABLE subcategory_list (
        #subcategory_id integer PRIMARY KEY AUTOINCREMENT,
        #subcategory_name text NOT NULL
#)""" 

#sql_query = """ CREATE TABLE budget (
        #expenditure_id integer PRIMARY KEY AUTOINCREMENT,
        #expenditure_name text NOT NULL,
        #category_id integer NOT NULL references category_list(category_id),
        #subcategory_id integer NOT NULL references subcategory_list(subcategory_id),
        #status text NOT NULL,
        #billing_type text NOT NULL,
        #cost real NOT NULL,
        #URL text
#)"""

#Use cursor to execute the quesry
cursor.execute(sql_query)
