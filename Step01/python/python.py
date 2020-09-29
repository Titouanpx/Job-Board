import mariadb
import sys
import sqlite3


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

cursor.execute("SELECT firstname,lastname FROM people")

print(f"{cursor.fetchone()}")

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
