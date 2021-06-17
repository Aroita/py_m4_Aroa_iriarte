# Use python to operate the database
import mysql.connector

from sql import *

def crear_motor(id_coche):
    from programa import motor
    if id_coche is None:
        return None


    database = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="909990",
        database="mysqlapp"
    )

    cursor = database.cursor()
    params = (
        motor.cv,
        motor.combustible,
        id_coche

    )



    cursor.execute(sql_insert_motor, params)
    database.commit()
    result_num = cursor.rowcount
    cursor.close()
    database.close()
    return False if result_num == 0 else True

    for db in cursor:
        print(db)





