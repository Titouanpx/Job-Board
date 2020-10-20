import mariadb
import sys

from configparser import ConfigParser


def connect():
    try:
        config_object = ConfigParser()
        config_object.read(".env")
        databaseinfo = config_object["DATABASEINFO"]

        connection = mariadb.connect(
            user=databaseinfo["user"],
            password=databaseinfo["password"],
            host=databaseinfo["host"],
            port=int(databaseinfo["port"]),
            database=databaseinfo["databasename"]
        )
        return connection
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


connect = connect()
cursor = connect.cursor()


def model_create_new_ad(id, title, descr, wage, place, work_time, idpeople, idcompany):
    cursor.execute(
        "INSERT INTO advertisements (id, title, description, wage, place, working_time, id_people, id_company)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, title, descr, wage, place, work_time, idpeople, idcompany))
    connect.commit()

    print("ad created")


def model_get_ads():
    cursor.execute("SELECT * FROM advertisements")
    fetchall_data = cursor.fetchall()
    print(fetchall_data)
    return fetchall_data


def model_get_ad_by_id(ad_id):
    cursor.execute("SELECT * FROM advertisements WHERE id=?", (ad_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data


def model_get_people_by_id(people_id):
    cursor.execute("SELECT * FROM people WHERE id=?", (people_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data


def model_get_company_by_id(company_id):
    cursor.execute("SELECT * FROM companies WHERE id=?", (company_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data

def model_update_ad(id, title, descr, wage, place, work_time, idpeople, idcompany):
    cursor.execute('UPDATE advertisements '
                   'SET title = "' + title + '", description = "' + descr + '", wage = "' + wage + '", place = "' +
                   place + '", working_time = "' + work_time + '" , id_people = "' + idpeople + '", id_company ="' +
                   idcompany + '" WHERE id = ' + id)
    connect.commit()

    print("ad updated")

def model_delete_ad(id):
    cursor.execute('DELETE FROM advertisements WHERE id = ' + str(id))
    connect.commit()

    print("ad deleted")


