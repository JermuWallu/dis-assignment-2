import sqlite3
import random
import os

def view_db(db_name):
    # Connect to the database
    conn = sqlite3.connect("databases/{}".format(db_name))
    cursor = conn.cursor()

    # Fetch all records from the users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print the records
    for row in rows:
        print(row)

    # Close the connection
    conn.close()
    
def add_user(db_name, first_name, last_name, age):
    # Connect to the database
    conn = sqlite3.connect("databases/{}".format(db_name))
    cursor = conn.cursor()

    # Insert a new user into the users table
    cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)", (first_name, last_name, age))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
def modify_user(db_name, user_id, first_name=None, last_name=None, age=None):
    # Connect to the database
    conn = sqlite3.connect("databases/{}".format(db_name))
    cursor = conn.cursor()

    # Update the user's information based on the provided parameters
    if first_name is not None:
        cursor.execute("UPDATE users SET first_name = ? WHERE id = ?", (first_name, user_id))
    if last_name is not None:
        cursor.execute("UPDATE users SET last_name = ? WHERE id = ?", (last_name, user_id))
    if age is not None:
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
def delete_user(db_name, user_id):
    # Connect to the database
    conn = sqlite3.connect("databases/{}".format(db_name))
    cursor = conn.cursor()

    # Delete a user from the users table based on the provided user_id
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
