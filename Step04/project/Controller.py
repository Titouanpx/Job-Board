import mariadb
import sys


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


def create_new_ad(title, descr, wage, place, work_time, idpeople, idcompany):
    cursor.execute("INSERT INTO advertisements (title, description, wage, place, working_time, id_people, id_company)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)", (title, descr, wage, place, work_time, idpeople, idcompany))

    #cursor.commit()

    print("record created")


def get_ad():
    cursor.execute("SELECT * FROM advertisements")
    fetchall_data = cursor.fetchall()
    print(fetchall_data)
    return fetchall_data


def get_ad_by_id(ad_id):
    cursor.execute("SELECT * FROM advertisements WHERE id=?", (ad_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data


def get_people_by_id(people_id):
    cursor.execute("SELECT * FROM people WHERE id=?", (people_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data


def get_company_by_id(company_id):
    cursor.execute("SELECT * FROM companies WHERE id=?", (company_id,))
    fetchone_data = cursor.fetchone()
    return fetchone_data


def get_ad_by_id_foreign_keys(ad_id):
    data = get_ad_by_id(ad_id)
    creator = get_people_by_id(data[6])
    company = get_company_by_id(data[7])
    lstData = list(data)
    lstData[6] = creator[1]
    lstData[7] = company[1]
    data = tuple(lstData)
    return data


def update_ad(title, descr, wage, place, work_time, idpeople, idcompany):
    cursor.execute("UPDATE advertisements "
                   "Set title =" + title + ", description =" + descr + ", wage =" + wage + ", place =" + place +
                   ", working_time =" + work_time + ", id_people =" + idpeople + ", id_company =" + idcompany)

    #cursor.commit()

    print("record updated")


def delete_ad(id):
    cursor.execute("DELETE FROM advertisements WHERE id = %s", id,)

    # cursor.commit()

    print("record deleted")
