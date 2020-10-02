import mariadb
import sys
import sqlite3
import requests

from flask import *
import os

import json


def get_mdp_db():
    with open("../mdp_bdd.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


def connect():
    try:
        connexion = mariadb.connect(
            user="root",
            password=get_mdp_db(),
            host="127.0.0.1",
            port=3306,
            database="jobboarddb"
        )
        return connexion
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


cursor = connect().cursor()


app = Flask(__name__)

"""
@app.route('/')
def index():
    return "Hello World"
"""


@app.route('/')
def index():
    cursor.execute("SELECT title,description FROM advertisements")

    fetchall_data = cursor.fetchall()
    print(fetchall_data)

    return render_template('index.html', rows=fetchall_data)


if __name__ == '__main__':
    app.run(debug=True)

"""
def get_name(database_file, person_id):
    query = "SELECT personal || ' ' || family FROM Person WHERE id=?;"

    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query, [person_id])
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results[0][0]


print(get_name('survey.db', 'dyer'))
"""
